import unittest
from day18 import parse_tree, evaluate_tree_node, part_1, evalutate_part_2_expr, part_2

expr_1 = "1 + 2 * 3 + 4 * 5 + 6"
expr_2 = "2 * 3 + (4 * 5)"
expr_3 = "1 + (2 * 3) + (4 * (5 + 6))"
expr_4 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2"

class ParseTreeTests(unittest.TestCase):
    def test_parse_tree_simple(self):
        root =  parse_tree(expr_1)
        current_node = root

        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.right.val, "6")

        current_node = root.left
        self.assertEqual(current_node.val, "*")
        self.assertEqual(current_node.right.val, "5")

        current_node = root.left.left
        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.right.val, "4")

        current_node = root.left.left.left
        self.assertEqual(current_node.val, "*")
        self.assertEqual(current_node.right.val, "3")

        current_node = root.left.left.left.left
        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.right.val, "2")
        self.assertEqual(current_node.left.val, "1")
    
    def test_parse_tree_single_paren(self):
        root = parse_tree(expr_2)
        current_node = root

        self.assertEqual(current_node.val, "+")

        current_node = root.left
        self.assertEqual(current_node.val, "*")
        self.assertEqual(current_node.left.val, "2")
        self.assertEqual(current_node.right.val, "3")

        current_node = root.right
        self.assertEqual(current_node.val, "*")
        self.assertEqual(current_node.left.val, "4")
        self.assertEqual(current_node.right.val, "5")
    
    def test_parse_tree_nested_paren(self):
        root =  parse_tree(expr_3)
        current_node = root

        self.assertEqual(current_node.val, "+")

        current_node = root.left
        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.left.val, "1")

        current_node = root.left.right
        self.assertEqual(current_node.val, "*")
        self.assertEqual(current_node.left.val, "2")
        self.assertEqual(current_node.right.val, "3")

        current_node = root.right
        self.assertEqual(current_node.val, "*")
        self.assertEqual(current_node.left.val, "4")

        current_node = root.right.right
        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.left.val, "5")
        self.assertEqual(current_node.right.val, "6")

    def test_parse_tree_starting_paren(self):
        root =  parse_tree(expr_4)
        current_node = root

        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.right.val, "2")

        current_node = root.left
        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.right.val, "6")

        current_node = root.left.left
        self.assertEqual(current_node.val, "*")

        current_node = root.left.left.left
        self.assertEqual(current_node.val, "*")
        self.assertEqual(current_node.right.val, "9")

        current_node = root.left.left.left.left
        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.left.val, "2")
        self.assertEqual(current_node.right.val, "4")

        current_node = root.left.left.right
        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.right.val, "6")

        current_node = root.left.left.right.left
        self.assertEqual(current_node.val, "*")
        self.assertEqual(current_node.right.val, "8")

        current_node = root.left.left.right.left.left
        self.assertEqual(current_node.val, "+")
        self.assertEqual(current_node.left.val, "6")
        self.assertEqual(current_node.right.val, "9")

class EvaluateTreeNodeTests(unittest.TestCase):
    def test_evaluate_simple(self):
        root = parse_tree(expr_1)
        result = evaluate_tree_node(root)
        self.assertEqual(result, 71)

    def test_evaluate_single_paren(self):
        root = parse_tree(expr_2)
        result = evaluate_tree_node(root)
        self.assertEqual(result, 26)

    def test_evaluate_nested_paren(self):
        root = parse_tree(expr_3)
        result = evaluate_tree_node(root)
        self.assertEqual(result, 51)

example_input = [
    expr_1,
    expr_2,
    expr_3,
    expr_4
]

input_file = open("day18_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

class Part1Tests(unittest.TestCase):
    def test_example_input(self):
        result = part_1(example_input)
        self.assertEqual(result, 6960)
    
    def test_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 18213007238947)

class EvalutatePart2ExprTests(unittest.TestCase):
    def test_simple_expr(self):
        result = int(evalutate_part_2_expr(expr_1))
        self.assertEqual(result, 231)

    def test_paren_expr(self):
        result = int(evalutate_part_2_expr(expr_2))
        self.assertEqual(result, 46)
    
    def test_nested_paren_expr(self):
        result = int(evalutate_part_2_expr(expr_3))
        self.assertEqual(result, 51)
    
    def test_starting_paren_expr(self):
        result = int(evalutate_part_2_expr(expr_4))
        self.assertEqual(result, 11666)

class Part2Tests(unittest.TestCase):
    def test_example_input(self):
        result = part_2(example_input)
        self.assertEqual(result, 11994)
    
    def test_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 388966573054664)
        