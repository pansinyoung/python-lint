"""
137. Clone Graph
中文English
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

Example
Example1

Input:
{1,2,4#2,1,4#4,1,2}
Output:
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2
 \     |
  \    |
   \   |
    \  |
      4
Clarification
How we serialize an undirected graph: http://www.lintcode.com/help/graph/

Notice
You need return the node with the same label as the input node.
"""
"""
Definition for a undirected graph node
"""
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        if not node:
            return None
        nodes_dic = {}
        queue = [node]
        nodes_dic[node.label] = UndirectedGraphNode(node.label)
        while queue:
            cur = queue.pop()
            for next in cur.neighbors:
                if next.label not in nodes_dic:
                    queue.append(next)
                    nodes_dic[next.label] = UndirectedGraphNode(next.label)
                nodes_dic[cur.label].neighbors.append(nodes_dic[next.label])
        return nodes_dic[node.label]


def main():
    s = Solution()
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node4 = UndirectedGraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node4]
    node4.neighbors = [node1, node2]

    print(s.cloneGraph(node1).label)


if __name__ == '__main__':
    main()
