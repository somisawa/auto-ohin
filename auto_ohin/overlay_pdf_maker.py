from typing import List

import pathlib

from reportlab.pdfgen import canvas
from PIL import Image

PDF_SIZE = {
    "A0": (1189, 841),
    "A1": (841, 564),
    "A2": (564, 420),
    "A3": (420, 297),
    "A4": (297, 210),
    "A5": (210, 48),
}

DPI = (842, 595)


def mm_to_pixel(mms: List[int], size_name: str):

    pixel = [1.0, 1.0]
    for i in range(2):
        pixel[i] = int(DPI[i] * mms[i] / PDF_SIZE[size_name][i])

    return tuple(pixel)


def overlay_pdf_maker(overlay_path: str, img_path: str, position: List[float], img_size: List[float], pdf_size: str = "A4") -> None:

    x, y = mm_to_pixel(position, pdf_size)

    c = canvas.Canvas(overlay_path)

    c.drawImage(img_path, x, y,
                width=img_size[0], height=img_size[1], mask='auto')

    c.showPage()
    c.save()


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    for i in [2, 3, 4, 5]:
        args[i] = int(args[i])

    overlay_pdf_maker(*args)
