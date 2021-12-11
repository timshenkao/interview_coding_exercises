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

# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
# binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by
# more than one.
# 1 <= nums.length <= 10 ^ 4
# -10 ^ 4 <= nums[i] <= 10 ^ 4
# nums is sorted in a strictly increasing order.


class Solution:
    def sorted_array_to_BST_preorder(self, nums: List[int]) -> Optional[TreeNode]:
        """ Time complexity: O(N). We check / visit every node. DFS PREORDER traversal without explicit stack.
            Space complexity: if we don't count recursion stack then O(1).
                              Else O(log N) in case of balanced tree.
            Height-balanced restriction means that at each step one has to pick up the number in the middle as a root.
            That works fine with arrays containing odd number of elements but there is no predefined choice for arrays
            with even number of elements.
        """
        # empty array
        if not nums:
            return None

        left = 0
        right = len(nums) - 1
        middle = left + (right - left) // 2
        root = TreeNode(nums[middle], self.sorted_array_to_BST_preorder(nums[: middle]),
                        self.sorted_array_to_BST_preorder(nums[middle + 1: right + 1]))
        return root
