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

# 617. Merge Two Binary Trees   https://leetcode.com/problems/merge-two-binary-trees/
# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while
# the others are not. You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.


class Solution:
    def merge_trees_recursion(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # if both trees are non-empty: add root values; call recursively on left and right children
        # assign the returned values as left and right children of the first tree
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.merge_trees_recursion(root1.left, root2.left)
            root1.right = self.merge_trees_recursion(root1.right, root2.right)

        # if the first tree is empty then use nodes from the second tree
        if not root1:
            root1 = root2
        # return the first tree (its root) as a result
        # subtlety: if the second tree is empty then use nodes from the first tree
        return root1

    def merge_trees_iteration(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        # empty trees
        if not root1:
            return root2
        if not root2:
            return root1

        # both roots are non-empty
        stack = list()
        # use Depth First Search style to traverse
        stack.append((root1, root2))
        while stack:
            curr1, curr2 = stack.pop()
            # nodes from both trees are present
            if curr1 and curr2:
                curr1.val += curr2.val
                # there is no left subtree in the first tree
                if not curr1.left:
                    curr1.left = curr2.left
                else:
                    stack.append((curr1.left, curr2.left))

                if not curr1.right:
                    curr1.right = curr2.right
                else:
                    stack.append((curr1.right, curr2.right))
            # there is no second tree: do nothing as we return modified first tree as a result
            # don't add to stack anything
            else:
                continue

        return root1
