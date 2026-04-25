from pathlib import Path
from typing import Literal

from PIL.Image import Image as Image

class PDFToImage:
    def __init__(self) -> None: ...
    def convert(self, pdf_path: Path, **kwargs) -> list[Image]: ...
    def convert_to_save(
        self,
        pdf_path: Path,
        output_dir: Path,
        output_suffix: str = 'page',
        fmt: Literal['PNG', 'JPEG'] = 'PNG',
        **kwargs,
    ) -> list[Path]: ...
    def resize_if_needed(self, img: Image, max_px: int = 2048) -> Image: ...
    def pil_to_base64(
        self, img: Image, fmt: Literal['PNG', 'JPEG'] = 'PNG', encoding: str = 'utf-8'
    ) -> str: ...
