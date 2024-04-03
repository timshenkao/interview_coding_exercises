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
    def countComponents(self, n, edges):
        visited, res, adj = set(), 0, collections.defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        def dfs(i):
            visited.add(i)
            for v in adj[i]:
                if v not in visited:
                    dfs(v)
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res

    Approach 1: BFS
    Time:     O(∣V∣+∣E∣)
    Space:     O(∣V∣+∣E∣)


    class Solution:
        def countComponents(self, n: int, edges: List[List[int]]) -> int:
            ans = 0
            graph = [[] for _ in range(n)]
            seen = set()

            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            def bfs(node: int, seen: Set[int]) -> None:
                q = collections.deque([node])
                seen.add(node)

                while q:
                    u = q.pop()
                    for v in graph[u]:
                        if v not in seen:
                            q.append(v)
                            seen.add(v)

            for i in range(n):
                if i not in seen:
                    bfs(i, seen)
                    ans += 1

            return ans


Approach 2: DFS
Time: O(∣V∣+∣E∣)
Space: O(∣V∣+∣E∣)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        graph = [[] for _ in range(n)]
        seen = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u: int, seen: Set[int]) -> None:
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    dfs(v, seen)

        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(graph, i, seen)
                ans += 1

        return ans

Approach 3: UF
Time: O(∣V∣+∣E∣)
Space: O(∣V∣+∣E∣)

class UnionFind:
    def __init__(self, n: int):
        self.count = n
        self.id = list(range(n))
        self.rank = [0] * n

    def unionByRank(self, u: int, v: int) -> None:
        i = self._find(u)
        j = self._find(v)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.id[i] = j
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i
        else:
            self.id[i] = j
            self.rank[j] += 1
        self.count -= 1

    def _find(self, u: int) -> int:
        if self.id[u] != u:
            self.id[u] = self._find(self.id[u])
        return self.id[u]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v in edges:
            uf.unionByRank(u, v)

        return uf.count

    
