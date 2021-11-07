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

# 572. Subtree of Another Tree  https://leetcode.com/problems/subtree-of-another-tree/
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
# structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.


class Solution:
    def _check_subtree_recursion(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        # both trees aren't empty
        if root and sub_root:
            # values are the same, check left and right trees / subtrees correspondingly without current
            # root and sub_root
            if root.val == sub_root.val:
                return self._check_subtree_recursion(root.left, sub_root.left) and \
                       self._check_subtree_recursion(root.right, sub_root.right)
        # we reached leaf nodes both in tree and subtree during the previous recursion call,
        # i.e. subtree is in tree
        elif not root and not sub_root:
            return True
        else:
            return False

    def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree is subtree of any tree
        if not sub_root:
            return True

        # tree is empty but sub tree is non-empty
        if not root:
            return False

        # if values are the same, check the whole tree and subtree
        # recursion inside of recursion
        if root.val == sub_root.val:
            if self._check_subtree_recursion(root, sub_root):
                return True

        # values are not the same or subtree is not subtree for the current root
        # look deeper for subtree in left and right trees
        if self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root):
            return True

        return False
