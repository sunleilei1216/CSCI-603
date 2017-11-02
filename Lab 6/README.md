# Lab 6
![Lab6](https://i.imgur.com/cAnkB56.jpg)

In this lab, we are consider the operation of gene splicing, snipping and joining. Specifically, we will represent a strand of DNA as a linked list. Each node in the list represents one nucleotide by storing a character **A**, **C**, **G**, or **T**. Since we are interested in making efficient changes to potentially very long lists, it is important to consider the time complexity of all the operations on our DNA strands.

## Implementation

For the implementation, you will write a class called DNAList. You may use the official course version of a linked list for reference, but for the best learning experience, you should code your list class from scratch!

Your list should implement the following functions:

- ```__init__(self,gene=’’) ```This function creates a new list. The gene argument is an optional argument for which a default (empty string) value is provided. The list should be created such that it represents the DNA string provided as an argument. This function should run in time *O*(*k*) where *k* is the length of the **gene** string.

- append(self,item) This function takes in a single character and extends the list with a node that represents this character. This function should run in *O*(1) time.
