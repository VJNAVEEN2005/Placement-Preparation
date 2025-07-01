class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    
# Helper function to convert list to linked list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
# Sample test
l1 = build_linked_list([1, 2, 3, 4, 5])
l1.next.next.next.next = l1.next  # Creating a cycle for testing
result = Solution().hasCycle(l1)
# Print result
print("Cycle Detected" if result else "No Cycle Detected")