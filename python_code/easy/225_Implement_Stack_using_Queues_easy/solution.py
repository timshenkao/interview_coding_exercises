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


# 225. Implement Stack using Queues  https://leetcode.com/problems/implement-stack-using-queues/
# Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:
#     void push(int x) Pushes element x to the top of the stack.
#     int pop() Removes the element on the top of the stack and returns it.
#     int top() Returns the element on the top of the stack.
#     boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
#     You must use only standard operations of a queue, which means that only push to back, peek/pop from front,
#     size and is empty operations are valid.
#     Depending on your language, the queue may not be supported natively.
#     You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard
#     operations.

# Follow-up: Can you implement the stack using only one queue?


class MyStack:
    """ Time complexity: top() --> O(1).
                         empty() --> O(1).
                         pop() --> O(1).
                         push() --> O(N).
        Space complexity: O(N). We use 1 list as queue.
    """
    def __init__(self):
        self._size = 0
        self._queue = list()

    def push(self, x: int) -> None:
        orig_size = len(self._queue)
        self._queue.append(x)
        while orig_size:
            self._queue.append(self._queue.pop(0))
            orig_size -= 1
        self._size += 1

    def pop(self) -> int:
        self._size -= 1
        return self._queue.pop(0)

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return self._size == 0
