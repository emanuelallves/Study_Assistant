import os
import requests
import json

def get_api_key():
    API_Key_path = './API_Key.txt'

    with open(API_Key_path, 'r', encoding='utf-8') as f:
        API_Key = f.read().strip()
    
    return API_Key

def write(text, output_path='./content', file_name='summary'):
    summary_path = os.path.join(output_path, file_name + '.txt')
    os.makedirs(output_path, exist_ok=True)
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(text)

def clean_text(text):
    if text.startswith(r'\boxed{') and text.endswith('}'):
        text = text[8:-1]

    if text.startswith(r'``text'):
        text = text[7:]

    return text

def resumir(text):
    print('Resumindo o texto...')
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {get_api_key()}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "deepseek/deepseek-r1-zero:free",
            "messages": [
                {
                    "role": "system",
                    "content": "Você é um assistente útil que resume textos de forma clara e concisa."
                },
                {
                    "role": "user",
                    "content": f"Por favor, faça um resumo conciso e objetivo do texto a seguir. Inclua apenas as informações principais, mantendo a clareza e a fidelidade ao conteúdo original. Se o texto for muito longo, você pode dividir o resumo em tópicos ou parágrafos curtos. Destaque eventuais dados importantes, como números, nomes relevantes ou conclusões significativas. Formate a resposta em português brasileiro.:\n\n{text}"
                }
            ]
        })
    )

    if response.status_code == 200:
        summary_text = response.json()['choices'][0]['message']['content']
        summary_text = clean_text(summary_text)
        print('Salvando resumo...')
        write(summary_text)
        print('Resumo salvo!')
        return summary_text
    else:
        print(f"Erro na API: {response.status_code} - {response.text}")
        return None