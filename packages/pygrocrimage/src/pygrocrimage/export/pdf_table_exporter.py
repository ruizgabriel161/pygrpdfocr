import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from pygrocrimage.export.table_exporter_base import TableExporterBase


class PdfTableExporter(TableExporterBase):
    def export(self, df: pd.DataFrame, output_path: str) -> None:

        doc = SimpleDocTemplate(output_path, pagesize=landscape(A4))
        data = [df.columns.tolist()] + df.values.tolist()
        table = Table(data)
        table.setStyle(
            TableStyle(
                [
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    (
                        'ROWBACKGROUNDS',
                        (0, 1),
                        (-1, -1),
                        [colors.white, colors.lightgrey],
                    ),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ]
            )
        )
        doc.build([table])
