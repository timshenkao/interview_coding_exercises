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


# 155. Min Stack  https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 10^4 calls will be made to push, pop, top, and getMin.


class MyStack:
    """ Time complexity: top() --> O(1).
                         get_min() --> O(1).
                         pop() --> O(1).
                         push() --> O(1).
        Space complexity: O(N). We keep additional list.
    """
    def __init__(self):
        self._stack = list()
        self._stack_of_mins = list()

    def push(self, x: int) -> None:
        self._stack.append(x)
        # If stack of mins is empty, or current number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if (not self._stack_of_mins) or (x < self._stack_of_mins[-1][0]):
            self._stack_of_mins.append([x, 1])
        # current number is equal to top of stack of mins; increment the count at the top by 1.
        elif x == self._stack_of_mins[-1][0]:
            self._stack_of_mins[-1][1] += 1

    def pop(self) -> int:
        if self._stack_of_mins[-1][0] == self._stack[-1]:
            self._stack_of_mins[-1][1] -= 1

        # If the count at the top of stack of mins is 0
        if self._stack_of_mins[-1][1] == 0:
            self._stack_of_mins.pop()
        return self._stack.pop()

    def get_min(self) -> int:
        return self._stack_of_mins[-1][0]

    def top(self) -> int:
        return self._stack[-1]
