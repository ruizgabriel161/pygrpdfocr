from typing import override

import pandas as pd
from PIL.Image import Image
from pytesseract import Output, image_to_data

from pygrocrimage.ocr.base_orc import OCRBase
from pygrocrimage.ocr.pre_processing.pdf_text_detector import PDFTextDetector
from pygrocrimage.ocr.pre_processing.text_extractor_strategy import (
    TextExtractorStrategy,
)
from pygrocrimage.ocr.tesseract.tesseract_base import TableExtractorBase
from pygrocrimage.ocr.tesseract.tesseract_table_parse import TesseractTableParser
from pygrocrimage.ocr.tesseract.tesseract_text_extractor import TesseractTextExtractor


class OCRTesseract(OCRBase, TableExtractorBase):
    def __init__(
        self,
        lang: str = 'por',
        psm: int = 6,
        text_extractor: TextExtractorStrategy | None = None,
        table_parser: TesseractTableParser | None = None,
    ) -> None:
        super().__init__()
        self.lang = lang
        self.config = f'--psm {psm}'
        self._extractor = text_extractor or TesseractTextExtractor()
        self._parser = table_parser or TesseractTableParser()  # DIP via injeção

    def extract_tesseract_text(self, img: Image) -> str:
        """
        extract_tesseract_text Método responsável por extrair texto da imagem

        Args:
            img (Image): imagem

        Raises:
            e: erro ao extrair o arquivo

        Returns:
            str: texto extraído
        """
        try:
            text = self._extractor.extract(img)

            self._logger.info('Texto extraído com sucesso')
            return text
        except Exception as e:
            self._logger.error(f'Erro ao extrair texto {e} - {type(e).__name__}')
            raise e

    @override
    def extract_text(
        self,
        pdf_path: str,
        images: list[Image],
        detector: PDFTextDetector,
    ) -> str | list[str]:
        """
        extract_pdf_text Método responsável por orquestrar a extração

        Args:
            pdf_path (str): caminho do pdf
            images (list[Image]): imagem extraída
            detector (PDFTextDetector): detectar a vetorização do texto

        Raises:
            e: caso de erro na extração do texto

        Returns:
            str: retorna o texto extraído
        """

        try:
            # verifica se o pdf possui ocr vetorial
            if detector.has_text(pdf_path):
                self._logger.info(
                    'PDF possui camada textual. Extração direta iniciada.'
                )
                # Extraí o texto via pdf
                return detector.extract_text(pdf_path)

            # ==========================================
            # OCR fallback
            # ==========================================

            self._logger.info('PDF sem camada textual. Executando OCR.')
            # extrai o texto via tesseract
            texts = [self.extract_tesseract_text(img) for img in images]
            if len(images) > 1:
                return texts
            return '\n'.join(texts)

        except Exception as e:
            self._logger.error(f'Erro ao extrair pdf {e} - {type(e).__name__}')
            raise e

    @override
    def extract_table(self, img: Image) -> pd.DataFrame:
        """
        extract_table Método responsável por extrair a tabela do pdf

        Args:
            img (Image): imagem

        Raises:
            e: erro na extração

        Returns:
            pd.DataFrame: tabela extraída
        """
        try:
            raw = image_to_data(
                image=img,
                lang=self.lang,
                config=self.config,
                output_type=Output.DATAFRAME,
            )
            df = self._parser.parse(raw)  # delega a reconstrução
            self._logger.info(f'Tabela extraída: {df.shape}')
            return df
        except Exception as e:
            self._logger.error(f'Erro ao extrair tabela {e} - {type(e).__name__}')
            raise e

    @override
    def extract_table_batch(self, images: list[Image]) -> list[pd.DataFrame]:
        return [self.extract_table(img) for img in images]
