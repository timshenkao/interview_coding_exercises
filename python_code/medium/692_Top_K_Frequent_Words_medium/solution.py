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

class Solution:
    def topKFrequent(self, words, k):
        return [w for w, v in sorted(collections.Counter(words).items(), key = lambda x: (-x[1], x[0])) [:k]]


Approach 1: Bucket Sort¶
Time: O(n)
Space: O(n)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        bucket = [[] for _ in range(len(words) + 1)]

        for word, freq in collections.Counter(words).items():
            bucket[freq].append(word)

        for b in reversed(bucket):
            for word in sorted(b):
                ans.append(word)
                if len(ans) == k:
                    return ans

Approach 2: Follow up¶
Time: O(nlogk)
Space: O(nlogk)


class T:
    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            # Words with higher frequency and lower alphabetical order are in the
            # bottom of the heap because we'll pop words with lower frequency and
            # higher alphabetical order if the heap's size > k.
            return self.word > other.word
        return self.freq < other.freq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        heap = []

        for word, freq in collections.Counter(words).items():
            heapq.heappush(heap, T(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            ans.append(heapq.heappop(heap).word)

        return ans[::-1]