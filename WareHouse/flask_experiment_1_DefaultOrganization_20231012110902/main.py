'''
Create a web application that uses python and Flask to query the libretranslate github project to translate text to english. The front-end must also have a field to accept files to translate. Include tests that are made with pytest.
'''
from flask import Flask, request, jsonify
from libretranslate import translate_text
app = Flask(__name__)
@app.route('/')
def index():
    return 'Translate Text'
@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text')
    translated_text = translate_text(text)
    return jsonify({'translated_text': translated_text})
if __name__ == '__main__':
    app.run()