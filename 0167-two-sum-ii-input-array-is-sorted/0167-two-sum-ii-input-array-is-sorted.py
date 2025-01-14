class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        sumv = numbers[left]+numbers[right]
        while sumv != target:
            if sumv > target:
                right-=1
            elif sumv < target:
                left+=1
            sumv = numbers[left] + numbers[right]

        return [left+1,right+1]

        