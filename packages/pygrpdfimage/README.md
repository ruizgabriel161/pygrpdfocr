# pygrpdfimage
## Autor: Gabriel Lopes Ruiz

Biblioteca responsável pela conversão de arquivos PDF em imagens.

Permite transformar páginas de um PDF em objetos de imagem (PIL.Image), facilitando o processamento posterior (como OCR).

---
### **Funcionalidades**

- Conversão de PDF → lista de imagens

- Suporte a múltiplas páginas

- Preparação para integração com pipelines de OCR

---
### Exemplos de Uso: 
---
#### 1. Extrair o pdf:
 
```python
from pathlib import Path
from pygrpdfimage.pdf_to_image import PDFToImage

pdf_to_image = PDFToImage()

images = pdf_to_image.convert(
    pdf_path=Path("docs/pdf/arquivo.pdf")
)

# Acessar primeira página
first_page = images[0]

# Última página
last_page = images[-1]

```
---
#### 2. Converter e salvar a imagem

```python
from pathlib import Path

output_files = pdf.convert_to_save(
    pdf_path=Path("docs/pdf/arquivo.pdf"),
    output_dir=Path("docs/img"),
    fmt="PNG"
)

for file in output_files:
    print(file)

```

---

#### 3. Redimensionar imagem

```python
images = pdf.convert(Path("docs/pdf/arquivo.pdf"))

resized_images = [
    pdf.resize_if_needed(img, max_px=1024)
    for img in images
]

```

---

#### 4. Converter imagem para base64 (Integração com LLM)

```python
images = pdf.convert(Path("docs/pdf/arquivo.pdf"))

b64_list = [
    pdf.pil_to_base64(img)
    for img in images
]

print(b64_list[0][:100])  # preview

```
