'''
This module provides functions for translating text using the libretranslate API.
'''
import requests
def translate_text(text):
    '''
    Translate the given text to English using the libretranslate API.
    Args:
        text (str): The text to be translated.
    Returns:
        str: The translated text.
    '''
    url = 'https://libretranslate.com/translate'
    payload = {
        'q': text,
        'source': 'auto',
        'target': 'en'
    }
    response = requests.post(url, json=payload)
    translated_text = response.json()['translatedText']
    return translated_text