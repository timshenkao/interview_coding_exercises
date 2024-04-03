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

class Solution:
    def maxPathSum(self, root):
        res = [-float("inf")]
        def dfs(node):
            if not node: return -float("inf")
            l, r = dfs(node.left), dfs(node.right)
            mx = max(node.val, l + node.val, r + node.val)
            res[0] = max(res[0], mx, node.val + l + r)
            return mx
        dfs(root)
        return res[0]


DFS
DP
Time: O(n)
Space: O(h)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -math.inf

        def maxPathSumDownFrom(root: Optional[TreeNode]) -> int:
            """
            Returns the maximum path sum starting from the current root, where
            root.val is always included.
            """
            nonlocal ans
            if not root:
                return 0

            l = max(0, maxPathSumDownFrom(root.left))
            r = max(0, maxPathSumDownFrom(root.right))
            ans = max(ans, root.val + l + r)
            return root.val + max(l, r)

        maxPathSumDownFrom(root)
        return ans