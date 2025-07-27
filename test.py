#!/usr/bin/env python

import pytest
import locale
import platform
from weblate_language_data.languages import LANGUAGES

WORDS = ('zkouška', 'zkouzka', 'zkouaka', 'Français', '中文', 'š')
LOCALES = (None, "en_US.UTF-8")

FIXTURE = [(locale_name, word) for locale_name in LOCALES for word in WORDS]

@pytest.mark.parametrize("locale_name,word", FIXTURE)
def test(locale_name, word):
    locale.setlocale(locale.LC_ALL, locale_name)
    print(f"strxfrm({word!r}) = {locale.strxfrm(word)!r}")

def test_languages():
    locale.setlocale(locale.LC_ALL, ("en_US", "UTF-8"))
    sorted(LANGUAGES, key=lambda x: locale.strxfrm(x[1]))
