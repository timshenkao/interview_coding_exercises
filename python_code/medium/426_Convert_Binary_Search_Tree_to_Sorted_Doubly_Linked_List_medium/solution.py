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
    def treeToDoublyList(self, root):
        head, tail = [None], [None]
        def dfs(node, pre):
            if not node:
                return
            l = dfs(node.left, pre)
            new = Node(node.val, l or pre, None)
            if pre and not l:
                pre.right = new
            elif l:
                l.right = new
            if not pre and not l:
                head[0] = new
            if not tail[0] or node.val > tail[0].val:
                tail[0] = new
            r = dfs(node.right, new)
            return r if r else new
        dfs(root, None)
        if head[0]:
            head[0].left = tail[0]
            tail[0].right = head[0]
        return head[0]

Approach 1: Divide and conquer¶
Time: O(n)
Space: O(h)

Approach 2: Stack¶
Time: O(n)
Space: O(h)