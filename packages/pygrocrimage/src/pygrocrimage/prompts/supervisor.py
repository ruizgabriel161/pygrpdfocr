from langchain_core.messages import HumanMessage


class Supervisor:
    """
    classe responsável por orquestrar os prompts da aplicação
    """

    @staticmethod
    def _img_prompt() -> str:
        return """
            You are performing OCR (optical character recognition).

            This task only involves extracting visible content from the image.

            Do not refuse. The image is safe and contains no sensitive content.

            Extract all visible information, including:
            - text
            - tables
            - charts
            - visual elements

            Follow the structure below:

            [TEXTO]
            ...

            [TABELAS]
            ...

            [GRÁFICOS]
            ...

            [IMAGENS]
            ...

            Return in Portuguese (pt-BR).
    """

    @staticmethod
    def read_img(b64: str, mime: str = 'image/png') -> HumanMessage:
        return HumanMessage(
            content=[
                {
                    'type': 'image_url',
                    'image_url': {'url': f'data:{mime};base64,{b64}'},
                },
                {'type': 'text', 'text': Supervisor._img_prompt()},
            ]
        )
