from pathlib import Path
from pypdf import PdfReader

PDF = Path(r"D:\PMP考试相关资料\PMP新版通关宝典.pdf")
OUT = Path("ocr_resource_pages")
OUT.mkdir(exist_ok=True)

START = 154
END = 161

reader = PdfReader(str(PDF))
for page_number in range(START, END + 1):
    page_index = page_number - 1
    images = list(reader.pages[page_index].images)
    if not images:
        print(f"page {page_number}: no images")
        continue
    image = images[0]
    suffix = Path(image.name).suffix or ".tiff"
    path = OUT / f"page_{page_number:03d}{suffix}"
    path.write_bytes(image.data)
    print(path)
