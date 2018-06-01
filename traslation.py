#!/usr/bin/python
# -*- coding: utf-8 -*-
from googletrans import Translator


def translate(content, dest_language, src_language):
    translator = Translator()
    translation = translator.translate(content, dest=dest_language, src=src_language)
    return translation.text


dest_language = {
    "ja": "ja", "ar": "ar", "de": "de",
    "es": "es", "fr": "fr", "ko": "ko",
    "pl": "pl", "pt": "pt", "ru": "ru",
    "th": "th", "in": "id", "tr": "tr",
    "vi": "vi"
}
ready_to_translate = {
    "toast_unprotect_succeed": "Cancel to lock this app succeed"
}
for k, v in dest_language.items():
    print(k + "------" + k)
    for t_k, t_v in ready_to_translate.items():
        print '<string name="' + t_k + '">' + translate(t_v, v, "en") + '</string>'
    print(k + "------" + k + "\n")
