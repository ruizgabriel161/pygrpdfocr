from importlib.util import find_spec
from typing import override

from pygrocrimage.utils.providers.providers import ProviderConfig


class OpenAIConfig(ProviderConfig):
    """
    Classe responsável por configurar o provider do gpt
    """

    @override
    def check_installed(self) -> None:
        """
        check_installed Método responsável por checar a instalação do pacote da llm

        Raises:
            ImportError: Erro de import. Inexistencia da biblioteca
        """
        if find_spec('langchain_openai') is None:
            raise ImportError(
                'Instale com o pip install pygrocrimage[openai]'
            ) from None

    @override
    def build_params(self, llm: str, endpoint: str | None) -> dict:
        """
        build_params Método responsável por buildar os parametros

        Args:
            llm (str): modelo da llm
            endpoint (str | None): conexão da llm

        Returns:
            dict: retorna o parametro
        """
        params = {'model': llm, 'model_provider': 'openai', 'temperature': 0}
        if endpoint:
            params['api_key'] = endpoint
        return params
