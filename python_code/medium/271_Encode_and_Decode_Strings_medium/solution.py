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

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is
# decoded back to the original list of strings.
# Machine 1 (sender) has the function:
#   string encode(vector<string> strs) {
#       // ... your code
#       return encoded_string;
#   }
# Machine 2 (receiver) has the function:
    # vector<string> decode(string s) {
#       //... your code
#       return strs;
#   }
# So Machine 1 does:
# string encoded_string = encode(strs);
# and Machine 2 does:
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
# Implement the encode and decode methods.
# You are not allowed to solve the problem using any serialize methods (such as eval).
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.


class Codec:
    def encode1(self, strs):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        return "".join(str(len(s)) + ":" + s for s in strs)

    def decode1(self, s):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        strs = []
        while s:
            i = s.find(":")
            length = int(s[:i])
            s = s[i+1:]
            strs.append(s[:length])
            s = s[length:]
        return strs

    def encode2(self, strs):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        return "".join(str(len(s)) + '/' + s for s in strs)

    def decode2(self, s):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        decoded = []
        i = 0
        while i < len(s):
            slash = s.find('/', i)
            length = int(s[i:slash])
            i = slash + length + 1
            decoded.append(s[slash + 1:i])
        return decoded
