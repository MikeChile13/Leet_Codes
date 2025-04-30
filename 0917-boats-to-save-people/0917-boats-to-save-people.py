class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        length = len(people)

        boats = 0

        boat = 0

        people.sort()

        j = length - 1
        while j >= 0:
            if people[j] >= limit:
                boats += 1
            else:
                break
            j -= 1

        i = 0
        while i <= j:
            if people[j] + people[i] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            boats += 1

        # print(i)
        return boats

