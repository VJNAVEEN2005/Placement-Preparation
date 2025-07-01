class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev , current = current , temp
        return prev

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
result = Solution().reverseList(l1)
# Print result
while result:
    print(result.val, end=" -> ")
    result = result.next
# Print None at the end
print("None")