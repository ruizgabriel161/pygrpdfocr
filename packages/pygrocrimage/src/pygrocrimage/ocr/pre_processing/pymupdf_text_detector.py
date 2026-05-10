from typing import cast, override

import fitz

from pygrocrimage.ocr.pre_processing.pdf_text_detector import PDFTextDetector


class PyMuPDFTextDetector(PDFTextDetector):
    @override
    def has_text(self, pdf_path: str) -> bool:
        """
        has_text Metodo responsável por verificar se existe texto vetorial

        Args:
            pdf_path (str): caminho do pdf

        Returns:
            bool: retorna true se existe vetor ou false se não existe
        """
        with fitz.open(pdf_path) as doc:
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)

                text = cast(str, page.get_text())

                if text.strip():
                    return True

        return False

    @override
    def extract_text(self, pdf_path: str) -> str:
        """
        extract_text Método responsável por extrair o texto caso exista o vetor

        Args:
            pdf_path (str): caminho do pdf

        Returns:
            str: texto retornado
        """
        doc = fitz.open(pdf_path)

        texts: list[str] = []

        for page in doc:
            texts.append(str(page.get_text()))

        return '\n'.join(texts)
