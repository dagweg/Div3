
class Solution:
    def deleteNode(self, node):
        s, f = node, node.next

        while f.next:
            s.val, f.val = f.val, s.val
            s = f
            f = f.next
        s.val, f.val = f.val, s.val
        s.next = None
