from abc import ABC, abstractmethod

from PIL.Image import Image


class ImagePreprocessor(ABC):
    """
    ImagePreprocessor Classe abstrata para processar a imagem

    Args:
        ABC (_type_): Abstração
    """

    @abstractmethod
    def process(self, img: Image) -> Image: ...
