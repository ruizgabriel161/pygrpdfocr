from typing import overload

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Flowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer

from pygrocrimage.export.text_exporter_base import TextExporterBase


class PdfExporter(TextExporterBase):
    """
    Classe para salvar o pdf
    """

    @overload
    def export(self, text: str, output_path: str): ...

    @overload
    def export(self, text: list[str], output_path: str) -> None: ...

    def export(self, text: str | list[str], output_path: str) -> None:
        """
        export Método responsável por exportar em pdf

        Args:
            text (str): texto
            output_path (str): caminho de saída
        """

        pages = [text] if isinstance(text, str) else text
        story = self._build_story(pages)
        SimpleDocTemplate(output_path, pagesize=A4).build(story)

    def _build_story(self, pages: list[str]) -> list[Flowable]:
        styles = getSampleStyleSheet()
        story: list[Flowable] = []

        for i, page_text in enumerate(pages):
            for line in page_text.splitlines():
                if line.strip():
                    story.append(Paragraph(line, styles['Normal']))
                    story.append(Spacer(1, 6))

            if i < len(pages) - 1:
                story.append(PageBreak())

        return story
