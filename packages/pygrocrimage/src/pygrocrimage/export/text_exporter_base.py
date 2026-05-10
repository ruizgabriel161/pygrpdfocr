from abc import ABC, abstractmethod


class TextExporterBase(ABC):
    """
    Classe abstrata para tratar de exportação de dados
    """

    @abstractmethod
    def export(self, text: str | list[str], output_path: str) -> None: ...
