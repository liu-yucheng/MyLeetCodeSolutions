class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        subresults = [0 for _ in range(n + 1)]
        subresults[0] = 1
        subresults[1] = 1
        for iter in range(2, n + 1):
            for left in range(0, iter):
                right = iter - left - 1
                subresults[iter] += subresults[left] * subresults[right]
        return subresults[-1]
