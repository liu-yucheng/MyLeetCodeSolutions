class Solution(object):
    def threeSum(self, nums):
        nl = len(nums)  # nums length
        if nl < 3:
            return []
        nums.sort()
        r = []  # result
        il = 0  # index left
        ic = 0  # index center
        ir = 0  # index right
        while il < nl - 2:
            ic = il + 1
            ir = nl - 1
            ts = -nums[il]  # target sum
            while ic < ir:
                tl = nums[il]  # tuple left
                tc = nums[ic]  # tuple center
                tr = nums[ir]  # tuple right
                s = tc + tr  # sum
                if s < ts:
                    ic += 1
                elif s > ts:
                    ir -= 1
                else:
                    t = [tl, tc, tr]  # tuple
                    r.append(t)
                    ic += 1
                    ir -= 1
                    while ic < ir and nums[ic] == tc:
                        ic += 1
                    while ic < ir and nums[ir] == tr:
                        ir -= 1
            tl = nums[il]
            il += 1
            while il < nl - 2 and nums[il] == tl:
                il += 1
        return r
