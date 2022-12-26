#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает текст из файла и выводит на экран только
предложения, начинающиеся с тире, перед которым могут находиться только пробельные
символы.
"""


if __name__ == "__main__":
    with open("ind1.txt", "r", encoding="utf-8") as txt:
        content = txt.read().split(".")

    for line in content:
        if ' -' in line:
            print(line.strip())
