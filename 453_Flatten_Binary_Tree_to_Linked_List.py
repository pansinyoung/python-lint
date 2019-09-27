"""
453. Flatten Binary Tree to Linked List
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Example
Example 1:

Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
Example 2:

Input:{1}
Output:{1}
Explanation：
         1
         1
Challenge
Do it in-place without any extra memory.

Notice
Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def flatten(self, root: TreeNode):
        if not root:
            return
        self.helper(root)

    def helper(self, root: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root
        left_end, right_end = None, None
        if root.left:
            left_end = self.helper(root.left)
        if root.right:
            right_end = self.helper(root.right)
        if not left_end:
            return right_end
        if not right_end:
            root.right = root.left
            root.left = None
            return left_end
        left_end.right = root.right
        root.right = root.left
        root.left = None
        return right_end




def main():
    s = Solution()
    test = ArrayReader([1, 3, 3, 3, 6, 9, 21])
    target = 122
    print(s.searchBigSortedArray(test, target))

if __name__ == '__main__':
    main()
