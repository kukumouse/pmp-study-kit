from pathlib import Path
from pypdf import PdfReader

PDF = Path(r"D:\PMP考试相关资料\PMP新版通关宝典.pdf")
OUT = Path("ocr_pages")
OUT.mkdir(exist_ok=True)

reader = PdfReader(str(PDF))
for page_index in range(3):
    images = list(reader.pages[page_index].images)
    if not images:
        print(f"page {page_index + 1}: no images")
        continue
    image = images[0]
    suffix = Path(image.name).suffix or ".tiff"
    path = OUT / f"page_{page_index + 1:03d}{suffix}"
    path.write_bytes(image.data)
    print(path)
