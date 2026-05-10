from typing import override

from PIL.Image import Image as Image
from pygrocrimage.ocr.base_orc import OCRBase as OCRBase

class OCRTesseract(OCRBase):
    lang: str
    def __init__(self, lang: str = 'por') -> None: ...
    @override
    def extract_tesseact_text(self, img: Image) -> str: ...
    def extract_batch(self, images: list[Image]) -> list[str]: ...
