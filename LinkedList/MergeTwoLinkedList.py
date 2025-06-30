
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        current1 = list1
        current2 = list2
        dummy = ListNode(-1)
        current = dummy

        while current1 and current2:
            if current1.val >= current2.val:
                current.next = current2
                current2 = current2.next
            else:
                current.next = current1
                current1 = current1.next
            current = current.next

        # Attach the remaining list (no infinite loop here)
        if current1:
            current.next = current1
        else:
            current.next = current2

        return dummy.next

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
l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([3,5])
result = Solution().mergeTwoLists(l1, l2)

# Print result
while result:
    print(result.val, end=" -> ")
    result = result.next

# Print None at the end
print("None")

        