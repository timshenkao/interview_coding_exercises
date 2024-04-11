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

# 139. Word Break  https://leetcode.com/problems/word-break/
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


class Solution:
    def word_break(self, s, word_dict):
        """ Time complexity: O(n^3).
            Space complexity: O(n^2 +Σ∣wordDict[i]∣).
        """
        rightmosts, words = [0], set(word_dict)
        for i in range(1, len(s) + 1):
            for last_index in rightmosts:
                if s[last_index:i] in words:
                    rightmosts.append(i)
                    if i == len(s):
                        return True
                    break
        return False

    def word_break2(self, s, word_dict):
        """ Time complexity: O(n^3).
            Space complexity: O(n^2 +Σ∣wordDict[i]∣).
        """
        import functools
        @functools.lru_cache(None)
        def _word_break(s: str) -> bool:
            if s in wordSet:
                return True
            return any(s[:i] in wordSet and _word_break(s[i:]) for i in range(len(s)))

        wordSet = set(word_dict)
        return _word_break(s)

    def word_break3(self, s, word_dict):
        """ Time complexity: O(n^3).
            Space complexity: O(n^2 +Σ∣wordDict[i]∣).
        """
        import functools
        @functools.lru_cache(None)
        def wordBreak(i: int) -> bool:
            """Returns True if s[i..n) can be segmented."""
            if i == len(s):
                return True
            return any(s[i:j] in wordSet and wordBreak(j) for j in range(i + 1, len(s) + 1))
        wordSet = set(word_dict)
        return wordBreak(0)

    def word_break4(self, s, word_dict):
        """ Time complexity: O(n^3).
            Space complexity: O(n^2 +Σ∣wordDict[i]∣).
        """
        n = len(s)
        wordSet = set(word_dict)
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

    def word_break5(self, s, word_dict):
        """ Time complexity: O(n^3).
            Space complexity: O(n^2 +Σ∣wordDict[i]∣).
        """
        n = len(s)
        maxLength = len(max(word_dict, key=len))
        wordSet = set(word_dict)
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
