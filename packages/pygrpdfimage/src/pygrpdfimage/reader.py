import logging
from pathlib import Path
from typing import List

from pdf2image import convert_from_path
from PIL.Image import Image


class PDF2ImageReader:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def convert(self, pdf_path: Path, **kwargs) -> List[Image]:
        '''
        convert Metodo responsável por converter o pdf em imagem

        Args:
            pdf_path (Path): caminho do PDF

        Raises:
            FileNotFoundError: Arquivo não encontrado

        Returns:
            List[Image]: lista de imagem
        '''        
        try:
            images = convert_from_path(str(pdf_path), **kwargs)
            self._logger.info('PDF convertido com sucesso')
            return images

        except FileNotFoundError as e:
            self._logger.error(f'Arquivo não existe: {e}')
            raise FileNotFoundError('Arquivo não encontrado')

        except Exception as e:
            self._logger.error(f'Erro ao converter PDF: {e}')
            raise
