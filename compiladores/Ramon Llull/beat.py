from antlr4 import *
from llullLexer import llullLexer
from llullParser import llullParser
from beatVisitor import beatVisitor
import sys


def main():
    input_stream = FileStream(sys.argv[1])
    lexer = llullLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llullParser(token_stream)
    tree = parser.root()
    visitor = beatVisitor()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
