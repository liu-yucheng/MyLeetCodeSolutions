from typing import List


class HashableList:
    def __init__(self, il=[]):
        self.il = il  # inner list

    def __eq__(self, value):
        return hash(self) == hash(value)

    def __hash__(self):
        r = 0  # result
        for e in self.il:  # e: element
            r += hash(e)
        return r


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rd = {}  # result dictionary
        for s in strs:  # s: string
            k = HashableList(list(s))  # key
            if k in rd.keys():
                rd[k].append(s)
            else:
                rd[k] = [s]
        r = [v for v in rd.values()]  # r: result
        return r
