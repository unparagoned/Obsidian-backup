"""Page numbers for the exported report PDF.

Usage (after exporting Report mod to PDF from Obsidian):

  1. Stamp a footer onto every page, writes <name> numbered.pdf:
       python3 "Z pdf page numbers.py" stamp "report.pdf"

  2. Fill real page numbers into the markdown Contents (run BEFORE the
     final export, on a draft export of the same file):
       python3 "Z pdf page numbers.py" toc "report.pdf" "Z Project Report - Report mod.md"
     Then re-export the PDF and run step 1 on it. Because adding the
     numbers does not add or remove lines, pagination is unchanged, but
     re-run step 2 afterwards to confirm every number still matches; it
     prints CHANGED if anything moved.

Requires pymupdf: python3 -m pip install pymupdf
"""
import re, sys

def stamp(pdf_path):
    import pymupdf
    doc = pymupdf.open(pdf_path)
    total = len(doc)
    for i, page in enumerate(doc, 1):
        rect = page.rect
        page.insert_text((rect.width/2 - 30, rect.height - 20),
                         f"Page {i} of {total}", fontsize=9,
                         fontname="helv", color=(0.35, 0.35, 0.35))
    out = pdf_path.replace(".pdf", " numbered.pdf")
    doc.save(out)
    print("written:", out)

def heading_page(doc, text):
    """Last page on which the heading text occurs (first is the Contents)."""
    hits = []
    for i, page in enumerate(doc, 1):
        if page.search_for(text):
            hits.append(i)
    return hits[-1] if hits else None

def toc(pdf_path, md_path):
    import pymupdf
    doc = pymupdf.open(pdf_path)
    md = open(md_path).read()
    lines = md.split("\n")
    start = next(i for i, l in enumerate(lines) if l.strip() == "# Contents")
    end = next(i for i in range(start+1, len(lines)) if lines[i].startswith("# "))
    changed = 0
    for i in range(start+1, end):
        m = re.match(r"^(\s*- \[\[#[^|\]]+\|([^\]]+)\]\])( \(p\. \d+\))?\s*$", lines[i])
        if not m:
            continue
        page = heading_page(doc, m.group(2))
        if page is None:
            print("NOT FOUND:", m.group(2)[:60])
            continue
        new = f"{m.group(1)} (p. {page})"
        if new != lines[i]:
            if m.group(3):
                print("CHANGED:", m.group(2)[:50], m.group(3), "->", page)
            lines[i] = new
            changed += 1
    open(md_path, "w").write("\n".join(lines))
    print(f"updated {changed} entries")

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "stamp":
        stamp(sys.argv[2])
    elif len(sys.argv) >= 4 and sys.argv[1] == "toc":
        toc(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
