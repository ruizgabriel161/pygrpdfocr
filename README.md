# Monorepo criado para fazer ocr em pdf

## Autor: Gabriel Lopes Ruiz

### Projeto está em desenvolvimento e tem como objetivo trabalhar com PDF


📄 PyGr PDF OCR

Projeto para conversão de PDFs em imagem e extração de texto via OCR, utilizando uma arquitetura modular baseada em pacotes.

🚀 Visão Geral

Este projeto realiza:

Conversão de arquivos PDF em imagens
Extração de texto das imagens via OCR
Salvamento do texto extraído em arquivo .txt

A estrutura foi pensada para ser extensível, permitindo troca de engines de OCR e futuras integrações com modelos LLM.

🧱 Arquitetura

O projeto está dividido em dois pacotes principais:

📦 pygrpdfimage

Responsável pela manipulação de PDFs:

Conversão de PDF → imagem
Utiliza a classe:
PDFToImage
📦 pygrocrimage

Responsável pelo OCR:

Criação de engines de OCR via Factory
Extração de texto de imagens
Utiliza:
OCRFactory