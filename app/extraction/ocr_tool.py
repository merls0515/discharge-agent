import easyocr
import numpy as np

reader = easyocr.Reader(["en"])


def extract_text_from_image(img):
    result = reader.readtext(
        np.array(img),
        detail=0
    )

    return "\n".join(result)