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

import collections

# 102. Binary Tree Level Order Traversal https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
# level by level).
#The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder_bfs(self, root):
        """ Time complexity: O(n)
            Space complexity: O(n)
        """
        q, res = [root], []
        while any(q):
            res.append([i.val for i in q])
            q = [child for node in q for child in (node.left, node.right) if child]
        return res

    def levelOrder_bfs2(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ Time complexity: O(n)
            Space complexity: O(n)
        """
        if not root:
            return []
        ans = []
        q = collections.deque([root])
        while q:
            currLevel = []
            for _ in range(len(q)):
                node = q.popleft()
                currLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(currLevel)
        return ans
