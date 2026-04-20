import logging
from abc import ABC, abstractmethod
from pathlib import Path


class OCRBase(ABC):
    """
    Classe abstrata para implementar o OCR
    """

    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    @abstractmethod
    def extract_text(self, **kwargs) -> str:
        pass

    def save_txt(self, text: str, output_path: str) -> None:
        """
        save_txt Método responsável por salvar o texto em txt

        Args:
            text (str): texto a ser salvo
            output_path (str): caminho do arquivo gerado
        """
        Path(output_path).write_text(text, encoding='utf-8')
