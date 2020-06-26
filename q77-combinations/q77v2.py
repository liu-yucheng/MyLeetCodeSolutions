from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        stack = []
        iter = 1
        while True:
            # print(f'iter:{iter}')
            length = len(stack)
            if length == k:
                result.append(stack[:])
            if length == k or iter > n - k + length + 1:
                if len(stack) == 0:
                    break
                iter = stack.pop() + 1
            else:
                stack.append(iter)
                iter += 1
            length = len(stack)
        return result
