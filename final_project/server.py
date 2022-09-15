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
    text = translator.english_to_french(request.args.get('textToTranslate'))
    if text is None:
        return "Please supply a valid text string to translate"
    else:
        return text

@app.route("/frenchToEnglish")
def french_to_english():
    """
    Accept request and return translated text
    """
    text = translator.french_to_english(request.args.get('textToTranslate'))
    if text is None:
        return "Please supply a valid text string to translate"
    else:
        return text

@app.route("/")
def render_index_page():
    """
    Accept request and return index page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
