import re

plus_expr_re = r"[0-9]+ \+ [0-9]+"
times_expr_re = r"[0-9]+ \* [0-9]+"

class MathNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Val={self.val} L:[{self.left}] R:[{self.right}]"

def parse_tree(input_str: str):
    without_spaces = input_str.replace(" ", "")
    root = MathNode("")
    idx = 0

    while idx < len(without_spaces):
        char = without_spaces[idx]

        if char == "(":
            start_idx = idx + 1
            required_closing = 1

            while required_closing > 0:
                idx += 1
                char = without_spaces[idx]
                if char == "(":
                    required_closing += 1
                elif char == ")":
                    required_closing -= 1
            
            substring = without_spaces[start_idx:idx]
            sub_tree = parse_tree(substring)
            if root.left == None:
                root.left = sub_tree
            else:
                root.right = sub_tree
        elif char == "+" or char == "*":
            if (root.val == ""):
                root.val = char
            else:
                new_node = MathNode(char)
                new_node.left = root
                root = new_node
        else:
            if (root.val == ""):
                root.val = char
            else:
                root.right = MathNode(char)
        
        idx += 1
    
    return root

def evaluate_tree_node(tree_node: MathNode):
    if tree_node.val == "+":
        return evaluate_tree_node(tree_node.left) + evaluate_tree_node(tree_node.right)
    elif tree_node.val == "*":
        return evaluate_tree_node(tree_node.left) * evaluate_tree_node(tree_node.right)
    else:
        return int(tree_node.val)

def part_1(input):
    total = 0
    for line in input:
        root = parse_tree(line)
        total += evaluate_tree_node(root)
    return total

def evalutate_part_2_expr(expr: str):
    while "(" in expr:
        start_idx = expr.find("(")
        required_closing = 1
        end_idx = start_idx
        while required_closing > 0:
            end_idx += 1
            char = expr[end_idx]
            if char == "(":
                required_closing += 1
            elif char == ")":
                required_closing -= 1

        result = evalutate_part_2_expr(expr[start_idx + 1:end_idx])
        expr = expr[:start_idx] + result + expr[end_idx + 1:]
    
    while "+" in expr:
        plus_expr = re.search(plus_expr_re, expr)
        plus_result = eval(expr[plus_expr.start():plus_expr.end()])
        expr = expr[:plus_expr.start()] + str(plus_result) + expr[plus_expr.end():]
    
    while "*" in expr:
        times_expr = re.search(times_expr_re, expr)
        times_result = eval(expr[times_expr.start():times_expr.end()])
        expr = expr[:times_expr.start()] + str(times_result) + expr[times_expr.end():]

    return expr

def part_2(input):
    total = 0
    for line in input:
        total += int(evalutate_part_2_expr(line))
    return total