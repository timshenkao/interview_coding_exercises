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

# 653. Two Sum IV - Input is a BST  https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST
# such that their sum is equal to the given target.
# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105


class Solution:
    def _get_list(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        else:
            return self._get_list(node.left) + [node.val] + self._get_list(node.right)



    def find_target(self, root: Optional[TreeNode], k: int) -> bool:
        """ Time complexity: O(N). We check / visit every node during sorted array creation and iterate
                             through sorted array.
            Space complexity: O(n). We create sorted array of elements. We also use recursion during sorted array
                              creation. if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree or O(N) in case of unbalanced tree.
        """
        sorted_array = self._get_list(root)
        # use left and right pointers
        left = 0
        right = len(sorted_array) - 1
        while left < right:
            if (sorted_array[left] + sorted_array[right]) == k:
                return True
            elif (sorted_array[left] + sorted_array[right]) > k:
                right -= 1
            elif (sorted_array[left] + sorted_array[right]) < k:
                left += 1
        return False
