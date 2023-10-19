# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head

        list1 = trav1 = ListNode()
        list2 = trav2 = ListNode()
        
        trav = head

        while trav:
            if trav.val < x:
                trav1.next = ListNode(trav.val)
                trav1 = trav1.next
            else:
                trav2.next = ListNode(trav.val)
                trav2 = trav2.next
            trav = trav.next
        
        if not list1.next:
            return list2.next
        
        list1 = list1.next
        trav1.next = list2.next
        trav2.next = None
        
        return list1
        
