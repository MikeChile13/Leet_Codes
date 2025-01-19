class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position,speed) for position,speed in zip(position,speed)]
        fleets = []
        for position,speed in sorted(pairs)[::-1]:
            fleets.append((target - position)/speed)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)

