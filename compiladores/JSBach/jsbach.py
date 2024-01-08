
from antlr4 import *
from TreeVisitor import JSTreeVisitor
from jsbachParser import jsbachParser
from jsbachLexer import jsbachLexer
import sys


def main():
    print(sys.argv)
    input_stream = FileStream(sys.argv[1])
    lexer = jsbachLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = jsbachParser(token_stream)
    tree = parser.root()
    visitor = JSTreeVisitor()
    visitor.visit(tree)


    if len(sys.argv) == 2:
        visitor.comenca0("Main")
    elif len(sys.argv) == 3:
        visitor.comenca0(sys.argv[2])
    else:
        visitor.comenca1(sys.argv[2], sys.argv[3:])

if __name__ == '__main__':
    main()