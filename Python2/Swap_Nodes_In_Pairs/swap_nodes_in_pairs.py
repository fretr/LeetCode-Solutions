# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # if the head node is None, return it
        if head == None:
            return head

        # if the node after the head node is None, return it
        elif head.next == None:
            return head

        # otherwise, swap the first two two nodes, and call swapPairs on the third node
        else:
            nextNode = head.next
            tempNode = nextNode.next
            nextNode.next = head
            head.next = self.swapPairs(tempNode)
            return nextNode

        
