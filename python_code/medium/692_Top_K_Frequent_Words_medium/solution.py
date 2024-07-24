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

# 692. Top K Frequent Words https://leetcode.com/problems/top-k-frequent-words/description/
# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their
# lexicographical order.
# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]


class Solution:
    def topKFrequent(self, words, k):
        """ Time complexity: O(N log N).
            Space complexity: O(N).
        """
        return [w for w, v in sorted(collections.Counter(words).items(), key = lambda x: (-x[1], x[0])) [:k]]


    def topKFrequent_bucket(self, words: List[str], k: int) -> List[str]:
        """ Time complexity: O(N log N).
            Space complexity: O(N log N).
            Bucket Sort approach
        """
        ans = []
        bucket = [[] for _ in range(len(words) + 1)]

        for word, freq in collections.Counter(words).items():
            bucket[freq].append(word)

        for b in reversed(bucket):
            for word in sorted(b): # in worst case, O(N log N)
                ans.append(word)
                if len(ans) == k:
                    return ans

    def topKFrequent_heap(self, words: List[str], k: int) -> List[str]:
        """ Time complexity: O(N log k).
            Space complexity: O(N log k).
        """
        ans = []
        heap = []

        for word, freq in collections.Counter(words).items():
            heapq.heappush(heap, T(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            ans.append(heapq.heappop(heap).word)
        return ans[::-1]


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
