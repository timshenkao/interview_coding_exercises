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

# 204. Count Primes  https://leetcode.com/problems/count-primes/
# Given an integer n, return the number of prime numbers that are strictly less than n.


class Solution:
    def count_primes(self, n: int) -> int:
        """ Time complexity: O(n * log log n). Sieve of Eratosthenes
        https://stackoverflow.com/questions/2582732/time-complexity-of-sieve-of-eratosthenes-algorithm/2582776#2582776
        Outer loop is O(n). Each time we see a prime number, we "cross out" the multiples of it.
        How many times do we cross out for each prime number? That depends on how many multiples of that number are
        lower than n.
                               For 2, we have to cross out n/2 numbers.
                               For 3, we have to cross out n/3 numbers.
                               For 5, we have to cross out n/5 numbers.
                               ...etc for each prime less than n.
        This means that the time complexity of "crossing out" is O(n/2 + n/3 + n/5 + ...+n/ (last prime < n)
        This is bounded by O(log log n)

            Space complexity: O(n).
        """
        # case of 0, 1 and 2
        if n <= 2:
            return 0

        # initialize list of n "marks"
        primes = [True] * n
        # 0 and 1 are not primes
        primes[0] = primes[1] = False

        # If number n is not a prime, it can be factored into two factors a and b: n = a * b
        # a and b can't be both greater than the square root of n, since then the product a * b would be greater
        # than sqrt(n) * sqrt(n) = n. So in any factorization of n, at least one of the factors must be smaller than
        # the square root of n, and if we can't find any factors less than or equal to the square root, n must be a
        # prime.
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # using Python slicing, "cross out" further multiples of i starting from i^2:
                # i^2, i^2+i, i^2+2*i, i^2+3*i, ...
                # Either there is no multiples of i in interval [i, i^2] or they were "crossed out" previously for
                # smaller prime number
                # we make (n - 1 - i * i) // i "cross outs" for such multiples and 1 more "cross out" for number n
                primes[i * i:n:i] = [False] * ((n - 1 - i * i) // i + 1)
        return sum(primes)
