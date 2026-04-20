from pathlib import Path

from pygrpdfimage.pdf_to_image import PDFToImage


def test_convert_pdf_base_64():

    path_pdf = '/home/ruizgabriel161/workspace/python/pygrpdfocr/docs/atestado.pdf'

    pdf_image = PDFToImage()

    images = pdf_image.convert(Path(path_pdf))

    for i, img in enumerate(images, start=1):
        b64 = pdf_image.pil_to_base64(img=img, fmt='PNG')
        assert isinstance(b64, str)
