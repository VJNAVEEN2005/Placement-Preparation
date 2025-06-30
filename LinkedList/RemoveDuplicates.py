class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):     
        current = head
        seen = set()
        while current:
            if current.val in seen:
                prev.next = current.next
            else :
                seen.add(current.val)
                prev = current
            current = current.next
        return head
    
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
l1 = build_linked_list([1, 2, 3, 3, 4, 4, 5])
result = Solution().deleteDuplicates(l1)
# Print result
while result:
    print(result.val, end=" -> ")
    result = result.next
# Print None at the end
print("None")