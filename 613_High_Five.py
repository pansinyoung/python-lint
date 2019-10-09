"""
613. High Five
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.

Example
Example 1:

Input:
[[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
Output:
1: 72.40
2: 97.40

Example 2:

Input:
[[1,90],[1,90],[1,90],[1,90],[1,90],[1,90]]
Output:
1: 90.00
"""


'''
Definition for a Record
'''
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

import heapq


class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        score_heaps = {}
        for r in results:
            if r.id not in score_heaps:
                score_heaps[r.id] = []
            score_heaps[r.id].append(r.score)
        for k in score_heaps:
            score_heaps[k] = sum(heapq.nlargest(5, score_heaps[k])) / 5
        return score_heaps
