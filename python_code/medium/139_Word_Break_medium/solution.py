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
    def wordBreak(self, s, wordDict):
        rightmosts, words = [0], set(wordDict)
        for i in range(1, len(s) + 1):
            for last_index in rightmosts:
                if s[last_index:i] in words:
                    rightmosts.append(i)
                    if i == len(s):
                        return True
                    break
        return False


Approach 1: Top-down w/ raw string
Time: O(n^3)
Space: O(n^2 +Σ∣wordDict[i]∣)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        @functools.lru_cache(None)
        def wordBreak(s: str) -> bool:
            if s in wordSet:
                return True
            return any(s[:i] in wordSet and wordBreak(s[i:]) for i in range(len(s)))

        return wordBreak(s)

Approach 2: Top-down w/ index
Time: O(n^3)
Space: O(n^2+Σ∣wordDict[i]∣)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        @functools.lru_cache(None)
        def wordBreak(i: int) -> bool:
            """Returns True if s[i..n) can be segmented."""
            if i == len(s):
                return True
            return any(s[i:j] in wordSet and wordBreak(j) for j in range(i + 1, len(s) + 1))

        return wordBreak(0)

Approach 3: Bottom-up
Time: O(n^3)
Space: O(n^2 +Σ∣wordDict[i]∣)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        # dp[i] := True if s[0..i) can be segmented
        dp = [True] + [False] * n

        for i in range(1, n + 1):
            for j in range(i):
                # s[0..j) can be segmented and s[j..i) is in `wordSet`, so s[0..i) can
                # be segmented.
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]

Approach 4: Bottom-up (optimized)
Time: O(n^3)
Space: O(n^2 +Σ∣wordDict[i]∣)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        maxLength = len(max(wordDict, key=len))
        wordSet = set(wordDict)
        # dp[i] := True if s[0..i) can be segmented
        dp = [True] + [False] * n

        for i in range(1, n + 1):
            for j in reversed(range(i)):
                if i - j > maxLength:
                    break
                # s[0..j) can be segmented and s[j..i) is in the wordSet, so s[0..i)
                # can be segmented.
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]
