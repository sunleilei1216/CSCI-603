# Lab 4

## Problem

You would like to send messages back and forth with a friend (or co-consiprator!) but want to make sure that other people cannot easily read those messages. However, rather than use a fixed encryption scheme, you decide to take your message string and apply a series of transformations to it to generate the encrypted message.

The transformations you have agreed to use are the following:

- *σ<sub>i</sub>* shifts the letter at index *i* forward one letter in the alphabet. So, **BALL** → *σ*<sub>0</sub> → **CALL**.

&emsp;&emsp;This can be applied multiple times to shift multiple letters forward, and if so would be designated *σ<sub>i</sub><sup>k</sup>* to shift letter *i* by *k* forward. If the shift takes the letter past the end of the alphabet, it will wrap around. Negative exponents shift the letter backward in the alphabet.

- *ρ* rotates the string one position to the right. So, **TOPS** → *ρ* → **STOP**.

&emsp;&emsp;This function can also be used with an exponent (positive or negative). For example, **TRAIN** → *ρ*<sup>2</sup> → **INTRA**.

- *δ<sub>i</sub>* duplicates (in place) the letter at index *i*. So, **HOPED** → *δ*<sub>2</sub> → **HOPPED**. This can also be used with a positive exponent to produce multiple duplicates, but not with negative exponents.

- *τ<sub>i,j</sub>* swaps the letters at index *i* and index *j*. So, **SAUCE** → *τ*<sub>0,3</sub> → **CAUSE**. You can assume that *i* < *j*.

- *τ<sub>i,j</sub>*<sup>(*g*)</sup> operates a little differently. In this case, we conceptually divide the string to *g* equal-sized groups of letters, and then swap groups *i* and *j*. So, **BACKHAND** → *τ*<sub>0,2</sub><sup>(4)</sup> → **HACKBAND**.

To more effectively obfuscate your message, you can go through several transformations. For example, **CANAL** → *ρ*<sup>2</sup>*δ*<sub>2</sub>*σ*<sub>2</sub><sup>9</sup> → **ALLCAN**.

## Implementation

In the implementation, your program will read in two files (the names of which should come from user input). One file will represent your messages (one message per line) while the other will read the sets of transformations, also one per line. It will also ask the user whether the messages are to be encrypted using the given transformations or decrypted (that is, the given transformations have been applied to generate the messages).

The format of the messages will be all upper-case letters (no spaces or punctuation). The format of the transformation strings will be as follows:

|Operation|String form|Example| |
|---------|-----------|-----|---|
|*σ<sub>i</sub>*|**Si**|*σ*<sub>0</sub>|**S0**|
|*σ<sub>i</sub><sup>k</sup>*|**Si,k**|*σ*<sub>2</sub><sup>-5</sup>|**S2,-5**|
|*ρ*|**R**|*ρ*|**R**|
|*ρ<sup>i</sup>*|**Ri**|*ρ*<sup>-3</sup>|**R-3**|
|*δ<sub>i</sub>*|**Di**|*δ*<sub>2</sub>|**D2**|
|*δ<sub>i</sub><sup>k</sup>*|**Di,k**|*δ*<sub>2</sub><sup>3</sup>|**D2,3**|
|*τ<sub>i,j</sub>*|**Ti,j**|*τ*<sub>2,4</sub>|**T2,4**|
|*τ<sub>i,j</sub>*<sup>(*g*)</sup>|**T(g)i,j**|*τ*<sub>0,2</sub><sup>(4)</sup>|**T(4)0,2**|

If a series of transformations are to be supplied, they will be separated by semicolons. So, for example, if you were asked to encrypt the string **HORSE** given the transformation string **T2,4;S4;R** you would generate the string **SHOES**.

Finally, in order to improve the level of secrecy between you and those you exchange a message with, we are asking you to create one additional operation of your choice. The operation must be decryptable as well. Clearly describe in a comment how your operation works and how it is represented in the operation string, and provide an example.
