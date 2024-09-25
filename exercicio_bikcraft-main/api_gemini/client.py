import google.generativeai as genai
import os

def client_gemini(modelo):
    genai.configure(api_key=os.environ['API_KEY'])

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content('Write a story about a magic backpack')
    print(response.text)