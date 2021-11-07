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

# 937. Reorder Data in Log Files  https://leetcode.com/problems/reorder-data-in-log-files/
# You are given an array of logs.
# Each log is a space-delimited string of words, where the first word is the identifier.
# There are two types of logs:
#     Letter-logs: All words (except the identifier) consist of lowercase English letters.
#     Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:
#     The letter-logs come before all digit-logs.
#     The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them
#     lexicographically by their identifiers.
#     The digit-logs maintain their relative ordering.
# Return the final order of the logs.


# Let N be the number of logs in the list and M be the maximum length of a single log.
# Time complexity: O(M * N * log N).
# The sorted() in Python is implemented with the Timsort algorithm which time complexity is O(N * log N).
# Comparison between two log keys can take up to O(M) time. The overall time complexity of the algorithm is
# O(M * N * log N).
#
# Space complexity: O(M * N).
# We need O(M * N) space to keep the log keys.
# In addition, the worst space complexity of the Timsort algorithm is O(N), assuming that the space required
# for each element is O(1). So, we would need O(M * N) space to hold the intermediate values for sorting.
# In total, the overall space complexity of the algorithm is O(M * N + M * N) = O(M * N)


class Solution:
    def reorder_log_files_comparator(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.comparator)

    def reorder_log_files_comparator2(self, logs: List[str]) -> List[str]:
        let_logs, dig_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                let_logs.append(log)
            else:
                dig_logs.append(log)
        let_logs.sort(key=self.comparator2)
        return let_logs + dig_logs

    def comparator(self, log: str) -> tuple:
        label, body = log.split(' ', maxsplit=1)
        return (0, body, label) if body[0].isalpha() else (1, )

    def comparator2(self, log: str) -> str:
        words = log.split()
        label, body = words[0], words[1:]
        return ' '.join(body + [' ', label])
