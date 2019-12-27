import unittest

from .AST import *
from .newparser import Parser, generate_tokens, Token


class TestConstructors(unittest.TestCase):

    def test_binOp_constructor(self):
        op = Token("MINUS", "-", 0, 1)
        left = ASTNode(op)
        right = ASTNode(op)
        node = BinOp(op, left, right)
        self.assertEqual(isinstance(node, BinOp), True)

    def test_unaryOp_constructor(self):
        token = Token("MINUS", "-", 0, 1)
        expr = ASTNode(token)
        node = UnaryOp(token, expr)
        self.assertEqual(isinstance(node, UnaryOp), True)

    def test_builtin_constructor(self):
        builtin = "max"
        args = []
        token = Token("MINUS", "-", 0, 1)
        node = Builtins(token, builtin, args)
        self.assertEqual(isinstance(node, Builtins), True)

    def test_term(self):
        tokens = generate_tokens("2")
        parser = Parser(tokens, "2")
        node = parser.parse()
        self.assertEqual(node.token.kind == "number" and node.token.value == '2', True)

    def test_unaryOp(self):
        tokens = generate_tokens("-2")
        parser = Parser(tokens, "-2")
        node = parser.parse()
        isUnaryNodeCorrect = node.token.value == "-" and node.token.kind == "-"
        self.assertEqual(isUnaryNodeCorrect and node.expr.token.value == '2', True)

    def test_binaryOp(self):
        tokens = generate_tokens("5-2")
        parser = Parser(tokens, "5-2")
        node = parser.parse()
        isUnaryNodeCorrect = node.token.value == "-" and node.token.kind == "-"
        isPrimitivesNodesCorrect = node.left.token.value == '5' and node.right.token.value == '2'
        self.assertEqual(isUnaryNodeCorrect and isPrimitivesNodesCorrect, True)