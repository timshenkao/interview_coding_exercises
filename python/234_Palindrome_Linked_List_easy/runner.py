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

    ###########################################################
    e0 = ListNode(1, None)
    e1 = ListNode(2, e0)
    e2 = ListNode(3, e1)
    e3 = ListNode(3, e2)
    e4 = ListNode(2, e3)
    l1 = ListNode(1, e4)
    print(solution.is_palindrome(l1))

    ###########################################################
    e1 = ListNode(1, None)
    e2 = ListNode(2, e1)
    e3 = ListNode(3, e2)
    e4 = ListNode(2, e3)
    l1 = ListNode(1, e4)
    print(solution.is_palindrome(l1))

    ###########################################################
    e0 = ListNode(1, None)
    e1 = ListNode(2, e0)
    e2 = ListNode(4, e1)
    e3 = ListNode(3, e2)
    e4 = ListNode(2, e3)
    l1 = ListNode(1, e4)
    print(solution.is_palindrome(l1))

    ###########################################################
    e1 = ListNode(1, None)
    e2 = ListNode(4, e1)
    e3 = ListNode(3, e2)
    e4 = ListNode(2, e3)
    l1 = ListNode(1, e4)
    print(solution.is_palindrome(l1))

    ###########################################################
    l1 = ListNode(1, None)
    print(solution.is_palindrome(l1))


if __name__ == '__main__':
    main()
