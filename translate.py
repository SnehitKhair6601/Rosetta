#import json

import argparse
import six

""" Translates provided orig_text to target language string """
def translate(text, output_file, target = "en"):
    from google.cloud import translate_v2 as translate
    translate_client = translate.Client()
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    result = translate_client.translate(text, target_language = target)
    translated = format(result['translatedText'])

    file = open(output_file, "a")
    file.write(translated)
    file.close()

    return translated


