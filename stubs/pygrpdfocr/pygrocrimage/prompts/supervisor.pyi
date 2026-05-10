from langchain_core.messages import HumanMessage

class Supervisor:
    @staticmethod
    def read_img(b64: str, mime: str = 'image/png') -> HumanMessage: ...
