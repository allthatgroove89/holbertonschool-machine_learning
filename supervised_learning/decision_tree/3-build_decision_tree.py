#!/usr/bin/env python3
"""Module for the Decision_Tree class."""
import numpy as np


class Node:
    """A class representing a node in a decision tree."""

    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """Initialize a Node.

        Args:
            feature: The feature used for splitting at this node.
            threshold: The threshold value for the feature.
            left_child: The left child Node.
            right_child: The right child Node.
            is_root: A boolean indicating if this node is the root.
            depth: The depth of this node in the tree.
        """
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """Calculate the maximum depth of the tree below this node.

        Returns:
            The maximum depth of the tree below this node.
        """
        if self.is_leaf:
            return self.depth
        else:
            if self.left_child:
                left_depth = self.left_child.max_depth_below()
            else:
                left_depth = 0
            if self.right_child:
                right_depth = self.right_child.max_depth_below()
            else:
                right_depth = 0
            return max(left_depth, right_depth)

    def count_nodes_below(self, only_leaves=False):
        """Count the number of nodes below this node.

        Args:
            only_leaves (bool): If True, only count leaf nodes.

        Returns:
            int: The number of nodes below this node.
        """
        # If only leafs are to be counted
        if only_leaves:
            # Check if the current node is a leaf
            if self.is_leaf:
                return 1
            else:
                left_count = self.left_child.count_nodes_below(
                    only_leaves=True) if self.left_child else 0
                right_count = self.right_child.count_nodes_below(
                    only_leaves=True) if self.right_child else 0
            return left_count + right_count

        # If only_leaves is falsy
        else:
            left_count = self.left_child.count_nodes_below(
                only_leaves=False) if self.left_child else 0
            right_count = self.right_child.count_nodes_below(
                only_leaves=False) if self.right_child else 0
        return 1 + left_count + right_count

    def __str__(self):
        """
        Method that returns the string representation of the current node
        """
        node_str = (
            f"root [feature={self.feature}, threshold={self.threshold}]\n"
            if self.is_root else
            f"-> node [feature={self.feature}, "
            f"threshold={self.threshold}]\n"
        )

        # If the node is a leaf, simply return the string representation
        if self.is_leaf:
            return node_str

        # Formatting for the left and right children
        left_str = self.left_child_add_prefix(
            self.left_child.__str__()) if self.left_child else ""
        right_str = self.right_child_add_prefix(
            self.right_child.__str__()) if self.right_child else ""

        return node_str + left_str + right_str

    def left_child_add_prefix(self, text):
        """ Add prefix to the left child """
        lines = text.split("\n")
        # Adding prefix to the first line
        new_text = "    +--" + lines[0] + "\n"
        # Adding prefix to the rest of the lines
        new_text += "\n".join(["    |  " + line for line in lines[1:-1]])
        # Append an additional newline character if there are multiple lines
        new_text += "\n" if len(lines) > 1 else ""
        return new_text

    def right_child_add_prefix(self, text):
        """ Add prefix to the right child """
        lines = text.split("\n")
        # Adding prefix to the first line
        new_text = "    +--" + lines[0] + "\n"
        # Adding prefix to the rest of the lines
        new_text += "\n".join(["     " + "  " + line for line in lines[1:-1]])
        # Append an additional newline character if there are multiple lines
        new_text += "\n" if len(lines) > 1 else ""
        return new_text

    def get_leaves_below(self):
        """Get all leaf nodes below this node.

        Returns:
            list: A list of leaf nodes below this node.
        """
        if self.is_leaf:
            return [self]
        leaves = []
        if self.left_child:
            leaves.extend(self.left_child.get_leaves_below())
        if self.right_child:
            leaves.extend(self.right_child.get_leaves_below())
        return leaves


class Leaf(Node):
    """A class representing a leaf node in a decision tree."""

    def __init__(self, value, depth=None):
        """Initialize a Leaf.

        Args:
            value: The value or class label that
            is predicted at this leaf node.
            depth: The depth of this node in the tree.
        """
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Calculate the maximum depth of the tree below this node.

        Since this is a leaf node, it returns its own depth.

        Returns:
            The depth of this leaf node.
        """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """Count the number of nodes below this leaf.

        Args:
            only_leaves (bool): If True, only count leaf nodes.

        Returns:
            int: The number of nodes below this leaf.
        """
        return 1

    def __str__(self):
        """
        Method that returns the string representation of the current node
        """
        return (f"-> leaf [value={self.value}]")

    def get_leaves_below(self):
        return [self]


class Decision_Tree():
    """A class representing a decision tree."""

    def __init__(self, max_depth=10, min_pop=1,
                 seed=0, split_criterion="random", root=None):
        """Initialize a Decision_Tree.

        Args:
            max_depth: The maximum depth of the tree.
            min_pop: The minimum population size at a
            node for a split to be considered.
            seed: The seed for the random number generator.
            split_criterion: The criterion used for splitting at each node.
            root: The root node of the tree.
        """
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """Calculate the maximum depth of the tree.

        Returns:
            The maximum depth of the tree.
        """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """Count the number of nodes in the tree.

        Args:
            only_leaves (bool): If True, only count leaf nodes.

        Returns:
            int: The number of nodes in the tree.
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        """
        Method that returns the string representation of the decision tree
        """
        return self.root.__str__() if self.root else ""

    def get_leaves(self):
        """Get all leaf nodes in the tree.

        Returns:
            list: A list of leaf nodes in the tree.
        """
        return self.root.get_leaves_below() if self.root else []
