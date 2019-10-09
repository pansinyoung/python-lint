"""
526. Load Balancer
Implement a load balancer for web servers. It provide the following functionality:

Add a new server to the cluster => add(server_id).
Remove a bad server from the cluster => remove(server_id).
Pick a server in the cluster randomly with equal probability => pick().
At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.

Example
Example 1:

Input:
  add(1)
  add(2)
  add(3)
  pick()
  pick()
  pick()
  pick()
  remove(1)
  pick()
  pick()
  pick()
Output:
  1
  2
  1
  3
  2
  3
  3
Explanation: The return value of pick() is random, it can be either 2 3 3 1 3 2 2 or other.
"""
import random


class LoadBalancer:
    def __init__(self):
        self.data = []
        self.data_to_pos_map = {}

    def add(self, server_id):
        self.data.append(server_id)
        self.data_to_pos_map[server_id] = len(self.data) - 1

    def remove(self, server_id):
        pos = self.data_to_pos_map[server_id]
        if pos != len(self.data) - 1:
            self.data[pos] = self.data[-1]
            self.data_to_pos_map[self.data[-1]] = pos
        self.data.pop()
        del self.data_to_pos_map[server_id]

    def pick(self):
        return self.data[random.randint(0, len(self.data) - 1)]
