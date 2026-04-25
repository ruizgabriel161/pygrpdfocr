from _typeshed import Incomplete
from langchain.chat_models import BaseChatModel as BaseChatModel

class LoadLLM:
    llm: Incomplete
    model_provider: Incomplete
    endpoint: Incomplete
    api_key: Incomplete
    def __init__(self, llm: str, model_provider, endpoint: str | None = None, api_key: str | None = None) -> None: ...
    def init_llm(self) -> BaseChatModel: ...
