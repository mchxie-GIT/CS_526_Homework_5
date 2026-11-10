import random
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def AddNode(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def DeleteNode(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # With zero or one child, return the subtree that stays.
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # With two children, use the largest value on the left.
            predecessor = node.left
            while predecessor.right is not None:
                predecessor = predecessor.right
            node.value = predecessor.value
            node.left = self._delete(node.left, predecessor.value)

        return node

    def FindNode(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return None

    def PrintTree(self):
        if self.root is None:
            print("(empty)")
        else:
            self._print_subtree(self.root, 0, "Root: ")

    def _print_subtree(self, node, depth, label):
        if node is None:
            return
        print("    " * depth + label + str(node.value))
        self._print_subtree(node.left, depth + 1, "L: ")
        self._print_subtree(node.right, depth + 1, "R: ")


def main():
    # The optional seed makes the screenshot run reproducible.
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else None
    rng = random.Random(seed)
    values = rng.sample(range(1, 1001), rng.randint(5, 50))
    unused = [value for value in range(1, 1001) if value not in values]
    tree = BST()

    for value in values:
        tree.AddNode(value)
    print(f"Input set ({len(values)} values, in insertion order):")
    print(values)
    print("\nInitial tree:")
    tree.PrintTree()

    added = rng.choice(unused)
    print(f"\nAfter AddNode({added}):")
    tree.AddNode(added)
    tree.PrintTree()

    deleted = values[0]
    print(f"\nAfter DeleteNode({deleted}):")
    tree.DeleteNode(deleted)
    tree.PrintTree()

    # Pick randomly from the present and absent values to guarantee both cases.
    present = values[1:] + [added]
    absent = [value for value in unused if value != added] + [deleted]
    for value in [rng.choice(present), rng.choice(absent)]:
        result = "found" if tree.FindNode(value) is not None else "not found"
        print(f"\nFindNode({value}): {result}")


if __name__ == "__main__":
    main()
