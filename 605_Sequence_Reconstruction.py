"""
605. Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example
Example 1:

Input:org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output:true
"""
from typing import List


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not org and (not seqs or not seqs[0]):
            return True
        if not org or not seqs:
            return False
        edges = {}
        degrees = {}
        for seq in seqs:
            for cur in seq:
                if cur not in edges:
                    edges[cur] = set()
                    degrees[cur] = 0
        for seq in seqs:
            for i in range(1, len(seq)):
                edges[seq[i - 1]].add(seq[i])
        for k in edges:
            for i in edges[k]:
                degrees[i] += 1

        result = []
        queue = []
        for k in degrees:
            if degrees[k] == 0:
                queue.append(k)

        while queue:
            if len(queue) != 1:
                return False
            cur = queue.pop()
            result.append(cur)
            for i in edges[cur]:
                degrees[i] -= 1
                if degrees[i] == 0:
                    queue.append(i)

        return result == org


def main():
    s = Solution()
    org = [4, 1, 5, 2, 6, 3]
    seqs = [[5, 2, 6, 3], [4, 1, 5, 2]]
    print(s.sequenceReconstruction(org, seqs))


if __name__ == '__main__':
    main()
