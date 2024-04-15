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

from solution import LRUCache, LRUCache2


def main():
    tests = {
        1: [
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        ],
        2: [
            ["LRUCache2", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        ]

    }
    for _, test in tests.items():
        print("instructions: ", test[0])
        print("inputs: ", test[1])
        cache_class = globals()[test[0][0]]
        cache = cache_class(*test[1][0])
        print(cache.__dict__)
        print(" ")

        for i in range(1, len(test[0])):
            print("instruction ", test[0][i])
            print("inputs ", test[1][i])
            func = getattr(cache, test[0][i])
            result = func(*test[1][i])
            print("cache ", cache.dic)
            print("result ", result)
            print(" ")

        print(" ")


if __name__ == "__main__":
    main()
