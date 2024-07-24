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

import collections

# 341. Flatten Nested List Iterator https://leetcode.com/problems/flatten-nested-list-iterator/description/
# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may
# also be integers or other lists. Implement an iterator to flatten it.
# Implement the NestedIterator class:
#       NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
#       int next() Returns the next integer in the nested list.
#       boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be judged as correct.
# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-10^6, 10^6].


class NestedIteratorDeque:
    """ Time complexity: O(n)
        Space complexity: O(n)
        Recursive approach
    """
    def __init__(self, nestedList: List[NestedInteger]):
        self.q = collections.deque()
        self.addInteger(nestedList)

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return self.q

    def addInteger(self, nestedList: List[NestedInteger]) -> None:
        for ni in nestedList:
            if ni.isInteger():
                self.q.append(ni.getInteger())
            else:
                self.addInteger(ni.getList())


class NestedIteratorStack:
    """ Time complexity: O(n)
        Space complexity: O(n)
    """
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack: List[NestedInteger] = []
        self.addInteger(nestedList)

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            self.addInteger(self.stack.pop().getList())
        return self.stack

    def addInteger(self, nestedList: List[NestedInteger]) -> None:
        for n in reversed(nestedList):
            self.stack.append(n)
