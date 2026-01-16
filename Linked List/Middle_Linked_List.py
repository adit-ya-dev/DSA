"Return the middle node of the linked list.
If there are 2 middle nodes, return the second one."

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
