"""
Server file for mapping browser requests to translations
"""
from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """
    Accept request and return translated text
    """
    return translator.english_to_french(request.args.get('textToTranslate'))

@app.route("/frenchToEnglish")
def french_to_english():
    """
    Accept request and return translated text
    """
    return translator.french_to_english(request.args.get('textToTranslate'))

@app.route("/")
def render_index_page():
    """
    Accept request and return index page
    """
    return render_template("static/index.html", title='Translation')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
