"You are given two sorted linked lists list1 and list2.
Merge them into one sorted linked list and return its head."

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # attach remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next
