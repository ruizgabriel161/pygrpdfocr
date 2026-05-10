from pathlib import Path

from pygrocrimage.export.text_exporter_base import TextExporterBase


class TxtExporter(TextExporterBase):
    def export(self, text: str, output_path: str) -> None:
        """
        export Método para exportar em text

        Args:
            text (str): _description_
            output_path (str): _description_
        """
        Path(output_path).write_text(text, encoding='utf-8')
