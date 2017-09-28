"""
Lab 4
Author: Jietong Chen
        Leilei Sun

This program read the message from file and encrypt/decrypt by specify sequence of transformations.
"""

import sys


def shift(msg, index, number=1):
    print("shift %d, %d" % (index, number))
    return msg


def rotate(msg, number=1):
    print("rotate %d" % number)
    return msg


def duplicate(msg, index, number=1):
    print("duplicate %d, %d" % (index, number))
    return msg


def swap(msg, index1, index2, group=1):
    print("swap ( %d ) %d, %d" % (group, index1, index2))
    return msg


def encrptyMsg(msg, trans):
    for i in range(len(trans)):
        if (trans[i][0] == 'S'):
            if (len(trans[i]) == 2):
                msg = shift(msg, trans[i][1])
            else:
                msg = shift(msg, trans[i][1], trans[i][2])

        elif (trans[i][0] == 'R'):
            if (len(trans[i]) == 1):
                msg = rotate(msg)
            else:
                msg = rotate(msg, trans[i][1])

        elif (trans[i][0] == 'D'):
            if (len(trans[i]) == 2):
                msg = duplicate(msg, trans[i][1])
            else:
                msg = duplicate(msg, trans[i][1], trans[i][2])

        elif (trans[i][0] == 'T'):
            if (len(trans[i]) == 3):
                msg = swap(msg, trans[i][1], trans[i][2])
            else:
                msg = swap(msg, trans[i][1], trans[i][2], trans[i][3])

    return msg


def initTransformation(trans):
    for i in range(len(trans)):
        trans[i] = trans[i].split(';')
        for k in range(len(trans[i])):
            op = [trans[i][k][0]]
            if (op[0] == 'S' or op[0] == 'D'):
                op += trans[i][k][1:].split(',')
                for t in range(1, len(op)):
                    op[t] = int(op[t])
            elif (op[0] == 'R'):
                if (len(trans[i][k]) > 1):
                    op += [int(trans[i][k][1:])]
            elif (op[0] == 'T'):
                if (trans[i][k][1] == '('):
                    index = trans[i][k].find(')')
                    op += trans[i][k][index + 1:].split(',')
                    op += [int(trans[i][k][2:index])]
                    for t in range(1, len(op)):
                        op[t] = int(op[t])
                else:
                    op += trans[i][k][1:].split(',')
                    for t in range(1, len(op)):
                        op[t] = int(op[t])

            trans[i][k] = op


def readFile(filename):
    lines = []

    try:
        file = open(filename)
    except FileExistsError as e:
        print(e)
    else:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].splitlines()[0]

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
    for m in message:
        print(m)

    print()

    print("transformation:")
    transformation = readFile(sys.argv[2])
    initTransformation(transformation)
    for a in transformation:
        print(a)

    print()

    for i in range(len(message)):
        message[i] = encrptyMsg(message[i], transformation[i])

    print("\nAfter encrypted:")
    for m in message:
        print(m)


if __name__ == '__main__':
    main()
