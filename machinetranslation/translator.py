"""
Translator program from englis to frence and vice versa
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

"""function to translate from english to french"""
def english_to_french(english_text):
    translation = language_translator.translate(
    text= english_text,
    model_id='en-fr').get_result()

    t_trns = {}

    t_trns = translation["translations"]
    french_text = t_trns[0]['translation']
    return french_text

"""function to translate from french to english"""
def french_to_english(french_text):
    translation = language_translator.translate(
    text= french_text,
    model_id='fr-en').get_result()

    t_trns = {}

    t_trns = translation["translations"]
    english_text = t_trns[0]['translation']
    return english_text

load_dotenv()


apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-08-07',
    authenticator=authenticator
)

language_translator.set_service_url(url)
