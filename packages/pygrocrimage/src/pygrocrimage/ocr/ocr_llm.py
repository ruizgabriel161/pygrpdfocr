from typing import override

from langchain.chat_models import BaseChatModel
from langchain_core.messages import AIMessage

from pygrocrimage.ocr.base_orc import OCRBase
from pygrocrimage.prompts.supervisor import Supervisor
from pygrocrimage.utils.load_llm import LoadLLM


class OCRImageLLM(OCRBase):
    """
    classe responsável por orquestrar a lib
    """

    def __init__(self, llm: str, model_provider: str, endpoint: str) -> None:
        super().__init__()
        self._llm: BaseChatModel = LoadLLM(
            llm=llm, model_provider=model_provider, endpoint=endpoint
        ).init_llm()

    @override
    def extract_text(self, b64: str) -> str:
        """
        extract_text Metodo responsável por enviar o texto em b64 para a llm

        Args:
            b64 (str): imagem convertida em b64

        Raises:
            e: erro na conversão

        Returns:
            str: retorno da llm
        """
        prompt = Supervisor().read_img(b64=b64, mime='image/png')
        try:
            response: AIMessage = self._llm.invoke([prompt])

        except Exception as e:
            self._logger.error(
                f'Erro ao extrair o texto. Error: {e} - type:{type(e).__name__}'
            )
            raise e
        return response.text
