"""
187. Gas Station
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station
(i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Example
Example 1:

Input:gas[i]=[1,1,3,1],cost[i]=[2,2,1,1]
Output:2
Example 2:

Input:gas[i]=[1,1,3,1],cost[i]=[2,2,10,1]
Output:-1
Challenge
O(n) time and O(1) extra space

Notice
The solution is guaranteed to be unique.
"""
from typing import List


class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost or len(gas) != len(cost):
            return -1

        m = len(gas)
        n = 0
        while n < m:
            j = n
            sum = gas[j]
            while sum - cost[j % m] >= 0:
                sum = sum - cost[j % m] + gas[(j + 1) % m]
                j += 1
                if j - n == m:
                    return n
            n = j + 1

        return -1


def main():
    s = Solution()
    gas = [1, 1, 3, 1]
    cost = [2, 2, 10, 1]
    print(s.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
