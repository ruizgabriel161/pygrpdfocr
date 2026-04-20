from typing import Literal, cast

from pygrocrimage.ocr.base_orc import OCRBase
from pygrocrimage.ocr.ocr_llm import OCRImageLLM
from pygrocrimage.ocr.orc_tesseract import OCRTesseract


class OCRFactory:
    """
    classe responsável por implementar o padrão factory
    """

    @staticmethod
    def create(
        engine: Literal['llm', 'tesseract'],
        llm: str | None = None,
        model_provider: str | None = None,
        endpoint: str | None = None,
        lang: str = 'por',
    ) -> OCRBase:
        if engine == 'llm':
            if not all([llm, model_provider, endpoint]):
                raise ValueError(
                    """Para usar a engine llm informe os parametros: '
                    llm, model_provider, endpoint"""
                )
            return OCRImageLLM(
                llm=cast(str, llm),
                model_provider=cast(str, model_provider),
                endpoint=cast(str, endpoint),
            )

        if engine == 'tesseract':
            return OCRTesseract(lang=lang)
