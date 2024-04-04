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

class Codec:

    def encode(self, strs):
        return "".join(str(len(s)) + ":" + s for s in strs)

    def decode(self, s):
        strs = []
        while s:
            i = s.find(":")
            length = int(s[:i])
            s = s[i+1:]
            strs.append(s[:length])
            s = s[length:]
        return strs

Time: O(n)
Space: O(n)



class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        return "".join(str(len(s)) + '/' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []

        i = 0
        while i < len(s):
            slash = s.find('/', i)
            length = int(s[i:slash])
            i = slash + length + 1
            decoded.append(s[slash + 1:i])

        return decoded