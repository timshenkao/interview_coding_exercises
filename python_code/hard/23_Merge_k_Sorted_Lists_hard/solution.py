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

from queue import PriorityQueue

from python_code.helper.linked_lists import ListNode
from python_code.helper.linked_lists import generate_list, print_list

# 23. Merge k Sorted Lists https://leetcode.com/problems/merge-k-sorted-lists/
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4


class Solution:
    def merge_k_lists(self, lists):
        """ Time complexity: O(nlogk).
            Space complexity: O(k).
        """
        dummy = ListNode(0)
        curr = dummy
        pq = PriorityQueue()
        # [print_list(l) for l in lists ]
        for i, lst in enumerate(lists):
            # print_list(lst)
            if lst:
                pq.put((lst.val, i, lst))

        while not pq.empty():
            _, i, min_node = pq.get()
            if min_node.next_node:
                pq.put((min_node.next_node.val, i, min_node.next_node))
            curr.next_node = min_node
            curr = curr.next_node
        return dummy.next_node
