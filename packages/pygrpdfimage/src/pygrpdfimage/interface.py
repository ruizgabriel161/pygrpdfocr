from pathlib import Path
from typing import List, Protocol

from PIL.Image import Image


class PDFReader(Protocol):
    def convert(self, pdf_path: Path) -> List[Image]: ...
