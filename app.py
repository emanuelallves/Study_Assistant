import streamlit as st
import extract_text as et
import generate_summaries as gs
import os

st.set_page_config(
    page_title="Resumidor de Vídeos do YouTube",
    layout="centered"
)

st.title("Transcrição e resumo de vídeo")
st.markdown("""
Esta aplicação extrai o áudio de um vídeo do YouTube, transcreve o conteúdo e gera um resumo.
""")

url = st.text_input("Cole a URL do vídeo do YouTube aqui:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Gerar Resumo"):
    if not url:
        st.warning("Por favor, insira uma URL válida do YouTube.")
    else:
        with st.spinner("Processando o vídeo. Isso pode levar alguns minutos..."):
            try:
                audio_path = et.baixar_e_converter_audio(url)
                
                et.transcrever_audio(audio_path)
                
                file_path = './content/video_text.txt'
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    txt = f.read()
                
                summary = gs.resumir(txt)
                
                st.success("Processamento concluído!")
                
                st.subheader("Resumo do Vídeo")
                st.markdown(summary, unsafe_allow_html=True)
                
                with st.expander("Ver transcrição completa"):
                    st.text(txt)
                
                if os.path.exists(audio_path):
                    os.remove(audio_path)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    
            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")
                st.error("Verifique se a URL é válida e se o vídeo tem áudio para transcrição.")

st.markdown("---")