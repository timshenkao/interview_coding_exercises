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

# 143. Reorder List https://leetcode.com/problems/reorder-list/
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """ Time complexity: O(n)
            Space complexity: O(n)
        """
        if head:
            arr = []
            # put all nodes into array
            while head:
                arr += head
                head = head.next
            l, r, prev = 0, len(arr) - 1, ListNode(0)
            while l < r:
                prev.next, arr[l].next, prev, l, r = arr[l], arr[r], arr[r], l + 1, r - 1
            if l == r:
                prev.next = arr[l]
            arr[l].next = None

    def reorderList2(self, head: ListNode) -> None:
        """ Time complexity: O(n)
            Space complexity: O(1)
        """
        # use slow and fast pointer to reach the middle and end in O(n)
        # we actually need slow pointer later
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # pointer in the beginning of the 2nd half
        head_fast = slow.next
        # disconnect first half from second half
        slow.next = None

        # invert second half in O(n)
        prev = None
        while head_fast:
            tmp = head_fast.next
            head_fast.next = prev
            prev = head_fast
            head_fast = tmp

        # pointers to the heads of halves
        first, second = head, prev
        # merge 2 halves in O(n)
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
