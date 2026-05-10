from typing import override

from PIL.Image import Image
from pytesseract import image_to_string

from pygrocrimage.ocr.pre_processing.image_pre_processor import ImagePreprocessor
from pygrocrimage.ocr.pre_processing.opencv_pre_processor import OpenCVPreprocessor
from pygrocrimage.ocr.pre_processing.text_extractor_strategy import (
    TextExtractorStrategy,
)


class TesseractTextExtractor(TextExtractorStrategy):
    def __init__(
        self,
        lang: str = 'por',
        psm: int = 6,
        preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        self.lang = lang
        self.config = f'--oem 3 --psm {psm}'
        self.preprocessor = preprocessor or OpenCVPreprocessor()

    @override
    def extract(self, img: Image) -> str:
        processed = self.preprocessor.process(img)

        return image_to_string(
            image=processed,
            lang=self.lang,
            config=self.config,
        )
