class Solution(object):
    def copyRandomList(self, head):

        if not head:
            return None

        # Map original node → copied node
        copy = {}

        # Create all copied nodes
        current = head

        while current:
            copy[current] = Node(current.val)
            current = current.next

        # Connect next and random
        current = head

        while current:
            copy[current].next = copy.get(current.next)
            copy[current].random = copy.get(current.random)

            current = current.next

        return copy[head]