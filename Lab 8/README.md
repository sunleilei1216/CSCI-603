# Lab 8

## Introduction

An *interpreter* is a program that executes instructions for a programming language. The **python3** interpreter executes Python programs. This assignment involves writing an interpreter for a very simple language called **PreTee**.

The interpreter accepts *prefix* mathematical expressions as input, where a prefix expression is one in which the mathematical operation is written at the beginning rather than in the middle. Inside the interpreter is a *parser*, whose job is to convert prefix expressions, represented as a string, into a collection of tree structures known as *parse trees*. The PreTee interpreter can evaluate mathematical expressions using the operators **+**, **-**, **\***, and **//**. The supported operands are positive integer literals (e.g., **8**) and variables (e.g., **’x’**). A data structure called a *symbol table* is used by the interpreter to associate a variable with its integer value. When given a prefix expression, PreTee displays the *infix* form of the expression and evaluates the result.

Consider the following example using the prefix expression: **''\* 8 + x y''**

![Lab8-1](https://i.imgur.com/lIoAwdE.png)

Let’s assume that the parse tree has already been constructed from the prefix expression. The infix form of the expression can be obtained by doing an **inorder** (left, parent, right) traversal of the tree from the root and constructing a string. Recall the private **__inorder** helper function from lecture that **__str\__** called when getting a string representation of a general purpose tree.

```python
def __inorder(self, node):
    if not node:
        return ’ ’
    else:
        return self.__inorder(node.left) + \
               str(node.val) + \
               self.__inorder(node.right)
```

The result of the expression can be found by evaluating the root node in **preorder** fashion (parent, left, right).

The implementation stage will cover details of the symbol table and evaluation of the parses tree to generate the result of the expression.

## Design

### PreTee Language

The source code lines begin with one of four tokens:

- **#**: The line is a comment.
- **=**: The line is an assignment statement.
- **@**: The line is a print statement.
- **''''**: A blank line (counted but ignored).

#### Comment

Any line that is a comment is ignored when parsed. It still counts as a line number. For example:
```python
# this line is a comment
```

#### Assignment

An assignment statement is of the prefix form:
```python
= {variable} {expression}
```
For example:
```python
= x 10
= y 20
= z + x y
= x 40
```
When emitted, the variable is emitted, followed by the equals sign, followed by the emission of the expression that followed.
```python
x = 10
y = 20
z = (x + y)
x = 40
```
When evaluated, the expression is evaluated and its result is stored in the symbol table for the variable:
```python
# symbol table: {..., 'x': 10, ...}
# symbol table: {..., 'y': 20, ...}
# symbol table: {..., 'z': 30, ...}
# symbol table: {..., 'x': 40, ...}
```
A syntax error exception will be raised for the following:
1. Assignment to a non-variable node, e.g.:
   ```python
   = 10 10      # error message: Bad assignment to non-variable
   ```
2. Bad expression for assignment, e.g.:
   ```python
   = x @        # error message: Bad assignment expression
   ```

#### Print

A print statement is of the prefix form, where expression is optional:
```python
@ {expression}
```
For example:
```python
@               # prints a new line
@ 10
@ + 10 20
@ x             # assuming x = 10
```
When emitted, the string **''print''** is emitted, followed by a space, and the emission of the expression that follows.
```python
print
print 10
print (10 + 20)
print x
```
When evaluated, the expression is evaluated and its result, if present, is displayed:
```python
                # just a newline is printed
10
30
10              # the value of x is printed
```

### Expressions

These are the various expressions that can be encountered when parsing statements.

#### Literal

A literal expression is of the prefix form, where value is an integer:
```python
{value}
```
For example:
```python
10
4
```
When emitted, the expressions are displayed infix as strings:
```
10
4
```
When evaluated, their integer form is returns:
```python
10
4
```

#### Variable

A variable expression is a legal identifier in Python:
```python
{id}
```
For example:
```python
x
y
variable
```
When emitted, the variable name is returned as a string, e.g.:
```python
x
y
variable
```
When evaluated, the value associated with the variable name in the symbol table is returned. For example if the symbol table contains `{..., 'x': 10, 'y': 20, 'z': 30, ...}`, the evaluations would be:
```python
10
20
30
```
A runtime exception is raised if the variable is not in the symbol table, e.g.:
```python
a               # error message: Unrecognized variable a
```

#### Math

A math expression is of the prefix form:
```python
{operator} {left-expression} {right-expression}
```
For example:
```python
+ 10 20
* 3 5
- 2 4
// 13 2
+ 2 * 8 7
```
When emitted, the statement is converted into an infix string:
```
(10 + 20)
(3 * 5)
(2 - 4)
(13 // 2)
(2 + (8 * 7))
```
When evaluated, integer result is returned:
```python
30
15
-2
6
58
```
A runtime exception is raised division by 0 is attempted:
```python
// 4 0          # error message: Division by zero error
```

### Full Example

The full grammar can be seen in this example source file, **prog1.pre**.
```python
# Create three variables
= x 10
= y 20
= z + x y

# Print some expressions
@
@ + 10 20
@ - 10 20
@ * 10 20
@ // 20 10
@ z
@ * x + y z
@ // * x + y 10 - y * 10 z
```

### Sample Run

The interpreter is run by providing the source code file as a command line argument:
```
$ python3 pretree.py prog1.pre
```
Note: To specify the command line argument in PyCharm, go to **Edit Configurations...** and then specify the source code file name in **Script parameters**.

When run, the three stages of interpretation occur:

1. **Parsing**: The source code is compiled into a sequential collection of parse trees.
2. **Emitting**: The parse trees are traversed inorder to generate infix strings of the statements.
3. **Evaluating**: The parse trees are executed and any printed output is generated.

Here is the full interpretation output for **prog1.pre**:
```
PRETEE: Compiling prog1.pre...

PRETEE: Infix source...
x = 10
y = 20
z = (x + y)
print
print (10 + 20)
print (10 - 20)
print (10 * 20)
print (20 // 10)
print z
print (x * (y + z))
print ((x * (y + 10)) // (y - (10 * z)))

PRETEE: Executing...

30
-10
200
2
30
500
-2
```

### Errors

There are two types of errors that can occur when interpreting:

#### Syntax Errors

These occur when parsing the statements and a violation of the grammar is encountered. Under these circumstances, the interpreter will not generate a parse tree for this statement (and thus will not emit in infix form). *The interpreter must display the line number the syntax error occurs on.*

Syntax errors do not halt parsing. The parsing continues as normal with the next statement, and any further syntax errors encountered will also be displayed. However, if there are any syntax errors in the program, it will not execute.

Using the example above, these are the syntax errors you need to deal with:
```python
=               # Incomplete statement
= 10 10         # Bad assignment to non-variable
= x @           # Bad assignment expression
^               # Invalid token ^
```

#### Runtime Errors

Runtime errors occur during execution of the parse trees. These can only happen if there are no syntax errors. When the first runtime error is encountered, the program should display the error and then halt execution of the program.

Using the example above, these are the runtime errors you need to deal with:
```python
@ a             # Unrecognized variable a
@ // 5 0        # Division by zero error
```

### PreTee UML

![Lab8-2](https://i.imgur.com/uk71BuV.jpg)

The full object oriented design is diagrammed above. It involves the following classes

- **PreTee**: The main interpreter class. It is responsible for parsing the PreTee source code, displaying it in infix, and then executing it.

- **AssignmentNode**: A class to represent the assignment node. It assigns the result of an expression to a variable.

- **LiteralNode**: A class to represent a literal node containing a positive integer.

- **MathNode**: A class to represent a mathematical node. It contains the operation, plus the left and right expressions.

- **PrintNode**: A class to to represent a print node. It displays the result of an expression to standard output.

- **VariableNode**: A class to represent a variable node. It stores the id of the variable and can retrieve its stored value from the symbol table.

- **SyntaxError**: An exception class used to indicate syntax errors when compiling the code.

- **RuntimeError**: An exception class used to indicate runtime errors that occur during execution.

### Python Documentation

The pydocs for all the classes have been generated in HTML and are stored on the MyCourses content section for this lab.

### Interpreter Design

The **PreTree** class is the heart of the interpreter. It contains the following slots:

- **srcFile**: the name of the source file (string)

- **symTbl**: the symbol table (dictionary: key=string, value=int)

- **parseTrees**: a list of the root nodes for valid, non-commented line of code

- **lineNum**: when parsing, the current line number in the source file (int)

- **syntaxError**: indicates whether a syntax error occurred during parsing (bool). If there
is a syntax error, the parse trees will not be evaluated

The routines that are used by the main program are:

- **__init\__** : A constructor for initializing the interpreter.

- **parse**: The compilation phase that parses the source code and builds the parse trees.

- **emit**: The generation of the infix form of the parse trees.

- **evaluate**: The execution of the parse trees and generation of output.

### Node Design

The Node classes have di↵erent slots depending on their type. Please refer to the source code for more information.

All Node classes implement three methods:

- A constructor for initializing the slots.

- A **emit** function that takes nothing and returns an infix string for the node and its children.

- An **evaluate** function that takes nothing and returns the integer result of evaluating this node and all of its children.

## Implementation

### Starting Code

You should first download the starter code, **pretee.zip** from MyCourses under the Content Area for this lab. Unzip the code and import it into a new project in PyCharm. It should run without error but produce no real output.

### Provided Modules

We are giving you all the python source code for the project:

- **pretee.py**: The main program which contains the **PreTree** class. The main program is given to you completely and should not be changed. You will be implementing all the methods for the **PreTree** class.

  For **PreTee** (and all other classes), the class, slots, methods and docstring’s are all given to you. You are not allowed to change any of the slots, or method names. You should write your code in the provided methods and not create any additional ones. You are free to use whatever local variables you want in the methods, but there should be no use of globals. For any files you contribute to, make sure your name/s are added as authors in the top docstring for the module.

- **assignment_node.py**: This is a complete implementation of the **AssignmentNode** class. You should not alter this file at all. It is being given to you as a demonstration of how one node is implemented.

- **literal_node.py**: Contains the **LiteralNode** class that you will provide implementation for the methods contained within.

- **math_node.py**: Contains the **MathNode** class that you will provide implementation for the methods contained within.

- **print_node.py**: Contains the **PrintNode** class that you will provide implementation for the methods contained within.

- **variable_node.py**: Contains the **VariableNode** class that you will provide implementation for the methods contained within.

- **runtime_error.py**: The definition of the **RuntimeError** exception class. You should not modify this file.

- **syntax error.py**: The definition of the **SyntaxError** exception class. You should not modify this file.

#### Restrictions

You are not allowed to use Python’s build in **eval()** method for evaluating nodes. All nodes must be evaluating by traversing the parse trees from the root.
