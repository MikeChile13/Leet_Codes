class Solution:
    def countLargestGroup(self, n: int) -> int:
        largest_sum = 0
        sizes = defaultdict(int)
        for num in range(1,n+1):
            sumv = 0
            # s = num
            while num:
                sumv += num%10
                num //= 10
            # print(s,sumv)
            sizes[sumv] += 1
            largest_sum = max(largest_sum,sizes[sumv])
        count = 0
        # print(sizes)
        for value in sizes.values():
            count += value == largest_sum
        return count
