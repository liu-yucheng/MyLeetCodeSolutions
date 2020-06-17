class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 0
        nums.sort()
        il = 0  # index left
        ic = 1  # index center
        ir = 2  # index right
        r = -1 * 2 ** 31  # result (initialized to int min)
        while il < len(nums) - 2:
            ic = il + 1
            ir = len(nums) - 1
            tl = nums[il]  # tuple left
            while ic < ir:
                tc = nums[ic]  # tuple center
                tr = nums[ir]  # tuple right
                ts = tl + tc + tr  # tuple sum
                ard = abs(r - target)  # absolute result difference
                td = ts - target  # target difference
                atd = abs(td)  # absolute result difference
                if td == 0:
                    return ts
                if atd < ard:
                    r = ts
                if td < 0:
                    while ic < ir and nums[ic] == tc:
                        ic += 1
                elif td > 0:
                    while ic < ir and nums[ir] == tr:
                        ir -= 1
            while il < len(nums) - 2 and nums[il] == tl:
                il += 1
        return r
