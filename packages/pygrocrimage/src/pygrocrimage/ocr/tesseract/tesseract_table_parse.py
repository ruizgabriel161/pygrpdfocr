import pandas as pd


class TesseractTableParser:
    """Reconstrói DataFrame a partir dos dados brutos do Tesseract."""

    def __init__(self, row_tolerance: int = 10) -> None:
        self.row_tolerance = row_tolerance

    def parse(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        parse Método responsável por fazer o parse da tabela extraida

        Args:
            data (pd.DataFrame): tabela em pandas

        Returns:
            pd.DataFrame: retorna a tabela tratada
        """
        data = data[data['conf'] > 0].dropna(subset=['text'])
        data = data[data['text'].str.strip() != '']

        if data.empty:
            return pd.DataFrame()

        data = data.sort_values('top')
        data['row'] = (data['top'] / self.row_tolerance).astype(int)

        rows = (
            data.groupby('row')
            .apply(lambda g: g.sort_values('left')['text'].tolist())
            .tolist()
        )

        n_cols = max(len(r) for r in rows)
        rows = [r + [''] * (n_cols - len(r)) for r in rows]

        return pd.DataFrame(rows)
