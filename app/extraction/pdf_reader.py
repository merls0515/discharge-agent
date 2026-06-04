import fitz
import io

from PIL import Image
from app.extraction.ocr_tool import extract_text_from_image


def extract_pdf(pdf_path):
    pages = []

    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        print(f"Processing page {page_num + 1}")
        page = doc[page_num]

        digital_text = page.get_text().strip()

        used_ocr = False

        if len(digital_text) < 20:
            pix = page.get_pixmap(dpi=50)
            

            image_bytes = pix.tobytes("png")

            image = Image.open(
                io.BytesIO(image_bytes)
            )
            print("Running OCR...")

            final_text = extract_text_from_image(image)

            print("OCR completed")

            used_ocr = True

        else:
            final_text = digital_text

        pages.append(
            {
                "page_number": page_num + 1,
                "text": final_text,
                "digital_text": digital_text,
                "used_ocr": used_ocr,
            }
        )

    doc.close()

    return pages