from abc import ABC, abstractmethod

import pandas as pd
from PIL.Image import Image


class TableExtractorBase(ABC):
    @abstractmethod
    def extract_table(self, img: Image) -> pd.DataFrame: ...

    @abstractmethod
    def extract_table_batch(self, images: list[Image]) -> list[pd.DataFrame]: ...
