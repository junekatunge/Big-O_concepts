class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_value = r

        while l <= r:
            k = (l + r)// 2
            # total hours
            hours = 0
            for i in piles:
                # round off using math.ceil()
                hours += math.ceil(i / k)
            if hours <= h:
                min_value = min(r,k)
                r = k - 1
            else:
                l = k + 1
        return min_value
