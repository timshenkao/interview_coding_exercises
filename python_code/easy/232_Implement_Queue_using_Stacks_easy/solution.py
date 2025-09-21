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

from typing import List

# 232. Implement Queue using Stacks    https://leetcode.com/problems/implement-queue-using-stacks/
# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
#     void push(int x) Pushes element x to the back of the queue.
#     int pop() Removes the element from the front of the queue and returns it.
#     int peek() Returns the element at the front of the queue.
#     boolean empty() Returns true if the queue is empty, false otherwise.
#
# Notes:
#     You must use only standard operations of a stack, which means only push to top, peek/pop from top, size,
#     and is empty operations are valid.
#     Depending on your language, the stack may not be supported natively. You may simulate a stack using a list
#     or deque (double-ended queue) as long as you use only a stack's standard operations.
# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
# In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.


class MyQueue:
    """ Time complexity: peek() --> O(1).
                         empty() --> O(1).
                         pop() --> O(N). Not amortized
                         push() --> O(N). Not amortized
        Space complexity: O(N). We use two lists as stacks.
    """
    def __init__(self):
        self._size = 0
        self._stack = list()
        self._reversed_stack = list()

    def _move_stack_to_stack(self, stack1: List[int], stack2: List[int]):
        while stack1:
            popped = stack1.pop()
            stack2.append(popped)

    def push(self, x: int) -> None:
        # populate 1st stack
        self._stack.append(x)

        temp = list()
        # move elements to temp stack in reverse order
        self._move_stack_to_stack(self._reversed_stack, temp)
        # reversed stack is empty now, push element
        self._reversed_stack.append(x)
        # move elements from temp stack to reversed stack
        self._move_stack_to_stack(temp, self._reversed_stack)
        self._size += 1

    def pop(self) -> int:
        # remove element from 1st stack
        temp = list()
        # move elements to temp stack in reverse order
        self._move_stack_to_stack(self._stack, temp)
        # "remove element"
        temp.pop()
        # move elements from temp stack to stack
        self._move_stack_to_stack(temp, self._stack)
        self._size -= 1
        return self._reversed_stack.pop()

    def peek(self) -> int:
        temp = self._reversed_stack.pop()
        self._reversed_stack.append(temp)
        return temp

    def empty(self) -> bool:
        return self._size == 0


class MyQueue2:
    """ Time complexity: peek() --> O(1). Amortized. Worst: O(N)
                         empty() --> O(1).
                         pop() --> O(1). Amortized. Worst: O(N)
                         push() --> O(1).
        Space complexity: O(N). We use two lists as stacks.
        Amortized O(1) is achieved because the costly transfer is spread over multiple pop/peek operations
    """
    def __init__(self):
        self._stack = list()
        self._reversed_stack = list()

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        if not self._reversed_stack:
            self._transfer()
        return self._reversed_stack.pop()

    def peek(self) -> int:
        if not self._reversed_stack:
            self._transfer()
        return self._reversed_stack[-1]

    def empty(self) -> bool:
        return not self._stack and not self._reversed_stack

    def _transfer(self):
        # TC: O(N)
        while self._stack:
            self._reversed_stack.append(self._stack.pop())
