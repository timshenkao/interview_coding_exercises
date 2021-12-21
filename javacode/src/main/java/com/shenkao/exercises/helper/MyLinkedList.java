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


import java.util.HashSet;
import java.util.Set;

public class MyLinkedList {
    public static ListNode generateList(int[] values) {
        if (values == null) {
            return null;
        }
        ListNode temp = null;
        ListNode head = null;
        //    # creating nodes in reverse order
        for (int i = values.length - 1; i >= 0; i--) {
            head = new ListNode(values[i], temp);
            temp = head;
        }
        return head;
    }

    public static ListNode generateListCycle(int[] values, int pos) {
        if (values == null) {
            return null;
        }
        ListNode head = generateList(values);
        ListNode currNode = null;

        if (pos >= 0) {
            // get pointer to an internal node
            int i = 0;
            currNode = head;
            while (i < pos) {
                i++;
                currNode = currNode.nextNode;
            }
            // get pointer to the tail node
            ListNode tail = currNode;
            while (tail.nextNode != null) {
                tail = tail.nextNode;
            }
            tail.nextNode = currNode;
        }
        return head;
    }

    /**
     * Given the head of a singly-linked list and value, return ListNode that contains the value.
     */
    public static ListNode locateNode(ListNode head, int value) {
        ListNode temp = head;
        while (temp != null) {
            if (temp.val == value) {
                return temp;
            }
            temp = temp.nextNode;
        }
        return null;
    }

    public static void printNode(ListNode node) {
        System.out.println();
        if (node != null) {
            System.out.printf("node: %s; value: %s; next node: %s", node, node.val, node.nextNode);
        } else {
            System.out.printf("node: %s; value: %s; next node: %s", null, null, null);
        }
        System.out.println();
    }

    public static void printList(ListNode head) {
        System.out.println();
        int i = 0;
        if (head != null){
            Set<ListNode> visitedNodes = new HashSet<ListNode>();
            while (head.nextNode != null){
                if (!visitedNodes.contains(head)){
                    System.out.printf("node %s: %s; value: %s; next node: %s", i, head, head.val, head.nextNode);
                    visitedNodes.add(head);
                    head = head.nextNode;
                    i++;
                } else {
                    break;
                }
            }
            if (head.nextNode == null){
                System.out.printf("node %s: %s; value: %s; next node: %s", i, head, head.val, head.nextNode);
            } else {
                System.out.printf("node %s: %s; value: %s; next node: %s", 0, head, null, null);
            }
        }
    }
}
