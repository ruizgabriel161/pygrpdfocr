import base64
import logging
from io import BytesIO
from pathlib import Path
from typing import List, Literal

from pdf2image import convert_from_path
from PIL.Image import Image, Resampling


class PDFToImage:
    """
    classe responsável por converter PDF em imagem
    """

    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def convert(self, pdf_path: Path, **kwargs) -> List[Image]:
        """
        convert Metodo responsável por converter o pdf

         Args:
             pdf_path (Path): caminho do arquivo

         Raises:
             e: erro ao converter em umagem

         Returns:
             List[Image]: salva as imagens em uma lista
        """

        try:
            images: List[Image] = convert_from_path(pdf_path=str(pdf_path), **kwargs)
        except FileNotFoundError as e:
            self._logger.error(f'Arquivo não existe {e} - {type(e).__name__}')

            raise FileNotFoundError('Arquivo passado não existe. Verifique o arquivo')

        except Exception as e:
            self._logger.error(
                f'erro ao transformar em imagem {e} - {type(e).__name__}'
            )
            raise e
        else:
            self._logger.info('arquivo convertido')

        return images

    def convert_to_save(
        self,
        pdf_path: Path,
        output_dir: Path,
        output_suffix: str = 'page',
        fmt: Literal['PNG', 'JPEG'] = 'PNG',
        **kwargs,
    ) -> List[Path]:
        """
        convert Método responsável por converter pdf em imagem.
        Abstrai a função da lib pdf2image

        Args:
            pdf_path (Path): caminho do arquivo
            output_suffix (str, optional): sufixo das imagem. Defaults to 'page'.
            fmt (Literal[&#39;PNG&#39;, &#39;JPEG&#39;], optional): Formato de saída da
            imagem. Defaults to 'PNG'.

        Returns:
            List[Path]: retorna a lista de páginas
        """

        images: List[Image] = self.convert(pdf_path=pdf_path, **kwargs)

        output_dir.mkdir(parents=True, exist_ok=True)

        output_files = []

        for i, img in enumerate(images, start=1):
            self._logger.info(f'convertendo página {i}/{len(images)}')
            filename = f"""
                    {output_dir}/{pdf_path.name[: pdf_path.name.rfind('.')]}_{output_suffix}_{i}.{fmt.lower()}
                    """

            img.save(fp=filename, format=fmt)
            output_files.append(filename)

        return output_files

    def resize_if_needed(self, img: Image, max_px: int = 2048) -> Image:
        """
        resize_if_needed Metodo responsável por redefinir o tamanho da imagem

        Args:
            img (Image): imagem
            max_px (int, optional): tamanho máximo da imagem. Defaults to 2048.

        Returns:
            Image: imagem redimensionada
        """

        w, h = img.size  # tamanho da imagem
        if max(w, h) <= max_px:
            return img
        scale = max_px / max(w, h)  # escala da imagem
        return img.resize(
            (int(w * scale), int(h * scale)), Resampling.LANCZOS
        )  # redefine a imagem

    def pil_to_base64(
        self, img: Image, fmt: Literal['PNG', 'JPEG'] = 'PNG', encoding: str = 'utf-8'
    ) -> str:

        buf = BytesIO()  # abre um buffer na memória
        img.save(buf, format=fmt)  # salva a imagem no buffer
        return base64.b64encode(buf.getvalue()).decode(
            encoding
        )  # converter o buffer em base64
