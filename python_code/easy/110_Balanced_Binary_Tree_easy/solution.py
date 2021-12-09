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

# 110. Balanced Binary Tree https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
#     a binary tree in which the left and right subtrees of EVERY node differ in height by no more than 1.
# The number of nodes in the tree is in the range [0, 5000].
# -10 000 <= Node.val <= 10 000


class Solution:
    def _subtree_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # left subtree height
        left_height = self._subtree_height(root.left)
        # right subtree height
        right_height = self._subtree_height(root.right)
        # current node height
        current_level_from_leaves = max(abs(left_height), abs(right_height)) + 1
        # negative height means that tree is imbalanced either in left subtree or right subtree
        # or becomes imbalanced in current node
        # we pass negative value up to the root
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            current_level_from_leaves *= -1
        return current_level_from_leaves

    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # tree is empty
        if not root:
            return True
        # tree has just 1 node
        if not root.left and not root.right:
            return True

        return self._subtree_height(root) >= 0
