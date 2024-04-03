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
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic, start, end = {}, 0, 0
        for end in range(1, len(s)+1):
            if not s[end-1] in dic: dic[s[end-1]] = 1
            else: dic[s[end-1]] += 1
            if end-start-max(dic.values()) > k:
                dic[s[start]] -= 1
                start += 1
        return end-start

Approach 1: Regular Window¶
Time:
�
(
    �
)
O(n)
Space:
�
(
    26
)
=
�
(
    1
)
O(26)=O(1)

C++
Java
Python

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        maxCount = 0
        count = collections.Counter()

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            maxCount = max(maxCount, count[c])
            while maxCount + k < r - l + 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

Approach 2: Lazy Window¶
Time:
�
(
    �
)
O(n)
Space:
�
(
    26
)
=
�
(
    1
)
O(26)=O(1)

C++
Java
Python

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0
        count = collections.Counter()

        # l and r track the maximum window instead of the valid window.
        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            maxCount = max(maxCount, count[c])
            while maxCount + k < r - l + 1:
                count[s[l]] -= 1
                l += 1

        return r - l + 1