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


# 997. Find the Town Judge  https://leetcode.com/problems/find-the-town-judge/
# In a town, there are n people labeled from 1 to n.
# There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that
# the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

class Solution:
    def find_judge(self, n: int, trust: List[List[int]]) -> int:
        """ Time complexity: O(n^2). In the worst case scenario, there could be O(n^2) elements in trust array.
            Space complexity: O(n). We keep 2 counts per each person.
        """
        # not enough data; there is no person who is trusted by everyone
        if len(trust) < n - 1:
            return -1

        # create map:
        # key --> person's label
        # value --> 2-element list.
        #           First element denotes how many people this person trusts
        #           Second element denotes how many people trust this person
        # trust_relation = dict.fromkeys([x for x in range(1, n + 1)], [0, 0])
        trust_relation = dict()
        for x in range(1, n + 1):
            trust_relation.setdefault(x, [0, 0])

        # iterate through trust list and populate map
        for elem in trust:
            trust_relation[elem[0]][0] += 1
            trust_relation[elem[1]][1] += 1

        # find judge
        possible_judges = []
        for k, v in trust_relation.items():
            # person doesn't trust anyone and person is trusted by everyone else
            if v[0] == 0 and v[1] == n - 1:
                possible_judges.append(k)
        if len(possible_judges) == 1:
            return possible_judges.pop()
        return -1

    def find_judge_one_array(self, n: int, trust: List[List[int]]) -> int:
        """ Time complexity: O(n^2). In the worst case scenario, there could be O(n^2) elements in trust array.
            Space complexity: O(n). We keep 1 count per each person.
        """
        # not enough data; there is no person who is trusted by everyone
        if len(trust) < n - 1:
            return -1

        trust_scores = [0] * n
        # each person gets 1 "point" if he /she is trusted by another person
        # each person loses 1 "point" if he /she trusts another person.
        # town judge, if he / she exist, must be the person with n - 1 "points".
        for a, b in trust:
            trust_scores[a - 1] -= 1
            trust_scores[b - 1] += 1

        for i in range(len(trust_scores)):
            if trust_scores[i] == n - 1:
                return i + 1
        return -1
