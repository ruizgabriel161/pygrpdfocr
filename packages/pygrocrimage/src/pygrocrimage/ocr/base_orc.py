import logging
from abc import ABC, abstractmethod

from pygrocrimage.export.text_exporter_base import TextExporterBase


class OCRBase(ABC):
    """
    Classe abstrata para implementar o OCR
    """

    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    @abstractmethod
    def extract_text(self, **kwargs) -> str:
        pass

    def save(self, text: str | list[str], output_path: str, exporter: TextExporterBase) -> None:
        """
        save Metodo responsável por salvar o arquivo gerado

        Args:
            text (str): texto gerado
            output_path (str): caminho do salvamento
            exporter (TextExporterBase): tipo de exporte

        Raises:
            e: erro no salvamento
        """
        try:
            exporter.export(text=text, output_path=output_path)
            self._logger.info(f'Arquivo salvo: {output_path}')
        except Exception as e:
            self._logger.error(f'Erro ao salvar {e}')
            raise e
