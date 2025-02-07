class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        distinct_colors = defaultdict(int)
        colored = {}
        res = []
        length = 0
        for index,new_color in queries:
            if index in colored:
                prev_color = colored[index]
                distinct_colors[prev_color] -=1
                if distinct_colors[prev_color] == 0:
                    del distinct_colors[prev_color]

            distinct_colors[new_color] +=1
            colored[index] = new_color
            res.append(len(distinct_colors))

        return res