"""2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
- Problem description: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticals = [None]
        prev = head
        curr = head.next
        # Determine the critical points
        while True:
            if curr.next is None:
                criticals.append(None)
                break
            if (prev.val < curr.val > curr.next.val) or (prev.val > curr.val < curr.next.val):
                criticals.append(True)
            else:
                criticals.append(None)
            prev = curr
            curr = curr.next

        if len(list(filter(None, criticals))) < 2:
            # Avoid distance calculation if there is not enough criticals
            return [-1, -1]
        # Calculate the min/max lengths between critical points
        min_dist = max_dist = None
        first = last = None
        for idx, crit in enumerate(criticals):
            if crit:
                if not first:
                    first = idx
                if last:
                    max_dist = idx - first
                    last_dist = idx - last
                    min_dist = min_dist if min_dist and min_dist < last_dist else last_dist
                last = idx

        return [min_dist, max_dist]


tests = [
    [[3, 1], [-1, -1]],
    [[5, 3, 1, 2, 5, 1, 2], [1, 3]],
    [[1, 3, 2, 2, 3, 2, 2, 2, 7], [3, 3]]
]
print(tests)


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
    list_nodes = create_list_node_structure(arr=given)
    result = solution.nodesBetweenCriticalPoints(list_nodes)
    print("Result:", result)
    assert result == expected

# input = ListNode(5, ListNode(3, ListNode(1, ListNode(2,ListNode(5, ListNode(1, ListNode(2)))))))
