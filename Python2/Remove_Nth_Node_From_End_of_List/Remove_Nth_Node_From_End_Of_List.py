# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # node from where the skip should occur
        nodeBeforeRemove = head

        # current node we are on
        currentNode = head

        # total nodes traverse
        distanceTraveled = 0

        # until we reach the end of the linked list
        while currentNode != None:
            # if we're at the end of the list and we've traveled far enough, delete the nth node from list
            if currentNode.next == None and distanceTraveled >= n:
                nodeBeforeRemove.next = nodeBeforeRemove.next.next
                return head
            # if we've traveled far enough, step forward the node from where the skip should occur
            elif distanceTraveled >= n:
                nodeBeforeRemove = nodeBeforeRemove.next

            # otherwise, note that we've traveled another node
            else:
                distanceTraveled += 1

            # traverse to the next node
            currentNode = currentNode.next

        # if we've reach the end of the list and our input n is longer than the list, delete the first node
        return head.next
