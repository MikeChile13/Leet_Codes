class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1 = [
            float(event1[0][:2]) + float(event1[0][3:])/100,
            float(event1[1][:2]) + float(event1[1][3:])/100
            ]
        event2 = [
            float(event2[0][:2]) + float(event2[0][3:])/100,
            float(event2[1][:2]) + float(event2[1][3:])/100
        ]
        if event1[0] > event2[1] or event1[1] < event2[0]:
            return False
        return True
