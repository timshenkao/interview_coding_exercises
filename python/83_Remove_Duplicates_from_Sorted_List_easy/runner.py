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
from solution import Solution, ListNode


def main():
    solution = Solution()

    e1 = ListNode(3, None)
    e2 = ListNode(3, e1)
    e3 = ListNode(2, e2)
    e4 = ListNode(1, e3)
    head = ListNode(1, e4)
    head2 = solution.delete_duplicates(head)

    while head2.next_node:
        print('node: ', head2, '; value: ', head2.val, '; next node: ', head2.next_node)
        head2 = head2.next_node
    print('node: ', head2, '; value: ', head2.val, '; next node: ', head2.next_node)


if __name__ == '__main__':
    main()
