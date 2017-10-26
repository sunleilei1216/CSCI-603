"""
GeneTester.py

Testing program of the DNAList. The tester test every functions of the list,
to determine whether the data structure implement correctly.

Author: Jietong Chen
        Leilei Sun
"""

from DNAList import *


def main():
    """
    The main function doing testing.
    """
    # test of __init__(self, gene='')
    list1 = DNAList()
    print("list1 = DNAList()\n%s" % list1)

    list2 = DNAList("ACT")
    print("list2 = DNAList(\"ACT\")\n%s" % list2)

    # test of append(self, item)
    print("\n----append----\n")

    list1.append('A')
    print("list1.append(\'A\')\n%s" % list1)
    list1.append('G')
    print("list1.append(\'G\')\n%s" % list1)

    # test of join(self, other)
    print("\n----join----\n")

    list1.join(DNAList())
    print("list1.join(DNAList())\n%s" % list1)
    list1.join(DNAList("CCAT"))
    print("list1.join(DNAList(\"CCAT\"))\n%s" % list1)

    # test of splice(self, ind, other)
    print("\n----splice----\n")

    list1.splice(3, DNAList("TAT"))
    print("list1.splice(3, DNAList(\"TAT\"))\n%s" % list1)
    list1.splice(-1, DNAList("GTA"))
    print("list1.splice(-1, DNAList(\"GTA\"))\n%s" % list1)

    # test of snip(self, i1, i2)
    print("\n----snip----\n")

    list1.snip(0, 2)
    print("list1.snip(0, 2)\n%s" % list1)
    list1.snip(1, 4)
    print("list1.snip(1, 4)\n%s" % list1)
    list1.snip(5, 2)
    print("list1.snip(5, 2)\n%s" % list1)
    list1.snip(-1, 4)
    print("list1.snip(-1, 4)\n%s" % list1)

    # test of replace(self, repstr, other)
    print("\n----replace----\n")

    list1.replace("CAT", DNAList("TG"))
    print("list1.replace(\"CAT\", DNAList(\"TG\"))\n%s" % list1)
    list1.replace("Not exist string", DNAList("TAG"))
    print("list1.replace(\"Not exist string\", DNAList(\"TAG\"))\n%s" % list1)
    list1.replace("C", DNAList())
    print("list1.replace(\"C\", DNAList())\n%s" % list1)

    # test of copy(self)
    print("\n----copy----\n")

    list3 = list1.copy()
    print("list3 = list1.copy()\n%s" % list3)


if __name__ == '__main__':
    main()
