from antlr4 import *
from llullLexer import llullLexer
from llullParser import llullParser
from LlullTreeVisitor import LlullTreeVisitor
import sys


def main():
    input_stream = FileStream(sys.argv[1])
    lexer = llullLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llullParser(token_stream)
    tree = parser.root()
    visitor = LlullTreeVisitor()
    visitor.visit(tree)

    if len(sys.argv) == 2:
        visitor.empieza0("main")
    elif len(sys.argv) == 3:
        visitor.empieza0(sys.argv[2])
    else:
        visitor.empieza1(sys.argv[2], sys.argv[3:])


if __name__ == '__main__':
    main()
