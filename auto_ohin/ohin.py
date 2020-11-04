import os

from typing import List

from overlay_pdf_maker import overlay_pdf_maker

from PyPDF4 import PdfFileReader, PdfFileWriter


def ohin(obj_pages: List[int], save_path: str, input_path: str, img_path: str, position: List[float], img_size: List[float], pdf_size: str = "A4") -> None:

    overlay_pdf_maker("overlay.pdf", img_path, position, img_size, pdf_size)

    f_overlay = open("overlay.pdf", 'rb')
    overlay = PdfFileReader(f_overlay).getPage(0)

    f_target = open(input_path, 'rb')
    reader = PdfFileReader(f_target)
    num_pages = reader.getNumPages()

    assert num_pages >= max(obj_pages)

    for p in obj_pages:
        page = reader.getPage(p - 1)
        page.mergePage(overlay)

    writer = PdfFileWriter()
    for p in range(num_pages):
        page = reader.getPage(p)
        writer.addPage(page)

    with open(save_path, 'wb') as f:
        writer.write(f)

    f_overlay.close()
    f_target.close()

    os.remove("overlay.pdf")


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    for i in [0, 1, 5, 6, 7, 8]:
        args[i] = int(args[i])

    obj_pages = args[:2]

    ohin(obj_pages, *args[2:])
