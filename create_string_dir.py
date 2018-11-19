#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def mkdir(path):
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path.decode('utf-8'))

    else:
        print("Dir already exists, path: " + path)


def create_string_dirs():
    dest_dirs = [
        "values",
        "values-ar",
        "values-de",
        "values-es",
        "values-fr",
        "values-in",
        "values-ja",
        "values-ko",
        "values-pl",
        "values-pt",
        "values-ru",
        "values-th",
        "values-tr",
        "values-vi",
    ]
    for string_dir in dest_dirs:
        folder = os.getcwd() + '\\' + string_dir
        mkdir(folder)
        string_file = folder + "\\strings.xml"
        empty_string_file = open(string_file, "w")
        empty_string_file.close()
        print("Create file succeed,path: " + string_file)


if __name__ == "__main__":
    create_string_dirs()
