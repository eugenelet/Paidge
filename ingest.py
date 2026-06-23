import json
import os
import re
from openai import OpenAI
from pypdf import PdfReader

# Initialize Ollama client
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

PDF_DIR = "./papers"
DB_FILE = "./_data/paper_db.json"
BASE_KNOWLEDGE_DIR = "./notes"
MASTER_PAGE_FILE = "./reading-list.md"

TAXONOMY = {
    "Test-Time Adaptation": "🔄",
    "In-Context Learning": "🧠",
    "Efficient Architectures": "⚡",
    "Multimodal & Vision": "👁️",
    "Embodied AI & Robotics": "🤖",
    "Theory & Optimization": "📐",
}


def derive_arxiv_date(arxiv_id):
    """Deterministically converts an arXiv ID (e.g. '2605.12345') into an ISO '2026-05' date"""
    if not arxiv_id:
        return None
    match = re.match(r"^(\d{2})(\d{2})\.", arxiv_id)
    if match:
        year, month = match.groups()
        return f"20{year}-{month}"
    return None


def load_db():
    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    patched = False
    for filename, data in db.items():
        if "pub_date" not in data:
            aid = extract_arxiv_id(filename, "")
            data["pub_date"] = derive_arxiv_date(aid) or "2026-01"
            patched = True

    if patched:
        save_db(db)

    return db


def save_db(db):
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)


def extract_arxiv_id(filename, text):
    match = re.search(r"\b\d{4}\.\d{4,5}(?:v\d+)?\b", filename)
    if match:
        return match.group(0)
    match = re.search(r"\b\d{4}\.\d{4,5}(?:v\d+)?\b", text)
    return match.group(0) if match else None


def clean_slug(name):
    return re.sub(r'[\\/*?:"<>|]', "", name).strip().replace(" ", "_").lower()


def extract_key_sections(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        num_pages = len(reader.pages)
        pages_to_read = set([0, 1, 2])

        ref_page = next(
            (
                i
                for i in range(num_pages)
                if any(
                    k in (reader.pages[i].extract_text() or "").lower()
                    for k in ["references", "bibliography"]
                )
            ),
            None,
        )

        if ref_page and ref_page > 2:
            pages_to_read.update([ref_page - 2, ref_page - 1])
        else:
            pages_to_read.update([max(0, num_pages - 2), max(0, num_pages - 1)])

        return "\n".join(
            f"--- PAGE {i+1} ---\n{reader.pages[i].extract_text() or ''}"
            for i in sorted(pages_to_read)
            if i < num_pages
        )
    except Exception as e:
        print(f"PDF Error in {pdf_path}: {e}")
        return None


def synthesize_frontier(topic, paper_list):
    if not paper_list:
        return "Awaiting empirical literature for this vector."

    takeaways_bulleted = "\n".join(f"- {p['takeaway']}" for p in paper_list)

    prompt = f"""
    You are an elite academic AI research director. Look at the core empirical takeaways extracted from the literature tracked under the research pillar '{topic}':
    
    {takeaways_bulleted}
    
    Synthesize these distinct points into a dense, cohesive 2-sentence summary of the "Current Field Frontier". 
    Focus strictly on: What is the overarching paradigm shift, the shared mathematical trajectory, or the collective bottleneck these papers point toward? 
    Write strictly about the science. Do not reference individual paper titles or use conversational filler.
    """

    res = client.chat.completions.create(
        model="qwen3.6",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return res.choices[0].message.content.strip()


def analyze_paper(text):
    allowed_list_str = ", ".join(f'"{k}"' for k in TAXONOMY.keys())
    prompt = f"""
    Analyze this machine learning paper. 
    You MUST categorize it strictly into ONE of these exact 6 Primary Topics: [{allowed_list_str}].
    
    Output strictly in this format:
    
    ---METADATA---
    Primary Category: [Pick exactly one from the 6 allowed topics]
    Short Title: [Clean 3-5 word title for web slug]
    Pub Date: [YYYY-MM format, e.g. 2026-05]
    Core Takeaway: [A single punchy, high-signal sentence summarizing the advancement]
    ---END METADATA---
    
    # [Full Paper Title]
    
    #### 🚀 Technical Novelty
    * **Mechanism**: [Concrete advancement]
    * **Nuance**: [How it differs from prior SOTA]
    
    #### 💡 Yield
    - [Key theoretical or empirical results]
    
    #### ⚠️ Limitations
    - [Authors' admitted constraints]

    Text to analyze:
    {text}
    """

    res = client.chat.completions.create(
        model="qwen3.6",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
    )
    return res.choices[0].message.content


def render_master_reading_list(db, updated_topics):
    if "_frontiers" not in db:
        db["_frontiers"] = {}

    grouped = {t: [] for t in TAXONOMY.keys()}
    for key, entry in db.items():
        if key == "_frontiers":
            continue
        cat = entry.get("topic")
        if cat in grouped:
            grouped[cat].append(entry)

    md = """---
layout: page
title: Reading List
permalink: /reading-list/
---

# 📚 Centralized Reading List & Field Advancements

Select a research vector below to isolate the literature and view its trend.

<div class="topic-filter-container" style="display: flex; gap: 8px; flex-wrap: wrap; margin: 1.5rem 0 2rem 0;">
  <button class="topic-pill active" onclick="filterTopic('all', this)">🌟 All Advancements</button>
"""

    for topic, emoji in TAXONOMY.items():
        if grouped[topic]:
            slug = clean_slug(topic)
            md += f'  <button class="topic-pill" onclick="filterTopic(\'{slug}\', this)">{emoji} {topic}</button>\n'

    md += "</div>\n\n"

    # Updated CSS with Qualcomm Blue (#3253DC) active states and glowing borders
    md += """<style>
  .topic-pill { padding: 6px 14px; background: #1a202c; border: 1px solid #4a5568; color: #a0aec0; border-radius: 20px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.2s; }
  .topic-pill.active { background: #3253DC; color: white; border-color: #6382f2; box-shadow: 0 0 8px rgba(50, 83, 220, 0.4); }
  .topic-pill:hover:not(.active) { background: #2d3748; color: white; }
</style>

<script>
  function filterTopic(slug, btnEl) {
    document.querySelectorAll('.topic-pill').forEach(b => b.classList.remove('active'));
    btnEl.classList.add('active');
    document.querySelectorAll('.topic-section-group').forEach(group => {
      group.style.display = (slug === 'all' || group.getAttribute('data-topic') === slug) ? 'block' : 'none';
    });
  }
</script>

"""

    for topic, papers in grouped.items():
        if not papers:
            continue

        papers.sort(key=lambda x: x.get("pub_date", "0000-00"), reverse=True)

        slug = clean_slug(topic)
        emoji = TAXONOMY[topic]

        if topic in updated_topics or topic not in db["_frontiers"]:
            print(f"   🧠 Synthesizing macro-frontier for '{topic}'...")
            db["_frontiers"][topic] = synthesize_frontier(topic, papers)
            save_db(db)

        frontier_text = db["_frontiers"][topic]

        md += f'<div class="topic-section-group" data-topic="{slug}" markdown="1">\n\n'
        md += f"## {emoji} {topic}\n\n"

        # Executive Slate box with Qualcomm Blue accent bar and high-contrast electric blue header
        md += f"""<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">{frontier_text}</p>
</div>\n\n"""

        md += "| Date | Paper | Core Takeaway |\n| :---: | :--- | :--- |\n"
        for p in papers:
            date_badge = p.get("pub_date", "2026-01")
            md += f"| `{date_badge}` | [{p['short_title']}]({p['web_url']}) | {p['takeaway']} |\n"

        md += "\n</div>\n\n"

    with open(MASTER_PAGE_FILE, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"🔄 Rebuilt master index: {MASTER_PAGE_FILE}")


def main():
    db = load_db()
    os.makedirs(BASE_KNOWLEDGE_DIR, exist_ok=True)
    newly_ingested_topics = set()

    for file in os.listdir(PDF_DIR):
        if not file.endswith(".pdf") or file in db:
            continue

        print(f"\n📑 Ingesting: {file}...")
        pdf_path = os.path.join(PDF_DIR, file)
        text = extract_key_sections(pdf_path)

        if not text:
            continue

        arxiv_id = extract_arxiv_id(file, text)
        arxiv_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None

        raw_meta = analyze_paper(text)

        try:
            meta_box = re.search(
                r"---METADATA---(.*)---END METADATA---", raw_meta, re.DOTALL
            ).group(1)
            topic = re.search(r"Primary Category:\s*(.*)", meta_box).group(1).strip()
            short_title = re.search(r"Short Title:\s*(.*)", meta_box).group(1).strip()
            takeaway = re.search(r"Core Takeaway:\s*(.*)", meta_box).group(1).strip()
            content_md = re.sub(
                r"---METADATA---.*---END METADATA---", "", raw_meta, flags=re.DOTALL
            ).strip()

            pub_date = derive_arxiv_date(arxiv_id)
            if not pub_date:
                date_match = re.search(r"Pub Date:\s*(.*)", meta_box)
                pub_date = date_match.group(1).strip() if date_match else "2026-01"

            matched_topic = next((k for k in TAXONOMY.keys() if k in topic), None)
            if not matched_topic:
                matched_topic = "Theory & Optimization"

            folder_slug = clean_slug(matched_topic)
            file_slug = clean_slug(short_title)
            target_dir = os.path.join(BASE_KNOWLEDGE_DIR, folder_slug)
            os.makedirs(target_dir, exist_ok=True)

            disk_path = os.path.join(target_dir, f"{file_slug}.md")
            web_path = f"/notes/{folder_slug}/{file_slug}.html"

            note_header = f"""---
layout: page
title: "{short_title}"
parent: "{matched_topic}"
---

"""
            src_str = f"**🔗 Source:** [arXiv]({arxiv_url})\n\n" if arxiv_url else ""
            full_note = note_header + src_str + content_md

            with open(disk_path, "w", encoding="utf-8") as f:
                f.write(full_note)

            db[file] = {
                "file": file,
                "short_title": short_title,
                "topic": matched_topic,
                "takeaway": takeaway,
                "pub_date": pub_date,
                "web_url": web_path,
                "arxiv_url": arxiv_url,
            }
            save_db(db)
            newly_ingested_topics.add(matched_topic)
            print(f"   ✓ Succeeded: {short_title} ({pub_date})")

        except Exception as e:
            print(f"   ✗ AI Parsing Failed for {file}: {e}")

    render_master_reading_list(db, newly_ingested_topics)


if __name__ == "__main__":
    main()