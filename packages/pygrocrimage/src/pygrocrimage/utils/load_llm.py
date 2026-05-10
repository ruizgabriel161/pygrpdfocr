import logging
from typing import cast

from langchain.chat_models import BaseChatModel, init_chat_model

from pygrocrimage.utils.providers.provider_factory import ProviderFactory


class LoadLLM:
    """Classe responsável por carregar os modelos de LLM"""

    def __init__(self, llm: str, model_provider, endpoint: str | None = None) -> None:
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
        self.config = ProviderFactory.create(model_provider=model_provider)
        self._logger: logging.Logger = logging.getLogger(__name__)

    def init_llm(self) -> BaseChatModel:
        '''
        init_llm Método responsável por iniciar a llm

        Raises:
            ValueError: erro de importação da llm

        Returns:
            BaseChatModel: Instancia da llm
        '''        
        try:
            self.config.check_installed()
        except ImportError as e:
            self._logger.critical(f'Provider não instalado {e}')
            raise

        params: dict = self.config.build_params(
            self.llm,
            self.endpoint
        )

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

