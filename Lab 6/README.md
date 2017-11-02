# Lab 6
![Lab6](https://i.imgur.com/cAnkB56.jpg)

In this lab, we are consider the operation of gene splicing, snipping and joining. Specifically, we will represent a strand of DNA as a linked list. Each node in the list represents one nucleotide by storing a character **A**, **C**, **G**, or **T**. Since we are interested in making efficient changes to potentially very long lists, it is important to consider the time complexity of all the operations on our DNA strands.

## Implementation

For the implementation, you will write a class called DNAList. You may use the official course version of a linked list for reference, but for the best learning experience, you should code your list class from scratch!

Your list should implement the following functions:

- `__init__(self, gene=’’)` This function creates a new list. The **gene** argument is an optional argument for which a default (empty string) value is provided. The list should be created such that it represents the DNA string provided as an argument. This function should run in time *O*(*k*) where *k* is the length of the **gene** string.

- `append(self, item)` This function takes in a single character and extends the list with a node that represents this character. This function should run in *O*(1) time.

- `join(self, other)` This function takes in another **DNAList** and adds it to the end of the list. This function should run in *O*(1) time.

- `splice(self, ind, other)` This function takes in an integer **ind** representing an index into the list, and another **DNAList**. It should then insert the **other** list into the list immediately after the **ind**’th character of this list. This function should run in *O*(*n*) time, where *n* is the length of the list and *k* is the length of the other list (that’s correct, *k* should not appear in the time complexity of this function).

- `snip(self, i1, i2)` This function removes a portion of the gene (list) as specified by the integers **i1** and **i2**. Specifically, counting from the beginning of the list as 0, the list should no longer contain all nodes from the node at position **i1** (inclusive) up to but not including position **i2**. This function should run in *O*(*n*) time, where *n* is the length of the list, and for full credit, should visit each node in the list at most once.

- `replace(self, repstr, other)` This function should find the *string* **repstr** as a subsequence of the list and replace it with the list given by **other**. This function should run in *O*(*n*) time, where *n* is the length of the list, and should visit each node in the list at most **len(repstr)** times.

- `copy(self)`  This function returns a new list with the same contents as the list called upon. It should run in *O*(*n*) time, where *n* is the length of the list.

- `__str__(self)` This should simply return a string with the contents of the nodes all together, such as **GCACTT**. This function should run in *O*(*n*) time, where *n* is the length of the list.

- You may implement any additional ’helper’ functions that you find useful for providing the above functionality. Make sure you clearly document the purpose and behavior of these functions.

As mentioned above, with all data structures, comprehensive testing is also important. A significant portion of your grade will be given for a good test suite. Provide a separate **genetester.py** that runs your tests. This file should be thoroughly commented to explain what each test is testing.

