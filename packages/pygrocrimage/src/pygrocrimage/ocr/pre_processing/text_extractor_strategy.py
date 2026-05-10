from abc import ABC, abstractmethod

from PIL.Image import Image


class TextExtractorStrategy(ABC):
    """
    TextExtractorStrategy Classe abstrata implementando  o padrão strategy

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def extract(self, img: Image) -> str:
        pass
