from abc import ABC, abstractmethod


class ProviderConfig(ABC):
    """
    Classe abstrata para configuração dos provider de llm
    """

    @abstractmethod
    def build_params(self, llm: str, endpoint: str | None) -> dict: ...

    @abstractmethod
    def check_installed(self) -> None: ...
