#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

"""
Напишите программу, которая будет считывать список слов из
файла и собирать статистику о том, в каком проценте слов используется каждая буква
алфавита.

"""

if __name__ == "__main__":
    with open("ind2.txt", "r", encoding="utf-8") as txt:
        content = txt.readline().lower().replace(" ", "").replace(".", "")

    A = []
    for i in string.ascii_lowercase:
        k = 0
        for j in content:
            if i == j:
                k = k + 1
        if k > 0:
            s1 = i + ' ' + ("%1.2f" % (k / (len(content) - 1)))
            s2 = s1.split(' ')
            A.append(s2)
    A.sort(key=lambda n: n[1], reverse=True)
    B = "\n".join([i[0] + " " + i[1] for i in A])
    print(B)
