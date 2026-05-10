from typing import override

from langchain.chat_models import BaseChatModel as BaseChatModel
from langchain_core.messages import AIMessage as AIMessage
from pygrocrimage.ocr.base_orc import OCRBase as OCRBase
from pygrocrimage.prompts.supervisor import Supervisor as Supervisor
from pygrocrimage.utils.load_llm import LoadLLM as LoadLLM

class OCRImageLLM(OCRBase):
    def __init__(self, llm: str, model_provider: str, endpoint: str) -> None: ...
    @override
    def extract_tesseact_text(self, b64: str) -> str: ...
