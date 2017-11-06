# Lab 7

## Introduction

First we will study some properties of hash functions.

In both open addressing and chaining, collisions degrade performance. Many keys mapping to the same location in a hash table result in a linear search. Clearly, good hash functions should minimize the number of collisions. How might the “goodness” or “badness” of a given hash function be measured by looking at the hash table after it has loaded its entries?

This may be best explained by an example. Look at Figure 1. A program entered 5 keys – A, B, C, D, and E – into a chaining hash table of length 10.)

![Lab7](https://i.imgur.com/v2VODXV.jpg)

Figure 1: Two hypothetical hash functions applied to the same hash table array and the same stream of keys being put in the table

The figure shows the application of two different hash functions to this scenario. Clearly the second function is better, but how can you quantify that based on what you can measure in the tables?

## Implementation

The goal of this assignment is to examine how effective different hash functions are for storing English words. The program you will create and submit should be called **hashtable.py**.

### Instrumenting the Hashmap

For the first part of the implementation, you will add some code to a hashmap implementation to keep track of both the number of collisions and the number of probes required to add and search for keys in a hash map. In particular, you should start from the **hashmap.py** provided in the course website. The **put** function should count both collisions and probes (as defined in the problem solving portion of this assignment) and the **get** and **contains** functions should add to the count of probes.

The next step is to modify the hash map implementation to use different hash functions. That is, the constructor should accept an argument of a hash function in addition to any other argument(s) it might need.

Then, you should write at least two significantly different hash functions for strings. By significantly different, we intend that they compute the hash in qualitatively different ways (not just changing some constants). They should attempt to be good hash functions, not just trivial ones!

### Main method implementation

Now, it will be time to perform some testing. You will write a main method that the words in a text file into a hash map to count how many times each word appears. After it does so, it should then iterate through the hash map to find one word that has appeared the maximum number of times (if multiple words are tied, printing any such word is fine). It should also then print out how many probes and how many collisions occurred during this entire process. Write the main method so that it will test the same words on hash maps with *different hash functions* and *different maximum load factors* and print out the statistics for each separate case.

To remove punctuation from a word (and between words), you can use the **re** [regular expression] module. First **import re** and then the function call **re.split(’\W+’, t)** will take a line of text in the variable **t** and return a list of the words in **t** (skipping spaces and punctuation). Note that this will also split the word **don’t** into **don** and **t** but for this exercise we will not worry about such details. You should also convert all words to lower case.

### Evaluation

To get some good data upon which to test your hash functions, you should get two full novels from Project Gutenberg (**http://www.gutenberg.org**). These should each contain at least 50,000 words. You should also use a dictionary such as the one provided in Ubuntu or OS X at **/usr/share/dict/words** (this file actually contains different dictionaries in the two operating systems!). Send each of these through your main method, testing your two hash functions as well as Python’s builtin **hash** function over three different maximum load factors of your choice.

Then, you should collect and report on the data that you have obtained. Compare the results from the different input files, hash functions and load factors in tabular and/or graphical form, **putting this in a PDF document**.
