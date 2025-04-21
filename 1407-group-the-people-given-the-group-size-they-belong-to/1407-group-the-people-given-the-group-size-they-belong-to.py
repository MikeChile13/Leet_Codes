class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #dictionary of groups
        groups = defaultdict(list[int])
        res = []
        for index,val in enumerate(groupSizes):#enumerate for index and value
            groups[val].append(index) #at each point add the value to needed list
            if len(groups[val]) == val: #deal with lists of same size
                res.append(groups[val])
                groups[val] = []
                #this way the lists of size 3 are separate without hastle 
        return res