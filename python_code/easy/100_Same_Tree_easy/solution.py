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

# 100. Same Tree  https://leetcode.com/problems/same-tree/
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4

class Solution:
    def is_same_tree_recursion(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # both trees are empty
        if not p and not q:
            return True

        if p and q:
            if p.val != q.val:
                return False
            else:
                return self.is_same_tree_recursion(p.left, q.left) and self.is_same_tree_recursion(p.right, q.right)
        # if one of the trees is empty
        return False

    def is_same_tree_iteration(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: O(N). The last level with leaves may contain N/2 nodes in case of balanced tree
        """
        # use stack for iterative DFS
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.append((p.left,  q.left))
                stack.append((p.right, q.right))
            elif p or q:
                return False
        return True
