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

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def move(self, word, mod):
        cur = self.root
        for c in word:
            if c not in cur:
                if mod != 1:
                    return False
                cur[c] = {}
            cur = cur[c]
        if mod == 1:
            cur['#'] = None
        else:
            return mod == 3 or '#' in cur

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        return self.move(word, 1)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.move(word, 2)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.move(prefix, 3)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


Time:
Space:

C++
Java
Python

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node: TrieNode = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.isWord = True

    def search(self, word: str) -> bool:
        node: TrieNode = self._find(word)
        return node and node.isWord

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix)

    def _find(self, prefix: str) -> Optional[TrieNode]:
        node: TrieNode = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node