from abc import ABC, abstractmethod


class PDFTextDetector(ABC):
    """
    PDFTextDetector Classe abstrata para detectar texto vetorial e extrair o texto

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def has_text(self, pdf_path: str) -> bool:
        pass

    @abstractmethod
    def extract_text(self, pdf_path: str) -> str:
        pass
