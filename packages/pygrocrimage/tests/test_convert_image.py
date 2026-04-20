from pathlib import Path

from pygrpdfimage.pdf_to_image import PDFToImage

from pygrocrimage.ocr.factory_orc import OCRFactory


def main(model: str, pdf_path: str, model_provider: str, base_url: str):
    pdf_to_image = PDFToImage()

    image = pdf_to_image.convert(pdf_path=Path(pdf_path))[-1]

    # b64 = pdf_to_image.pil_to_base64(img=image)

    ocr = OCRFactory.create(engine='tesseract', lang='por')

    text = ocr.extract_text(img=image)

    ocr.save_txt(
        text=text,
        output_path='/home/ruizgabriel161/workspace/python/pygrpdfocr/docs/pdf/teste.txt',
    )


if __name__ == '__main__':
    model = 'llava:7b'
    model_provider = 'ollama'
    base_url = 'http://172.22.128.1:11434'
    pdf_path = (
        '/home/ruizgabriel161/workspace/python/pygrpdfocr/docs/pdf/Esclarecimento.pdf'
    )
    main(
        model=model, pdf_path=pdf_path, model_provider=model_provider, base_url=base_url
    )
