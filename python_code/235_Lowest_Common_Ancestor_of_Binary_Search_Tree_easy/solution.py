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

from python_code.helper.binary_trees import TreeNode

# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


class Solution:
    def lowest_common_ancestor_recursion(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)
        # root is an ancestor as one of the values in left subtree and another one in right subtree
        if min_val <= root.val <= max_val:
            ancestor = root
        # both values are less than root value so check in left subtree
        elif min_val <= root.val and max_val <= root.val:
            ancestor = self.lowest_common_ancestor_recursion(root.left, p, q)
        # both values are greater than root value so check in right subtree
        else:
            ancestor = self.lowest_common_ancestor_recursion(root.right, p, q)
        return ancestor

    def lowest_common_ancestor_iteration(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: O(1).  No additional data structures.
        """
        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)
        # Start from the root node of the tree
        curr_node = root
        # Traverse the tree in DFS manner
        while curr_node:
            # both values are less than root value so check in left subtree
            if min_val < curr_node.val and max_val < curr_node.val:
                curr_node = curr_node.left
            # both values are greater than root value so check in right subtree
            elif min_val > curr_node.val and max_val > curr_node.val:
                curr_node = curr_node.right
            else:
                # We have found the LCA node.
                return curr_node
