import logging
from typing import cast

from langchain.chat_models import BaseChatModel, init_chat_model


class LoadLLM:
    """Classe responsável por carregar os modelos de LLM"""

    def __init__(
        self,
        llm: str,
        model_provider,
        endpoint: str | None = None,
        api_key: str | None = None,
    ) -> None:
        """
        Construtor da classe LoadLLM

        Keyword Arguments:
            llm (str) -- modelo usado no projeto (default: {Settings.MODEL})
            model_provider (str) --provedor do modelo (default: {Settings.MODEL})
            base_url (str) -- url onde o modelo está ridando (default: {Settings.MODEL})
        """
        self.llm = llm
        self.model_provider = model_provider
        self.endpoint = endpoint
        self.api_key = api_key
        self._logger: logging.Logger = logging.getLogger(__name__)

    def init_llm(self) -> BaseChatModel:
        params: dict = self._set_model_connect()

        try:
            model = cast('BaseChatModel', init_chat_model(**params))

            assert hasattr(model, 'bind_tools')
            assert hasattr(model, 'invoke')
            assert hasattr(model, 'with_config')

            self._logger.info('Modelo carregado com sucesso!')

        except Exception as e:
            self._logger.critical(f'Erro ao carregar o modelo {self.llm=}, {e}')
            raise ValueError(f'Erro ao carregar o modelo {self.llm=}, {e}')

        return model

    def _set_model_connect(self) -> dict[str, str | float]:
        _PROVIDER_PARAMS: dict = {
            'ollama': {'base_url'},
            'google_genai': {'api_key'},
            'anthropic': {'api_key'},
            'openai': {'api_key', 'base_url'},
        }

        params: dict = {
            'model': self.llm,
            'model_provider': self.model_provider,
            'temperature': 0,
        }

        allowed = _PROVIDER_PARAMS.get(self.model_provider, set())

        if 'base_url' in allowed and self.endpoint:
            params['base_url'] = self.endpoint

        if 'api_key' in allowed and self.api_key:
            params['api_key'] = self.api_key
        return params
