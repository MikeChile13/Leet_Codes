class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list[int])
        res = []
        for index,val in enumerate(groupSizes):
            groups[val].append(index)
            if len(groups[val]) == val:
                res.append(groups[val])
                groups[val] = []
        return res