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
    def distanceK(self, root, target, K):
        adj, res, visited = collections.defaultdict(list), [], collections.defaultdict(int)
        def dfs(node):
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                dfs(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                dfs(node.right)
        dfs(root)
        def dfs2(node, d):
            if d < K:
                visited[node] = 1
                for v in adj[node]:
                    if not visited[v]:
                        dfs2(v, d + 1)
                visited[node] = 0
            else:
                res.append(node.val)
        dfs2(target, 0)
        return res


Time: O(n)
Space: O(n)
DFS
BFS
