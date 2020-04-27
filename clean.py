#!/usr/bin/python
# -*- coding: utf-8 -*-
import getopt
import os

import sys


def clean(argv):
    try:
        opts, args = getopt.getopt(argv, "s:")
    except getopt.GetoptError:
        print("error***error***error")
    print ("these files will be deleted")
    deleted_files = []
    for opt, arg in opts:
        if opt == "-s":
            suffix = arg
            if suffix:
                for root, dirs, files in os.walk('./'):
                    for name in files:
                        if name.endswith(suffix):
                            print (name)
                            deleted_files.append(os.path.join(root, name))
    # operation = raw_input("Are you sure? Y/N: ") pyton2
    operation = raw_input("Are you sure? Y/N: ")
    if operation == "Y":
        print ("start delete>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        for file_to_be_deleted in deleted_files:
            os.remove(file_to_be_deleted)
            print(file_to_be_deleted + "was deleted")
        print ("\ndelete over>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


if __name__ == "__main__":
    clean(sys.argv[1:])
