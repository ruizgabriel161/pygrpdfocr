from typing import override

from PIL.Image import Image
from pytesseract import image_to_string

from pygrocrimage.ocr.base_orc import OCRBase


class OCRTesseract(OCRBase):
    """
    Classe responsável por extrair texto de imagem via Tesseract
    """

    def __init__(self, lang: str = 'por') -> None:
        super().__init__()
        self.lang: str = lang

    @override
    def extract_text(self, img: Image) -> str:
        """
        extract Método responsável por extrair o texto para imagem

        Args:
            img (Image): Imagem

        Raises:
            e: Erro na conversão da imagem

        Returns:
            str: Retono do texto
        """
        try:
            text = image_to_string(image=img, lang=self.lang)
            self._logger.info('Texto extraído com sucesso')
            return text
        except Exception as e:
            self._logger.error(f'Erro ao extrair texto {e} - {type(e).__name__}')
            raise e

    def extract_batch(self, images: list[Image]) -> list[str]:
        """
        extract_batch Método responsável por extrair as páginas em lote

        Args:
            images (list[Image]): imagens a ser extraídas

        Returns:
            list[str]: retorna uma lista de string
        """
        texts = []
        for i, img in enumerate(images, start=1):
            self._logger.info(f'Extraindo texto página {i}/{len(images)}')
            texts.append(self.extract_text(img=img))

        return texts
