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

# 173. Binary Search Tree Iterator https://leetcode.com/problems/binary-search-tree-iterator/description/
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part
#        of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the
#       BST.
#    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
#       otherwise returns false.
#    int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the
# smallest element in the BST.
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the
# in-order traversal when next() is called.
# # The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext, and next.
# Follow up: Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory,
# where h is the height of the tree?


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.push_all(root)

    def next(self) -> int:
        cur = self.stack.pop()
        self.push_all(cur.right)
        return cur.val

    def hasNext(self):
        return self.stack

    def push_all(self, node):
        while node:
            self.stack += (node,)
            node = node.left


class BSTIterator2:
    """ Recursive
     Time complexity: Constructor: O(n), next(): O(1), hasNext(): O(1).
     Space complexity: O(n).
    """
    def __init__(self, root):
        self.i = 0
        self.vals = []
        self._inorder(root)

    def next(self) -> int:
        self.i += 1
        return self.vals[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.vals)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.vals.append(root.val)
        self._inorder(root.right)


class BSTIterator3:
    """ Iterative
     Time complexity:
        Constructor: O(h)
         next(): O(h)  Amortized O(1) average per call, since across all next() calls (up to n), each node is pushed
            and popped exactly once, totaling O(n) work. Worst-case per next() is O(h) if pushing a deep left subtree.
         hasNext(): O(1).
     Space complexity: O(h).
    """
    def __init__(self, root):
        self.stack = []
        self._pushLeftsUntilNull(root)

    def next(self) -> int:
        root = self.stack.pop()
        self._pushLeftsUntilNull(root.right)
        return root.val

    def hasNext(self):
        return self.stack

    def _pushLeftsUntilNull(self, root):
        while root:
            self.stack.append(root)
            root = root.left
