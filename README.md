# Assistente de Estudos com Resumos de Vídeos do YouTube

Este projeto é um assistente de estudo que gera resumos em texto a partir de vídeos do YouTube. A ferramenta faz o download do vídeo, extrai o áudio, transcreve com o modelo Whisper e gera um resumo usando a API do DeepSeek. A interface é apresentada de forma simples e intuitiva com Streamlit.

## Como Funciona

1. Você fornece o link de um vídeo do YouTube.
2. O sistema baixa o vídeo usando pytubefix.
3. Extrai o áudio com moviepy.
4. Transcreve o áudio com o modelo Whisper.
5. Envia o texto transcrito para a API do DeepSeek para gerar um resumo.
6. Exibe o resumo na interface do usuário com Streamlit.

## Bibliotecas Utilizadas

- [Whisper](https://github.com/openai/whisper)
- [DeepSeek API](https://www.deepseek.ai/)
- os
- pytubefix
- moviepy
- requests e json
- streamlit

## Interface

Aqui está um exemplo de como a interface do projeto se parece:

![Interface do Projeto](C:\Users\joema\Downloads\img_interface.jpeg)
