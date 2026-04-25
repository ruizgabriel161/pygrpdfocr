import base64
import logging
from io import BytesIO

from PIL.Image import Image


class ImageSerializer:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def to_base64(self, img: Image, fmt: str = 'PNG') -> str:
        """
        to_base64 Método responsável por converter a imagem em bas64

        Args:
            img (Image): imagem
            fmt (str, optional): formato da imagem. Defaults to 'PNG'.

        Returns:
            str: _description_
        """

        buffer = BytesIO()
        img.save(buffer, format=fmt)
        return base64.b64encode(buffer.getvalue()).decode('utf-8')
