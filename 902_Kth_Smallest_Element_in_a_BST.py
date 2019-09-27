"""
902. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example
Example 1:

Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.
Example 2:

Input：{2,1,3},1
Output：1
Explanation：
  2
 / \
1   3
The first smallest element is 1.
Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Notice
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        stack = []
        p = root
        while p:
            stack.append(p)
            p = p.left
        while stack or p:
            if not p:
                p = stack.pop()
                k -= 1
                if k == 0:
                    return p.val
                if p.right:
                    p = p.right
                else:
                    p = None
            else:
                while p:
                    stack.append(p)
                    p = p.left




def main():
    s = Solution()
    test = ArrayReader([1, 3, 3, 3, 6, 9, 21])
    target = 122
    print(s.searchBigSortedArray(test, target))


if __name__ == '__main__':
    main()
