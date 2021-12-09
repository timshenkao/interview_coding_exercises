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

from python_code.helper.binary_trees import TreeNode


# 257. Binary Tree Paths  https://leetcode.com/problems/binary-tree-paths/
# Given the root of a binary tree, return all root-to-leaf paths in any order.
#  A leaf is a node with no children.
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100


class Solution:
    def binary_tree_paths(self, root: Optional[TreeNode]) -> List[str]:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        result = list()
        # empty tree
        if not root:
            return result

        def _result_append(node: Optional[TreeNode], path_to_node: str) -> None:
            if node:
                if path_to_node:
                    path_to_current_node = path_to_node + '->' + str(node.val)
                # if it's root of the tree
                else:
                    path_to_current_node = str(node.val)
                # leaf
                if not node.left and not node.right:
                    result.append(path_to_current_node)

                _result_append(node.left, path_to_current_node)
                _result_append(node.right, path_to_current_node)

        _result_append(root, '')
        return result

    def binary_tree_paths_iteration(self, root: Optional[TreeNode]) -> List[str]:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: O(N). We keep the whole tree in stack.
        """
        result = list()
        # empty tree
        if not root:
            return result

        temp_stack = [(root, str(root.val))]
        while temp_stack:
            curr_node, curr_path = temp_stack.pop()
            # leaf
            if not curr_node.left and not curr_node.right:
                result.append(curr_path)
            if curr_node.left:
                temp_stack.append((curr_node.left, curr_path + '->' + str(curr_node.left.val)))
            if curr_node.right:
                temp_stack.append((curr_node.right, curr_path + '->' + str(curr_node.right.val)))
        return result
