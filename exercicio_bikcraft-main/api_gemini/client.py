import google.generativeai as genai
import os

def client_gemini(modelo):
    genai.configure(api_key=os.environ['API_KEY'])

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f'Crie uma descrição em um linha do modelo de biciclieta {modelo}')
    return response.text