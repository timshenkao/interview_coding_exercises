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

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList):
        def dfs(obj, d): return obj.getInteger() * d if obj.isInteger() else sum(dfs(new, d + 1) for new in obj.getList())
        return sum(dfs(item, 1) for item in nestedList)

Approach 1: BFS
Time: O(n)
Space: O(n)


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        ans = 0
        depth = 0
        q = collections.deque()

        def addIntegers(nestedList: List[NestedInteger]) -> None:
            for ni in nestedList:
                q.append(ni)

        addIntegers(nestedList)

        while q:
            depth += 1
            for _ in range(len(q)):
                ni = q.popleft()
                if ni.isInteger():
                    ans += ni.getInteger() * depth
                else:
                    addIntegers(ni.getList())

        return ans


Approach 2: DFS
Time: O(n)
Space: O(h)


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        ans = 0

        def dfs(nestedList: List[NestedInteger], depth: int) -> None:
            nonlocal ans
            for ni in nestedList:
                if ni.isInteger():
                    ans += ni.getInteger() * depth
                else:
                    dfs(ni.getList(), depth + 1)

        dfs(nestedList, 1)
        return ans