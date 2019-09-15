"""
7. Serialize and Deserialize Binary Tree
中文English
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

Example
Example 1:

Input：{3,9,20,#,#,15,7}
Output：{3,9,20,#,#,15,7}
Explanation：
Binary tree {3,9,20,#,#,15,7},  denote the following structure:
	  3
	 / \
	9  20
	  /  \
	 15   7
it will be serialized {3,9,20,#,#,15,7}
Example 2:

Input：{1,2,3}
Output：{1,2,3}
Explanation：
Binary tree {1,2,3},  denote the following structure:
   1
  / \
 2   3
it will be serialized {1,2,3}
Our data serialization use BFS traversal. This is just for when you got Wrong Answer and want to debug the input.

You can use other method to do serializaiton and deserialization.

Notice
There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.
"""


"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from typing import List
from collections import deque
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        result = []
        queue.append(root)
        queue.append('/')
        cur_result = []
        while queue:
            cur = queue.popleft()
            if not cur:
                cur_result.append('#')
            elif cur == '/':
                if not all(i == '#' for i in cur_result):
                    result += cur_result
                    cur_result = []
                    queue.append('/')
            else:
                cur_result.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
        return result


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data: List[int]) -> TreeNode:
        if not data:
            return None
        data_queue = deque(data)
        node_queue = deque()
        root = TreeNode(data_queue.popleft())
        node_queue.append(root)
        while node_queue and data_queue:
            cur_node = node_queue.popleft()
            cur_num = data_queue.popleft()
            if cur_num != '#':
                cur_node.left = TreeNode(cur_num)
                node_queue.append(cur_node.left)
            cur_num = data_queue.popleft()
            if cur_num != '#':
                cur_node.right = TreeNode(cur_num)
                node_queue.append(cur_node.right)

        return root



def main():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(s.serialize(None))
    print(s.serialize(s.deserialize(s.serialize(None))))


if __name__ == '__main__':
    main()
