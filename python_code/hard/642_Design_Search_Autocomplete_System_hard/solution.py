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
import heapq
from typing import List


# 642. Design Search Autocomplete System https://leetcode.com/problems/design-search-autocomplete-system/
# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a
# special character '#').
# You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously
# typed sentence and times[i] is the corresponding number of times the sentence was typed.
# For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part
# of the sentence already typed.
# Here are the specific rules:
#       The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
#       The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several
#       sentences have the same hot degree, use ASCII-code order (smaller one appears first).
#       If less than 3 hot sentences exist, return as many as you can.
#       When the input is a special character, it means the sentence ends, and in this case, you need to return an empty
#       list.
# Implement the AutocompleteSystem class:
# AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
# List<String> input(char c) This indicates that the user typed the character c.
#       Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
#       Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.
#       If there are fewer than 3 matches, return them all.
# n == sentences.length
# n == times.length
# 1 <= n <= 100
# 1 <= sentences[i].length <= 100
# 1 <= times[i] <= 50
# c is a lowercase English letter, a hash '#', or space ' '.
# Each tested sentence will be a sequence of characters c that end with the character '#'.
# Each tested sentence will have a length in the range [1, 200].
# The words in each input sentence are separated by single spaces.
# At most 5000 calls will be made to input.


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.cur = self.root = {}
        self.rank = collections.defaultdict(int)
        for i, s in enumerate(sentences):
            self.s = s
            self.rank[s] = times[i] - 1
            self.input("#")

    def move(self, c):
        if c not in self.cur:
            self.cur[c] = {}
        self.cur = self.cur[c]
        if "sentences" not in self.cur:
            self.cur["sentences"] = []

    def addSentence(self):
        self.cur = self.root
        for c in self.s:
            self.move(c)
            self.search()
            heapq.heappush(self.cur["sentences"], [-self.rank[self.s], self.s])

    def search(self):
        q, used, i = [], set(), 0
        while i < 3 and self.cur["sentences"]:
            r, s = heapq.heappop(self.cur["sentences"])
            if s not in used:
                used.add(s)
                q.append([r, s])
                i += 1
        for r, s in q:
            heapq.heappush(self.cur["sentences"], [r, s])
        return [s for r, s in q]

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.rank[self.s] += 1
            self.addSentence()
            self.s = ""
            self.cur = self.root
            return []
        else:
            self.s += c
            self.move(c)
            return self.search()

#############


class TrieNode:
    def __init__(self):
        self.children = {}
        self.s = None
        self.time = 0
        self.top3 = []

    def __lt__(self, other):
        if self.time == other.time:
            return self.s < other.s
        return self.time > other.time

    def update(self, node):
        if node not in self.top3:
            self.top3.append(node)
        self.top3.sort()
        if len(self.top3) > 3:
            self.top3.pop()


class AutocompleteSystemTrie:
    """ Time complexity: Constructor: O(sum of lengths ∣sentences[i]∣), input(c): O(1)
        Space complexity: O(sum of lengths ∣sentences[i]∣)
    """
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr = self.root
        self.s = []
        for sentence, time in zip(sentences, times):
            self._insert(sentence, time)

    def input(self, c):
        if c == "#":
            self._insert("".join(self.s), 1)
            self.curr = self.root
            self.s = []
            return []
        self.s.append(c)
        if self.curr:
            self.curr = self.curr.children.get(c, None)
        if not self.curr:
            return []
        return [node.s for node in self.curr.top3]  # O(3)

    def _insert(self, sentence, time):
        node = self.root
        for c in sentence:
            node = node.children.setdefault(c, TrieNode())
        node.s = sentence
        node.time += time

        leaf = node
        node = self.root
        for c in sentence:
            node = node.children[c]
            node.update(leaf)
