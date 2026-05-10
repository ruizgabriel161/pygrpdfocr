from pathlib import Path
from typing import List

from PIL.Image import Image

from pygrpdfimage.interface import PDFReader
from pygrpdfimage.reader import PDF2ImageReader
from pygrpdfimage.resizer import ImageResizer
from pygrpdfimage.saved import ImageSaver
from pygrpdfimage.serialize import ImageSerializer


class PDFService:
    def __init__(self) -> None:
        self._reader: PDFReader = PDF2ImageReader()
        self.saver = ImageSaver()
        self.resizer = ImageResizer()
        self.serializer = ImageSerializer()

    @property
    def reader(self) -> PDFReader:
        return self._reader

    @reader.setter
    def reader(self, value: PDFReader) -> None:
        self._reader = value

    def pdf_to_images(self, pdf_path: Path) -> List[Image]:
        return self.reader.convert(pdf_path)

    def pdf_to_files(self, pdf_path: Path, output_dir: Path, fmt: str = 'PNG'):
        images = self.reader.convert(pdf_path)

        if self.resizer:
            images = [self.resizer.resize_if_needed(img) for img in images]

        if not self.saver:
            raise ValueError('Saver não foi fornecido')

        return self.saver.save(
            images=images, output_dir=output_dir, base_name=pdf_path.stem, fmt=fmt
        )

    def pdf_to_base64(self, pdf_path: Path, fmt: str = 'PNG'):
        images = self.reader.convert(pdf_path)

        if self.resizer:
            images = [self.resizer.resize_if_needed(img) for img in images]

        if not self.serializer:
            raise ValueError('Serializer não foi fornecido')

        return [self.serializer.to_base64(img, fmt) for img in images]
