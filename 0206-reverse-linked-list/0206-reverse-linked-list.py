class Solution(object):
    def reverseList(self, head):
        last, current = None, head
        while current:
            next_pointer = current.next
            current.next = last
            last = current
            current = next_pointer
            
        return last