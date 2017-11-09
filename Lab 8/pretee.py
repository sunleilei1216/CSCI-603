"""
CSCI-603 PreTee Lab
Author: Sean Strout @ RIT CS
Author: Jietong Chen
        Leilei Sun

The main program and class for a prefix expression interpreter of the
PreTee language.  See prog1.pre for a full example.

Usage: python3 pretee.py source-file.pre
"""

import sys  # argv
import literal_node  # literal_node.LiteralNode
import variable_node  # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import print_node  # print_node.PrintNode
import math_node  # math_node.MathNode
import syntax_error  # syntax_error.SyntaxError
import runtime_error  # runtime_error.RuntimeError


class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN

    def __init__(self, srcFile):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """
        self.srcFile = srcFile
        self.symTbl = {}
        self.parseTrees = []
        self.lineNum = 0
        self.syntaxError = False

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).
        :return:
        """
        # no token left
        if len(tokens) < 1:
            # error message: Incomplete statement
            self.syntaxError = True
            return syntax_error.SyntaxError("Incomplete statement")

        elif len(tokens) == 1:
            if tokens[0].isdigit():
                return literal_node.LiteralNode(int(tokens[0]))

            elif tokens[0].isidentifier():
                return variable_node.VariableNode(tokens[0], self.symTbl)

            else:
                # error message: Invalid token
                self.syntaxError = True
                return syntax_error.SyntaxError("Invalid token %s" % tokens[0])

        elif tokens[0] in self.MATH_TOKENS:
            # leaf nodes required to construct the left expression parse tree
            leavesNeed = 1

            for i in range(1, len(tokens)):
                if tokens[i].isdigit() or tokens[i].isidentifier():
                    # a leaf node
                    leavesNeed -= 1

                elif tokens[i] in self.MATH_TOKENS:
                    # a interior node, need one more leaf node to construct the
                    # full binary tree
                    leavesNeed += 1

                else:
                    # error message: Invalid token
                    self.syntaxError = True
                    return syntax_error.SyntaxError("Invalid token %s" %
                                                    tokens[i])

                # has all nodes required to construct the left expression
                if leavesNeed == 0:
                    # construct the left and right expression
                    left = self.__parse(tokens[1:i + 1])
                    right = self.__parse(tokens[i + 1:])

                    # error raised in construction of left expression
                    if isinstance(left, syntax_error.SyntaxError):
                        return left

                    # error raised in construction of right expression
                    if isinstance(right, syntax_error.SyntaxError):
                        return right

                    return math_node.MathNode(left, right, tokens[0])

        else:
            # error message: Invalid token
            self.syntaxError = True
            return syntax_error.SyntaxError("Invalid token %s" % tokens[0])

    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """
        file = open(self.srcFile)

        for line in file:
            self.lineNum += 1
            tokens = line.split()

            # empty line
            if len(tokens) == 0:
                continue

            # assignment statement
            if tokens[0] == self.ASSIGNMENT_TOKEN:
                # lack of tokens
                if len(tokens) < 3:
                    self.syntaxError = True

                    # error message: Incomplete statement
                    print("\nFile \"%s\", line %d"
                          % (self.srcFile, self.lineNum), file=sys.stderr)
                    print("  %sSyntaxError: Incomplete statement"
                          % line, file=sys.stderr)

                    continue

                # left token is not valid variable name
                if not tokens[1].isidentifier():
                    self.syntaxError = True

                    # error message: Bad assignment to non-variable
                    print("\nFile \"%s\", line %d"
                          % (self.srcFile, self.lineNum), file=sys.stderr)
                    print("  %sSyntaxError: Bad assignment to non-variable"
                          % line, file=sys.stderr)

                    continue

                # construct parse tree for expression on the right
                expression = self.__parse(tokens[2:])

                # error raised during the construction of parse tree
                if isinstance(expression, syntax_error.SyntaxError):
                    # print out the error message
                    print("\nFile \"%s\", line %d"
                          % (self.srcFile, self.lineNum), file=sys.stderr)
                    print("  %sSyntaxError: %s"
                          % (line, expression), file=sys.stderr)

                else:
                    # create a new AssignmentNode
                    self.parseTrees.append(assignment_node.AssignmentNode(
                        variable_node.VariableNode(tokens[1], self.symTbl),
                        expression, self.symTbl, tokens[0]))

            # print statement
            elif tokens[0] == self.PRINT_TOKEN:
                # empty expression
                if len(tokens) == 1:
                    self.parseTrees.append(print_node.PrintNode(None))

                else:
                    # construct parse tree for the expression
                    expression = self.__parse(tokens[1:])
                    # create a new PrintNode
                    self.parseTrees.append(print_node.PrintNode(expression))

            # comment line
            elif tokens[0] == self.COMMENT_TOKEN:
                continue

            else:
                self.syntaxError = True

                # error message: Invalid token
                print("\nFile \"%s\", line %d"
                      % (self.srcFile, self.lineNum), file=sys.stderr)
                print("  %sSyntaxError: Invalid token %s"
                      % (line, tokens[0]), file=sys.stderr)

        file.close()

    def emit(self):
        """
        Prints an infix string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """
        # traversal all parse trees in the list and call their emit() function
        for parseTree in self.parseTrees:
            print(parseTree.emit())

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """
        if self.syntaxError == True:
            print("Found syntax error in source file \"%s\", will not execute."
                  % self.srcFile)

        else:
            pass


def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('*** Runtime error:', e)


if __name__ == '__main__':
    main()
