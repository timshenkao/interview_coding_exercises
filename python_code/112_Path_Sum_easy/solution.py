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

# 112. Path Sum  https://leetcode.com/problems/path-sum/
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
# A leaf is a node with no children.


class Solution:
    def _has_path_sum_recursion(self, root: Optional[TreeNode], target_sum, partial_sum) -> bool:
        # the node is a leaf
        if not root.left and not root.right:
            return (partial_sum + root.val) == target_sum

        # the node is NOT a leaf
        if root.left:
            is_left_path_sum = self._has_path_sum_recursion(root.left, target_sum, partial_sum + root.val)
            # There is root-to-leaf path in left subtree. No need ton continue
            if is_left_path_sum:
                return is_left_path_sum
        # there is no left child
        else:
            is_left_path_sum = False

        # the node is NOT a leaf
        if root.right:
            is_right_path_sum = self._has_path_sum_recursion(root.right, target_sum, partial_sum + root.val)
            # There is root-to-leaf path in right subtree. No need ton continue
            if is_right_path_sum:
                return is_right_path_sum
        # there is no right child
        else:
            is_right_path_sum = False

        # combine results from left and right subtrees
        return is_left_path_sum or is_right_path_sum

    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree
        if not root:
            return False

        # check paths via left child or right child
        return self._has_path_sum_recursion(root, target_sum, 0)
