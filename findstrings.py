#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import xml.etree.cElementTree as ET

destStringRes = ["values",
                 "values-ar",
                 "values-de",
                 "values-es",
                 "values-fr",
                 "values-in",
                 "values-ja",
                 "values-ko",
                 "values-pt",
                 "values-ru",
                 "values-th",
                 "values-tr",
                 "values-vi",
                 "values-zh",
                 "values-zh-rHK"
                 ]

stringKeys = {
    'item_text_notification_icon': 'item_text_notification_icon',
}


def get_dest_files_path():
    path_list = []
    for (root, dirs, files) in os.walk("."):
        for dirName in dirs:
            if dirName in destStringRes:
                parent_dir = os.path.join(root, dirName)
                path_list.append(os.path.join(parent_dir, "strings.xml"))
    return path_list


def get_strings():
    path_list = get_dest_files_path()
    for path in path_list:
        print "****" + path + "****"
        tree = ET.ElementTree(file=path)
        for elem in tree.iter(tag='string'):
            if elem.attrib['name'] in stringKeys.keys():
                key = stringKeys.get(elem.attrib['name'])
                print '<string name="' + key + '">' + elem.text + '</string>'
        print "****" + path + "****"


if __name__ == "__main__":
    get_strings()
