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

from typing import Optional

from python_code.helper.binary_trees import TreeNode

# 226. Invert Binary Tree  https://leetcode.com/problems/invert-binary-tree/
# Given the root of a binary tree, invert the tree, and return its root.


class Solution:
    def invert_tree_recursion(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              if we count recursion stack then O(height) which is O(log N) in case of balanced tree
                                and O(N) in case of unbalanced tree
        """
        # empty tree or root has no children
        if not root or (not root.left and not root.right):
            return root

        # root has at least one child; Depth-First Search;
        # invert children
        root.left, root.right = root.right, root.left
        self.invert_tree_recursion(root.left)
        self.invert_tree_recursion(root.right)
        return root

    def invert_tree_iteration(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: O(N). The last level with leaves may contain N/2 nodes in case of balanced tree
        """
        # empty tree or root has no children
        if not root or (not root.left and not root.right):
            return root

        # traverse binary tree in Breadth First Search manner
        # useful for very deep trees in memory-constrained environments
        queue = list()
        queue.append(root)
        while queue:
            curr_node = queue.pop(0)
            # invert children; whole subtrees with roots in these children are also rotated
            curr_node.left, curr_node.right = curr_node.right, curr_node.left

            # add to queue next nodes to handle
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        return root
