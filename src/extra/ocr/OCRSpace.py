# -*- coding: utf-8 -*-
""" original module taken and modified from https://github.com/ctoth/cloudOCR"""
from __future__ import unicode_literals
from builtins import object
import requests

translatable_langs = [_(u"Detect automatically"), _(u"Danish"), _(u"Dutch"), _(u"English"), _(u"Finnish"), _(u"French"), _(u"German"), _(u"Hungarian"), _(u"Korean"), _(u"Italian"), _(u"Japanese"), _(u"Polish"), _(u"Portuguese"), _(u"Russian"), _(u"Spanish"), _(u"Turkish")]
short_langs = ["", "da", "du", "en", "fi", "fr", "de", "hu", "ko", "it", "ja", "pl", "pt", "ru", "es", "tr"]
OcrLangs = ["", "dan", "dut", "eng", "fin", "fre", "ger", "hun", "kor", "ita", "jpn", "pol", "por", "rus", "spa", "tur"]

class APIError(Exception):
    pass

class OCRSpaceAPI(object):

    def __init__(self, key="4e72ae996f88957", url='https://api.ocr.space/parse/image'):
        self.key = key
        self.url = url

    def OCR_URL(self, url, overlay=False, lang=None):
        payload = {
            'url': url,
            'isOverlayRequired': overlay,
            'apikey': self.key,
        }
        if lang != None:
            payload.update(language=lang)
        r = requests.post(self.url, data=payload)
        result = r.json()['ParsedResults'][0]
        if result['ErrorMessage']:
            raise APIError(result['ErrorMessage'])
        return result

    def OCR_file(self, fileobj, overlay=False):
        payload = {
            'isOverlayRequired': overlay,
            'apikey': self.key,
            'lang': 'es',
        }
        r = requests.post(self.url, data=payload, files={'file': fileobj})
        results = r.json()['ParsedResults']
        if results[0]['ErrorMessage']:
            raise APIError(results[0]['ErrorMessage'])
        return results

