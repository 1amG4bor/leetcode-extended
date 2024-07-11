"""2181. Merge Nodes in Between Zeros
- Problem description: https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = tail = ListNode()
        local_sum = head.val
        curr = head.next
        while curr:
            if curr.val == 0:
                old_tail = tail
                tail = ListNode()

                old_tail.val = local_sum
                if curr.next:
                    old_tail.next = tail
                local_sum = 0
            else:
                local_sum += curr.val
            curr = curr.next

        return result
        # return self.create_list_node_structure(result)

tests = [
    [[0, 3, 1, 0, 4, 5, 2, 0], [4, 11]],
    [[0, 1, 0, 3, 0, 2, 2, 0], [1, 3, 4]]
]


def create_list_node_structure(arr: List[int], list_node: Optional[ListNode] = None) -> ListNode:
    val = arr.pop(0)
    if arr:
        next_node = create_list_node_structure(arr)
        return ListNode(val, next_node)
    else:
        return ListNode(val)

solution = Solution()
for test in tests:
    given = test[0]
    expected = test[1]
    list_nodes = create_list_node_structure(given)
    result = solution.mergeNodes(list_nodes)
    print("Result:", result)
    assert result == expected
