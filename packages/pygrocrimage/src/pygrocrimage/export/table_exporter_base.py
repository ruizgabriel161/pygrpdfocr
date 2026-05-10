from abc import ABC

import pandas as pd


class TableExporterBase(ABC):
    """
    Classe abstrata para exportar tables
    """

    def export(self, df: pd.DataFrame, output_path: str): ...
