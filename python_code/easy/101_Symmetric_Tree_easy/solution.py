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

# 101. Symmetric Tree https://leetcode.com/problems/symmetric-tree/
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


class Solution:
    def _is_symmetric_tree_recursion(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both trees are empty
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False
            else:
                return self._is_symmetric_tree_recursion(p.left, q.right) \
                       and self._is_symmetric_tree_recursion(p.right, q.left)
        # if one of the trees is empty
        return False

    def _is_symmetric_tree_iteration(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use stack for DFS
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.append((p.left,  q.right))
                stack.append((p.right, q.left))
            elif p or q:
                return False
        return True


    def is_symmetric_recursion(self, root: Optional[TreeNode]) -> bool:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree
        if not root:
            return True
        # just 1 node in the tree
        if not root.left and not root.right:
            return True
        if root.left and root.right:
            return self._is_symmetric_tree_recursion(root.left, root.right)
        return False

    def is_symmetric_iteration(self, root: Optional[TreeNode]) -> bool:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty tree
        if not root:
            return True
        # just 1 node in the tree
        if not root.left and not root.right:
            return True
        if root.left and root.right:
            return self._is_symmetric_tree_iteration(root.left, root.right)
        return False
