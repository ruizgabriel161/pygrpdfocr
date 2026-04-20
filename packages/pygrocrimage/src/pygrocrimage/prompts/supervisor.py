from langchain_core.messages import HumanMessage


class Supervisor:
    """
    classe responsável por orquestrar os prompts da aplicação
    """

    @staticmethod
    def _img_prompt() -> str:
        return """Extract all text present in the image.

    Rules:
    - Preserve the content exactly (do not correct spelling).
    - Maintain reading order (top to bottom, left to right).
    - Include numbers, symbols and punctuation.
    - Return only the text, no additional explanations.

    - Respond in Portuguese (pt-BR).
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
