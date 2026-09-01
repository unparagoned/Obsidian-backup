"""Regenerate the Contents block of the report from its headings, with PDF page numbers.
Usage: python update_contents.py <report.md> [<report.pdf>]
Entries: numbered H1/H2 sections, Appendix H2s, and A1-A7 / B1-B44 H3s. Aliases = heading text, backticks stripped."""
import re,sys,json
md_path=sys.argv[1]; pdf_path=sys.argv[2] if len(sys.argv)>2 else None
lines=open(md_path).read().split("\n")
ci=lines.index("# Contents"); cj=next(i for i in range(ci+1,len(lines)) if lines[i].startswith("# "))
entries=[]
for i in range(cj,len(lines)):
    m=re.match(r"^(#{1,3}) (.+?)\s*$",lines[i])
    if not m: continue
    lvl,h=len(m.group(1)),m.group(2)
    if lvl==1 and re.match(r"^\d+\.",h): entries.append((0,h))
    elif lvl==2 and re.match(r"^\d+\.\d+",h): entries.append((1,h))
    elif lvl==2 and h.startswith("Appendix "): entries.append((1,h))
    elif lvl==3 and re.match(r"^[AB]\d+\.",h): entries.append((2,h))
strip=lambda h: h.replace("`","")
pages=None
if pdf_path:
    from pypdf import PdfReader
    norm=lambda t: re.sub(r"\s+"," ",re.sub(r"[`*_\"“”’']","",t)).strip().lower()
    ptext=[norm(p.extract_text() or "") for p in PdfReader(pdf_path).pages]
    pages=[]; last=0
    for _,h in entries:
        key=norm(h); pg=None
        for k in (key,key[:60],key[:40]):
            for pi in range(max(0,last-1),len(ptext)):
                if k in ptext[pi]: pg=pi+1; break
            if pg: break
        if pg: last=pg
        pages.append(pg)
    total=len(ptext)
out=[]
for n,(lvl,h) in enumerate(entries):
    target=strip(h); alias=strip(h).rstrip(".")
    if lvl==0: alias=re.sub(r"^(\d+)\.\s*",r"\1. ",alias)
    pg=""
    if pages:
        p=pages[n]
        pg=f" (p. {p})" if p else " (p. ?)"
        if n==len(entries)-1 and p and total>p: pg=f" (pp. {p}–{total})"
    out.append("  "*lvl+f"- [[#{target}|{alias}]]{pg}")
lines[ci+1:cj]=[""]+out+[""]
open(md_path,"w").write("\n".join(lines))
print(f"{len(entries)} entries written; unresolved pages: {[h for (l,h),p in zip(entries,pages) if not p] if pages else 'n/a'}")
