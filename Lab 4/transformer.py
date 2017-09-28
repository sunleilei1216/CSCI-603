"""
Lab 4
Author: Jietong Chen
        Leilei Sun

This program read the message from file and encrypt/decrypt by specify sequence of transformations.
"""

import sys


def shift(msg, index, number=1):
    """
    Shift the letter at index forward in alphabet order with number.

    :param msg:    the message needed to transform
    :param index:    index of the letter
    :param number:     number of forward step, default as 1
    :return:    message after transformation
    """
    print("shift %d, %d" % (index, number))
    return msg


def rotate(msg, number=1):
    """
    Rotate the string with number position to right.

    :param msg:    the message needed to transform
    :param number:     number of rotate step, default as 1
    :return:    message after transformation
    """
    print("rotate %d" % number)
    return msg


def duplicate(msg, index, number=1):
    """
    Duplicate the letter at index with number times.

    :param msg:    the message needed to transform
    :param index:    index of the letter
    :param number:     number of duplicate times, default as 1
    :return:    message after transformation
    """
    print("duplicate %d, %d" % (index, number))
    return msg


def swap(msg, index1, index2, group=1):
    """
    Swap two letters at index1 and index2. If group specified, divide the string into group with equal size, swap two
    group of letters at index1 and index2.

    :param msg:    the message needed to transform
    :param index1:    index of the first letter
    :param index2:    index of the second letter
    :param group:    number of group, default as 1
    :return:    message after transformation
    """
    print("swap ( %d ) %d, %d" % (group, index1, index2))
    return msg


def encryptMsg(msg, trans):
    """
    Encrypt the message with given transformation by calling corresponding transformation function.

    :param msg:    the message needed to encrypt
    :param trans:    the list of transformation
    :return:    string after encrypt
    """
    for i in range(len(trans)):
        # transformation is shift
        if (trans[i][0] == 'S'):
            if (len(trans[i]) == 2):
                msg = shift(msg, trans[i][1])
            else:
                msg = shift(msg, trans[i][1], trans[i][2])
        # transformation is rotate
        elif (trans[i][0] == 'R'):
            if (len(trans[i]) == 1):
                msg = rotate(msg)
            else:
                msg = rotate(msg, trans[i][1])
        # transformation is duplicate
        elif (trans[i][0] == 'D'):
            if (len(trans[i]) == 2):
                msg = duplicate(msg, trans[i][1])
            else:
                msg = duplicate(msg, trans[i][1], trans[i][2])
        # transformation is swap
        elif (trans[i][0] == 'T'):
            if (len(trans[i]) == 3):
                msg = swap(msg, trans[i][1], trans[i][2])
            else:
                msg = swap(msg, trans[i][1], trans[i][2], trans[i][3])

    return msg


def decryptMsg(msg, trans):
    """
    Decrypt the message with given transformation by calling corresponding transformation function.

    :param msg:    the message needed to decrypt
    :param trans:    the list of transformation
    :return:    string after decrypt
    """
    for i in range(len(trans) -1, -1, -1):
        # transformation is shift
        if (trans[i][0] == 'S'):
            if (len(trans[i]) == 2):
                msg = shift(msg, trans[i][1], -1)
            else:
                msg = shift(msg, trans[i][1], -trans[i][2])
        # transformation is rotate
        elif (trans[i][0] == 'R'):
            if (len(trans[i]) == 1):
                msg = rotate(msg, -1)
            else:
                msg = rotate(msg, -trans[i][1])
        # transformation is duplicate
        elif (trans[i][0] == 'D'):
            if (len(trans[i]) == 2):
                msg = duplicate(msg, trans[i][1])
            else:
                msg = duplicate(msg, trans[i][1], trans[i][2])
        # transformation is swap
        elif (trans[i][0] == 'T'):
            if (len(trans[i]) == 3):
                msg = swap(msg, trans[i][1], trans[i][2])
            else:
                msg = swap(msg, trans[i][1], trans[i][2], trans[i][3])

    return msg


def isEncrypt():
    """
    Determine whether encrypt or decrypt the message with given transformation.

    :return:    True if encrypt the message, False if not
    """
    while (True):
        ch = input("Do you want to encrypt the message or decrypt it? (e/d)\n> ")
        if (ch == 'e' or ch == 'E'):
            return True
        elif (ch == 'd' or ch == 'D'):
            return False
        else:
            print("The input should be d or e!")


def init(trans):
    """
    Initialize the transformations list. Convert the transformation string into a list, where first character indicate
    the transform type, following integers as the arguments of transformation.

    :param trans:    list of transformation
    """
    for i in range(len(trans)):
        # split the line containing a sequence of operations by semicolon
        trans[i] = trans[i].split(';')

        for k in range(len(trans[i])):
            # first character of the string represent type of the transformation
            op = [trans[i][k][0]]

            # in the case of shift and duplicate, there will be one or two parameter
            if (op[0] == 'S' or op[0] == 'D'):
                op += trans[i][k][1:].split(',')
                # convert string into integer
                for t in range(1, len(op)):
                    op[t] = int(op[t])

            # in the case of rotate, there will be no or one parameter
            elif (op[0] == 'R'):
                if (len(trans[i][k]) > 1):
                    op += [int(trans[i][k][1:])]
            # in the case of swap, there will be two or three parameters
            elif (op[0] == 'T'):
                # contain the 'group' parameter
                if (trans[i][k][1] == '('):
                    # position of the right parenthesis
                    index = trans[i][k].find(')')
                    # get the last two parameters
                    op += trans[i][k][index + 1:].split(',')
                    # the third parameter
                    op += [int(trans[i][k][2:index])]
                    # convert strings into integers
                    for t in range(1, len(op)):
                        op[t] = int(op[t])
                else:
                    op += trans[i][k][1:].split(',')
                    # convert strings into integers
                    for t in range(1, len(op)):
                        op[t] = int(op[t])

            trans[i][k] = op


def readFile(filename):
    """
    Read a file from disk, return the content of the file

    :param filename:    the name of the file
    :return:    a list contain each lines of the file
    """
    lines = []  # list of lines

    try:
        file = open(filename)
    except FileExistsError as e:
        print(e)
    else:
        lines = file.readlines()
        # remove the line feed symbol behind the content
        for i in range(len(lines)):
            lines[i] = lines[i].splitlines()[0]
            # convert to uppercase if the string contain not uppercase letter
            if (not lines[i].isupper()):
                lines[i] = lines[i].upper()

        file.close()

    return lines


def main():
    """
    The main function of the progran.
    """
    # missing filename in commandline input
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
    transform = readFile(sys.argv[2])
    init(transform)
    for a in transform:
        print(a)

    print()

    encrypt = isEncrypt()
    if (encrypt):
        print("Encrypt it...")
    else:
        print("Decrypt it...")

    print()

    for i in range(len(message)):
        if (encrypt):
            print(encryptMsg(message[i], transform[i]))
        else:
            print(decryptMsg(message[i], transform[i]))
        print()


if __name__ == '__main__':
    main()
