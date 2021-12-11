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

# 270. Closest Binary Search Tree Value https://leetcode.com/problems/closest-binary-search-tree-value/
# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
# The number of nodes in the tree is in the range [1, 10 ^ 4].
# 0 <= Node.val <= 10 ^ 9
# -10 ^ 9 <= target <= 10 ^ 9


class Solution:
    def closest_value_inorder_traversal(self, root: Optional[TreeNode], target: float) -> int:
        """ Time complexity: O(N). We check / visit every node.
            Space complexity: O(N). We create array to keep sorted values.
        """
        def inorder(node: TreeNode) -> List[int]:
            """Create inorder traversal sorted array."""
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        # take element from sorted array
        return min(inorder(root), key=lambda x: abs(target - x))

    def closest_value(self, root: Optional[TreeNode], target: float) -> int:
        """ Time complexity: O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
            Space complexity: O(1).
        """
        closest = root.val
        # modification of binary search
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
