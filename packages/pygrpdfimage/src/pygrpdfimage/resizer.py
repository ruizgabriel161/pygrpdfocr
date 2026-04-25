import logging

from PIL.Image import Image, Resampling


class ImageResizer:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def resize_if_needed(self, img: Image, max_px: int = 2048) -> Image:
        """
        resize_if_needed Método responsavel por redimensionar a imagem

        Args:
            img (Image): imagem
            max_px (int, optional): pixel máximo. Defaults to 2048.

        Returns:
            Image: Imagem redimensionada
        """
        w, h = img.size

        if max(w, h) <= max_px:
            return img

        scale = max_px / max(w, h)

        return img.resize((int(w * scale), int(h * scale)), Resampling.LANCZOS)
