#!/usr/bin/env python

import locale

def test():
    for word in ('zkouška', 'zkouzka', 'zkouaka'):
        print(f"strxfrm({word!r}) = {locale.strxfrm(word)!r}")
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

