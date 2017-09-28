"""
Lab 4
Author: Jietong Chen

This program read the message from file and encrypt/decrypt by specify sequence of transformations.
"""

import sys


def initTransformation(trans):
    for i in range(len(trans)):
        trans[i] = trans[i].split(';')

    return trans


def readFile(filename):
    lines = []

    try:
        file = open(filename)
    except FileExistsError as e:
        print(e)
    else:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")

        file.close()

    return lines


def main():
    if (len(sys.argv) < 3):
        print("Missing file name!\n"
              + "Run the program like:\n"
              + "$ python3 transformer.py #_messageFileName #_transformationFileName\n"
              + "  #_messageFileName: the file name of message needed to encrypt/decrypt\n"
              + "  #_transformationFileName: the file name of transformation sequence")

        sys.exit(1)

    print("message:")
    message = readFile(sys.argv[1])
    print(message)

    print("transformation:")
    transformation = readFile(sys.argv[2])
    initTransformation(transformation)
    print(transformation)


if __name__ == '__main__':
    main()
