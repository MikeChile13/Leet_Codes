class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)#size of array

        bad_pairs = (n* (n-1) ) // 2 #total possible pairs set to bad_pairs
        diff = defaultdict(int) #keep track of good pairs found.

        for i,number in enumerate(nums):
            #for good pairs, the difference between their numbers and their indices will be the same.
            difference = number - i
            #subtract the corresponding good_pairs from the bad_pairs
            bad_pairs-=diff.get(difference,0) 
            diff[difference]+=1
        return bad_pairs
