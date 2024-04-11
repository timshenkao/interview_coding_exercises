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

# 938. Range Sum of BST https://leetcode.com/problems/range-sum-of-bst/
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes
# with a value in the inclusive range [low, high].
# The number of nodes in the tree is in the range [1, 2 * 10^4].
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# All Node.val are unique.


class Solution:
    def range_sum_bst(self, root, l, r):
        """ Time complexity: O(n). Recursive
            Space complexity: O(h).
        """
        if not root:
            return 0
        if root.val < l:
            return self.range_sum_bst(root.right, l, r)
        if root.val > r:
            return self.range_sum_bst(root.left, l, r)
        return root.val + self.range_sum_bst(root.left, l, r) + self.range_sum_bst(root.right, l, r)
