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



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

Time: Constructor: O(Σ∣sentences[i]∣), input(c: chr): O(1)
Space: O(Σ∣sentences[i]∣)


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.s: Optional[str] = None
        self.time = 0
        self.top3: List[TrieNode] = []

    def __lt__(self, other):
        if self.time == other.time:
            return self.s < other.s
        return self.time > other.time

    def update(self, node) -> None:
        if node not in self.top3:
            self.top3.append(node)
        self.top3.sort()
        if len(self.top3) > 3:
            self.top3.pop()


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr = self.root
        self.s: List[chr] = []

        for sentence, time in zip(sentences, times):
            self._insert(sentence, time)

    def input(self, c: str) -> List[str]:
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
        return [node.s for node in self.curr.top3]

    def _insert(self, sentence: str, time: int) -> None:
        node = self.root
        for c in sentence:
            node = node.children.setdefault(c, TrieNode())
        node.s = sentence
        node.time += time

        leaf = node
        node: TrieNode = self.root
        for c in sentence:
            node = node.children[c]
            node.update(leaf)