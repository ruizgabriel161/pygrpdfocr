from docx import Document

from pygrocrimage.export.text_exporter_base import TextExporterBase


class WordTextExporter(TextExporterBase):
    def export(self, text: str, output_path: str) -> None:

        doc = Document()
        for line in text.splitlines():
            doc.add_paragraph(line)
        doc.save(output_path)
