# Copyright (c) 2021 - present, Timur Shenkao
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _generate_binary_tree_recursion(values: List[int], root: Optional[TreeNode], current_index: int) -> \
        Optional[TreeNode]:
    length = len(values)

    # create root node for the first call
    if not root:
        root = TreeNode(values[0], None, None)

    # there is value for left child; don't generate node if value is None
    if (2 * current_index + 1) <= length - 1 and values[2 * current_index + 1] is not None:
        root.left = TreeNode(values[2 * current_index + 1], None, None)
        # call recursively; if left child has its own children, they will be populated
        _generate_binary_tree_recursion(values, root.left, 2 * current_index + 1)

    # there is value for right child; don't generate node if value is None
    if (2 * current_index + 2) <= length - 1 and values[2 * current_index + 2] is not None:
        root.right = TreeNode(values[2 * current_index + 2], None, None)
        # call recursively; if right child has its own children, they will be populated
        _generate_binary_tree_recursion(values, root.right, 2 * current_index + 2)
    return root


def generate_binary_tree(values: List[int]) -> Optional[TreeNode]:
    """ Generate binary tree from list of values.
        Tree is not binary-search tree or balanced tree specifically.
    """
    # empty list --> no tree
    if not values:
        return None

    current = 0
    # call recursive function to generate tree
    return _generate_binary_tree_recursion(values, None, current)


def print_node(node: Optional[TreeNode]) -> None:
    print('node: ', node, '; value: ', node.val, '; left : ', node.left, '; right : ', node.right)


def print_binary_tree(root: Optional[TreeNode], is_root: bool = False) -> None:
    if root:
        if is_root:
            print()
        print_node(root)

        if root.left:
            print('left child of ', root, ' -->')
            print_binary_tree(root.left)

        if root.right:
            print('right child of ', root, ' -->')
            print_binary_tree(root.right)
