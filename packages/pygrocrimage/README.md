#  pygrocrimage

## Descrição

Biblioteca para extração de texto de imagens utilizando OCR, com suporte a múltiplos engines:

-  OCR baseado em **LLM (multimodal)**
-  OCR tradicional com **Tesseract**

A arquitetura utiliza o padrão **Factory**, permitindo trocar facilmente o engine sem alterar o código cliente.

---

## Funcionalidades

- Extração de texto de imagens (`PIL.Image`)
- OCR com Tesseract
- OCR com modelos LLM (via LangChain)
- Processamento em lote
- Salvamento em `.txt`
- Arquitetura extensível

---

##  Arquitetura
```
OCRFactory
├── OCRTesseract
└── OCRImageLLM
```


- `OCRBase` → classe abstrata base
- `OCRFactory` → criação do engine
- `OCRTesseract` → OCR tradicional
- `OCRImageLLM` → OCR com LLM
- `LoadLLM` → carregamento de modelos

---

##  Exemplos de Uso

#### 1. OCR com Tesseract

```python
from pygrocrimage.ocr.factory_orc import OCRFactory

ocr = OCRFactory.create(
    engine="tesseract",
    lang="por"
)

text = ocr.extract_text(img=image)

print(text)
```
#### 2. OCR com LLM (multimodal)
```python
from pygrocrimage.ocr.factory_orc import OCRFactory

ocr = OCRFactory.create(
    engine="llm",
    llm="llava:7b",
    model_provider="ollama",
    endpoint="http://localhost:11434"
)

text = ocr.extract_text(b64=imagem_base64)

print(text)
```