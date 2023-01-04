# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #its a base case
        # this means if there is nothing or just one node return the head
        if not head or not head.next:
            return head
        # split
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp
        # calling the function
        list1 = self.sortList(left)
        list2 = self.sortList(right)
        # now we merge
        return self.merge(list1,list2)
    def getMid(self,head):
        slow = head
        fast = head.next
        if fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if fast.next is none then it means we have reached the mid point which is at slow
            return slow
    def merge(self,list1,list2):
        tail = dummy = ListNode()
        while list1 and list2:#while both lists have a value
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
    

                



