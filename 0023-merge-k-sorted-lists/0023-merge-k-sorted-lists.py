import heapq

class Solution(object):
    def mergeKLists(self, lists):

        dummy = ListNode(0)
        tail = dummy

        heap = []

        # Put first node of every list into heap
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(
                    heap,
                    (lists[i].val, i, lists[i])
                )

        # Merge lists
        while heap:

            value, i, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next is not None:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next
        