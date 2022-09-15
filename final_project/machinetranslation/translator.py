"""
Access to the IBM Language Translator and Translation Functions
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ["version"]

ENGLISH_TO_FRENCH = 'en-fr'
FRENCH_TO_ENGLISH = 'fr-en'


def get_translator():
    """
    Get an instance of the IBM Language Translator
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version={version},
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator


def translate_text(text_to_translate, locale, translator=get_translator()):
    """
    Calls the translate function from the translator
    """
    if text_to_translate == "" or text_to_translate is None:
        return None
    try:
        translations = translator.translate(
            text=text_to_translate,
            model_id=locale).get_result()

        translated_text = None
        if (translations.get("translations") and
                translations.get("translations")[0].get("translation")):
            translated_text = translations.get("translations")[
                0].get("translation")

        # print("\nLocale [" + locale + "] - Orig Text [" +
        # textToTranslate + "] - Translated Text [" + translatedText + "]")
        return translated_text
    except ApiException as ex:
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)
        return None


def english_to_french(english_text):
    """
    Translate english text to french
    """
    return translate_text(english_text, ENGLISH_TO_FRENCH)


def french_to_english(french_text):
    """
    Translate french text to english
    """
    return translate_text(french_text, FRENCH_TO_ENGLISH)
