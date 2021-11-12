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

# 637. Average of Levels in Binary Tree  https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
# Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def average_of_levels(self, root: Optional[TreeNode]) -> List[float]:
        """ Time complexity: O(N). We check / visit every node
            Space complexity: O(N). We have to keep leafs in case of balanced tree.
        """
        # empty tree
        if not root:
            return []

        # use Breadth First Search traversal
        queue = [(root, 1)]
        curr_depth = 1
        curr_sum = 0
        curr_count = 0
        result = list()
        while queue:
            # get and handle node
            node, node_depth = queue.pop(0)
            # if we are on the new level of tree, reset accumulators and set new current depth
            if node_depth != curr_depth:
                result.append(float(curr_sum / curr_count))
                curr_depth = node_depth
                curr_sum = 0
                curr_count = 0

            # increase accumulators
            curr_sum += node.val
            curr_count += 1

            # add the children to queue to handle
            if node.left:
                queue.append((node.left, node_depth + 1))
            if node.right:
                queue.append((node.right, node_depth + 1))

            # if queue becomes empty, we have to save current results
            if not queue:
                result.append(float(curr_sum / curr_count))

        return result
