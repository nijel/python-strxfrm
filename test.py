#!/usr/bin/env python

import locale

words = ('zkouška', 'zkouzka', 'zkouaka', 'Français', '中文')

def test():
    for word in words:
        try:
            print(f"strxfrm({word!r}) = {locale.strxfrm(word)!r}")
        except OSError as error:
            print(f"strxfrm({word!r}) failed with {error}")
    print()

print("no locale")
test()

print("C.UTF-8")
locale.setlocale(locale.LC_ALL, ("C", "UTF-8"))
test()


print("en_US.UTF-8")
locale.setlocale(locale.LC_ALL, ("en_US", "UTF-8"))
test()

print("C.UTF-8")
locale.setlocale(locale.LC_ALL, ("C", "UTF-8"))
test()

print("en_US")
locale.setlocale(locale.LC_ALL, ("en_US", "UTF-8"))
test()
