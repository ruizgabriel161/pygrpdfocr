from pygrocrimage.utils.providers.anthropic_config import AnthropicConfig
from pygrocrimage.utils.providers.gemini_config import GerminiConfig
from pygrocrimage.utils.providers.ollama_config import OllamaConfig
from pygrocrimage.utils.providers.openai_config import OpenAIConfig
from pygrocrimage.utils.providers.providers import ProviderConfig


class ProviderFactory:
    """
    Classe responsável por retor o config correto a partir do provider
    """

    _PROVIDERS: dict[str, type[ProviderConfig]] = {
        'openai': OpenAIConfig,
        'google_genai': GerminiConfig,
        'ollama': OllamaConfig,
        'anthropic': AnthropicConfig,
    }

    @classmethod
    def create(cls, model_provider: str) -> ProviderConfig:
        config = cls._PROVIDERS.get(model_provider)

        if config is None:
            available = ', '.join(cls._PROVIDERS.keys())

            raise ValueError(
                f'Provider {model_provider} não suportado.Disponíveis: {available}'
            )
        return config()
