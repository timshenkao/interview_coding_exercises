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
    def connect(self, root: "Node") -> "Node":
        if root == None:
            return root
        q, prev = [(root, 1)], None
        while q:
            curr, pos = q.pop(0)
            if prev != None and prev[1] == pos:
                prev[0].next = curr
            prev = [curr, pos]
            if curr.left:
                q.append((curr.left, pos + 1))
            if curr.right:
                q.append((curr.right, pos + 1))
        return root


Approach 1: Recursive¶
Time: O(n)
Space: O(h)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def connectTwoNodes(p, q) -> None:
            if not p:
                return
            p.next = q
            connectTwoNodes(p.left, p.right)
            connectTwoNodes(q.left, q.right)
            connectTwoNodes(p.right, q.left)

        connectTwoNodes(root.left, root.right)
        return root

Approach 2: Iterative¶
Time: O(n)
Space: O(1)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root  # the node that is above the current needling

        while node and node.left:
            dummy = Node(0)  # a dummy node before needling
            # Needle the children of the node.
            needle = dummy
            while node:
                needle.next = node.left
                needle = needle.next
                needle.next = node.right
                needle = needle.next
                node = node.next
            node = dummy.next  # Move the node to the next level.

        return root