import re

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