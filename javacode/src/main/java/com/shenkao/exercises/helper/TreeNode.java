/* Copyright (c) 2021 - present, Timur Shenkao
* All rights reserved.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

package com.shenkao.exercises.helper;


public class TreeNode {
    public Integer val;
    public TreeNode left;
    public TreeNode right;

    TreeNode(int x, TreeNode leftNode, TreeNode rightNode) {
        val = x;
        left = leftNode;
        right = rightNode;
    }

    TreeNode(int x, TreeNode leftNode) {
        this(x, leftNode, null);
    }
    TreeNode(int x) {
        this(x, null);
    }

    TreeNode() {
        this(0);
    }
}
