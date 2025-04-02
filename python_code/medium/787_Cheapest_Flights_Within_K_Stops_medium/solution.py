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


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        flight = collections.defaultdict(list)
        for s, e, p in flights:
            flight[s].append((e, p))
        heap = [(0, src, K + 1)]
        while heap:
            price, city, stop = heapq.heappop(heap)
            if city == dst:
                return price
            elif stop > 0:
                for c, p in flight[city]:
                    heapq.heappush(heap, (price + p, c, stop - 1))
        return -1

    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """ Time complexity: O((∣V∣+∣E∣)log∣V∣)
            Space complexity: O(∣E∣+∣V∣)
        """
        graph = [[] for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))

        return self._dijkstra(graph, src, dst, k)

    def _dijkstra(self, graph: List[List[Tuple[int, int]]], src: int, dst: int, k: int) -> int:
        dist = [[math.inf for _ in range(k + 2)] for _ in range(len(graph))]

        dist[src][k + 1] = 0
        minHeap = [(dist[src][k + 1], src, k + 1)]  # (d, u, stops)

        while minHeap:
            d, u, stops = heapq.heappop(minHeap)
            if u == dst:
                return d
            if stops == 0:
                continue
            for v, w in graph[u]:
                if d + w < dist[v][stops - 1]:
                    dist[v][stops - 1] = d + w
                    heapq.heappush(minHeap, (dist[v][stops - 1], v, stops - 1))

        return -1
