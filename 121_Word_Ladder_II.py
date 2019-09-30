"""
121. Word Ladder II
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, output sequence in dictionary order.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
Example
Example 1:

Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：[["a","c"]]
Explanation：
"a"->"c"
Example 2:

Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation：
1."hit"->"hot"->"dot"->"dog"->"cog"
2."hit"->"hot"->"lot"->"log"->"cog"
The dictionary order of the first sequence is less than that of the second.
Notice
All words have the same length.
All words contain only lowercase alphabetic characters.
At least one solution exists.
"""
import collections


class Solution:
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        index_map = self.find_indexes(dict)
        print(index_map)
        distance_map = self.find_length(end, index_map)
        print(distance_map)
        result = []
        self.find_path(start, end, distance_map, index_map, [], result)
        return result

    def find_indexes(self, dict):
        index_map = {}
        for d in dict:
            for i in range(len(d)):
                cur = d[:i] + '%' + d[i + 1:]
                if cur in index_map:
                    index_map[cur].add(d)
                else:
                    index_map[cur] = set()
                    index_map[cur].add(d)
        return index_map

    def find_next_words(self, word, index_map):
        result = []
        for i in range(len(word)):
            cur = word[:i] + '%' + word[i + 1:]
            for w in index_map.get(cur, []):
                result.append(w)
        return result

    def find_length(self, end, index_map):
        queue = collections.deque()
        distance_map = {end: 0}
        queue.append(end)
        while queue:
            cur = queue.popleft()
            for next_word in self.find_next_words(cur, index_map):
                if next_word not in distance_map:
                    distance_map[next_word] = distance_map[cur] + 1
                    queue.append(next_word)
        return distance_map

    def find_path(self, start, end, distance_map, index_map, prev, result):
        if start == end:
            result.append(prev + [end])
            return
        for word in self.find_next_words(start, index_map):
            if distance_map[word] != distance_map[start] - 1:
                continue
            prev.append(start)
            self.find_path(word, end, distance_map, index_map, prev, result)
            prev.pop()


def main():
    s = Solution()
    start = "hit"
    end = "cog"
    dict = {"hot", "dot", "dog", "lot", "log"}
    print(s.findLadders(start, end, dict))


if __name__ == '__main__':
    main()
