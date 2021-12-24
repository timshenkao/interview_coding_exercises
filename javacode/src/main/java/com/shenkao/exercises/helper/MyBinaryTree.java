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


import java.util.ArrayList;

public class MyBinaryTree {
    private static TreeNode generateBinaryTreeRecursion(ArrayList<Integer> values, TreeNode root, int currentIndex) {
        int length = values.size();
        // create root node for the first call
        if (root == null) {
            root = new TreeNode(values.get(0), null, null);
        }
        // there is value for left child; don't generate node if value is None
        // subtlety: value can be 0
        if ((2 * currentIndex + 1) <= (length - 1) && values.get(2 * currentIndex + 1) != null) {
            root.left = new TreeNode(values.get(2 * currentIndex + 1), null, null);
        }
        // call recursively; if left child has its own children, they will be populated
        generateBinaryTreeRecursion(values, root.left, 2 * currentIndex + 1);
        // there is value for right child; don't generate node if value is None
        // subtlety: value can be 0
        if ((2 * currentIndex + 2) <= (length - 1) && values.get(2 * currentIndex + 2) != null) {
            root.right = new TreeNode(values.get(2 * currentIndex + 2), null, null);
        }
        // call recursively; if right child has its own children, they will be populated
        generateBinaryTreeRecursion(values, root.right, 2 * currentIndex + 2);
        return root;
    }

    /**
     * Generate binary tree from list of values.
     * Tree is not binary-search tree or balanced tree specifically.
     */
    public static TreeNode generateBinaryTree(ArrayList<Integer> values) {
        // empty list --> no tree
        if (values == null){
            return null;
        }
        int current = 0;
        // call recursive function to generate tree
        return generateBinaryTreeRecursion(values, null, current);
    }

    public static void printNode(TreeNode node) {
        if (node != null){
            System.out.printf("node %s; value: %s; left: %s; right: %s", node, node.val, node.left, node.right);
        } else {
            System.out.printf("node %s; value: %s; left: %s; right: %s", null, null, null, null);
        }
    }

    public static void printBinaryTree(TreeNode root, boolean isRoot) {
        if (isRoot) {
            System.out.println();
        }
        printNode(root);

        if (root != null){
            if (root.left != null){
                System.out.println("left child of " + root + " -->");
                printBinaryTree(root.left, false);
            }
            if (root.right != null){
                System.out.println("right child of " + root + " -->");
                printBinaryTree(root.right, false);
            }
        }
    }
}
