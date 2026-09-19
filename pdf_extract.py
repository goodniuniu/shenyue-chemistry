# -*- coding: utf-8 -*-
"""提取真题 PDF 文本到 知识库/化学/素材与拓展/真题试卷/提取文本/。
注意：PDF 中公式符号大量丢失，提取文本仅用于检索考点，做题用原卷 PDF。"""
import sys
from pathlib import Path

import pymupdf

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
EXAM_DIR = ROOT / "知识库" / "化学" / "素材与拓展" / "真题试卷"
OUT_DIR = EXAM_DIR / "提取文本"
OUT_DIR.mkdir(exist_ok=True)

total = 0
for pdf_path in sorted(EXAM_DIR.glob("*.pdf")):
    out_path = OUT_DIR / (pdf_path.stem + ".txt")
    if out_path.exists():
        continue
    parts = []
    with pymupdf.open(pdf_path) as doc:
        n_pages = doc.page_count
        for i, page in enumerate(doc):
            parts.append(f"--- page {i + 1} ---\n" + (page.get_text() or ""))
    text = "\n".join(parts)
    out_path.write_text(text, encoding="utf-8")
    total += len(text)
    print(f"{pdf_path.name}: {n_pages} pages, {len(text)} chars")

print("total chars:", total)
