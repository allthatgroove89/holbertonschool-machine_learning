#!/usr/bin/env python3
"""
This module defines a Node class for building a decision tree.
"""

import numpy as np


class Node:
    """
    A class used to represent a Node in a decision tree.

    Attributes
    ----------
    feature : int
        The feature index used for splitting the node.
    threshold : float
        The threshold value used for splitting the node.
    left_child : Node
        The left child node.
    right_child : Node
        The right child node.
    is_leaf : bool
        Indicates if the node is a leaf node.
    is_root : bool
        Indicates if the node is the root node.
    sub_population : list
        The subset of data points that reach this node.
    depth : int
        The depth of the node in the tree.
    """
    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        # If the node is a leaf, return its depth
        if self.is_leaf:
            return self.depth

        # If the node has children, find the max depth
        # from the left and right children
        left_depth = (
            self.left_child.max_depth_below()
            if self.left_child
            else self.depth
        )
        right_depth = (
            self.right_child.max_depth_below()
            if self.right_child
            else self.depth
        )

        # Return the max depth from the children
        # plus one (to account for node's depth)
        return max(left_depth, right_depth)


class Leaf(Node):
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        return self.depth


class Decision_Tree():
    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random",
                 root=None):
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
        return self.root.max_depth_below()
