from pygrocrimage.ocr.base_orc import OCRBase as OCRBase
from pygrocrimage.ocr.ocr_llm import OCRImageLLM as OCRImageLLM
from pygrocrimage.ocr.orc_tesseract import OCRTesseract as OCRTesseract
from typing import Literal

class OCRFactory:
    @staticmethod
    def create(engine: Literal['llm', 'tesseract'], llm: str | None = None, model_provider: str | None = None, endpoint: str | None = None, lang: str = 'por') -> OCRBase: ...
