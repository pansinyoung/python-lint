"""
535. House Robber III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example
Example1

Input:  {3,2,3,#,3,#,1}
Output: 7
Explanation:
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
  3
 / \
2   3
 \   \
  3   1
Example2

Input:  {3,4,5,1,3,#,1}
Output: 9
Explanation:
Maximum amount of money the thief can rob = 4 + 5 = 9.
    3
   / \
  4   5
 / \   \
1   3   1
Notice
This problem is the extention of House Robber and House Robber II
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        return self.helper(root, False)

    def helper(self, root, parent_robbed):
        if not root:
            return 0
        result = self.helper(root.left, False) + self.helper(root.right, False)
        if not parent_robbed and root.val > 0:
            result = max(result, self.helper(root.left, True) + self.helper(root.right, True) + root.val)
        return result
