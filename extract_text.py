import whisper
import os
from pytubefix import YouTube
from moviepy import AudioFileClip

def baixar_e_converter_audio(url, output_path='./content', file_name='downloaded_video_audio'):
    os.makedirs(output_path, exist_ok=True)

    print("Baixando áudio do YouTube...")
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    webm_path = os.path.join(output_path, file_name + '.webm')
    audio.download(output_path=output_path, filename=file_name + '.webm')

    print("Convertendo para MP3...")
    mp3_path = os.path.join(output_path, file_name + '.mp3')
    clip = AudioFileClip(webm_path)
    clip.write_audiofile(mp3_path)
    clip.close()

    print("Removendo arquivo temporário (.webm)...")
    os.remove(webm_path)
    print("Arquivo MP3 salvo em:", mp3_path)

    return mp3_path

def write(text, output_path='./content', file_name='video_text'):
    txt_path = os.path.join(output_path, file_name + '.txt')
    
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

def transcrever_audio(input):
    audio_path = os.path.join(input)

    print("Transcrevendo o audio...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    write(result['text'])
    print('Audio transcrito')
    return result['text']