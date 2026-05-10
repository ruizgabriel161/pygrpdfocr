from typing import override

from cv2 import (
    COLOR_BGR2GRAY,
    COLOR_RGB2BGR,
    INTER_CUBIC,
    THRESH_BINARY,
    THRESH_OTSU,
    cvtColor,
    fastNlMeansDenoising,
    resize,
    threshold,
)
from numpy import array
from PIL.Image import Image, fromarray

from pygrocrimage.ocr.pre_processing.image_pre_processor import ImagePreprocessor


class OpenCVPreprocessor(ImagePreprocessor):
    @override
    def process(self, img: Image) -> Image:
        np_img = array(img)

        # RGB -> BGR
        np_img = cvtColor(np_img, COLOR_RGB2BGR)

        # grayscale
        gray = cvtColor(np_img, COLOR_BGR2GRAY)

        # upscale
        gray = resize(
            gray,
            None,
            fx=2,
            fy=2,
            interpolation=INTER_CUBIC,
        )

        # denoise
        gray = fastNlMeansDenoising(gray)

        # threshold
        thresh = threshold(
            gray,
            0,
            255,
            THRESH_BINARY + THRESH_OTSU,
        )[1]

        return fromarray(thresh)
