import logging
from pathlib import Path
from typing import List

from PIL.Image import Image


class ImageSaver:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def save(
        self,
        images: List[Image],
        output_dir: Path,
        base_name: str,
        fmt: str = 'PNG',
        suffix: str = 'page',
    ) -> List[Path]:
        '''
        save Método responsável por salvar a imagem

        Args:
            images (List[Image]): imagem
            output_dir (Path): caminho do salvamento
            base_name (str): nome do arquivo
            fmt (str, optional): formato do arquivo. Defaults to 'PNG'.
            suffix (str, optional): sufixo do arquivo. Defaults to 'page'.

        Returns:
            List[Path]: uma lista de imagem
        '''        
        output_dir.mkdir(parents=True, exist_ok=True)

        paths = []

        for i, img in enumerate(images, start=1):
            filename = output_dir / f'{base_name}_{suffix}_{i}.{fmt.lower()}'

            self._logger.info(f'Salvando {filename}')
            img.save(filename, format=fmt)

            paths.append(filename)

        return paths
