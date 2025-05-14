class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        relation = defaultdict()
        for i in range(len(names)):
            relation[heights[i]] = names[i]
        # for height in sorted(heights):
            # print(relation[height])
        return [ relation[height] for height in sorted(heights,reverse=True)]