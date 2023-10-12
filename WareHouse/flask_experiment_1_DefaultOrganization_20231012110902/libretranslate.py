import requests
def translate_text(text):
    url = 'https://libretranslate.com/translate'
    payload = {
        'q': text,
        'source': 'auto',
        'target': 'en'
    }
    response = requests.post(url, json=payload)
    translated_text = response.json()['translatedText']
    return translated_text