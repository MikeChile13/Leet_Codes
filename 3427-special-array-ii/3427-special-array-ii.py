class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)  # Get the length of the nums array
        special = [1]  # A list to store the count of special elements, initialized with 1
        count = 1  # Counter to track the number of special segments
        res = []  # List to store results of queries

        # Precompute the special array
        for i in range(1, n):
            if nums[i] & 1:  # Check if nums[i] is odd
                if nums[i-1] % 2 == 0:  # Check if the previous element is even
                    count += 1  # Increase count when the parity changes
            elif nums[i-1] & 1:  # If nums[i] is even and previous was odd
                count += 1  # Increase count
            special.append(count)  # Store the updated count in the special list
        # print(special)
        # Process each query
        for start, end in queries:
            # Check if all elements in the range [start, end] form a special subarray
            # A subarray is special if consecutive elements have alternating parity
            if special[end] - special[start] + 1 == end - start + 1:
                res.append(True)  # The segment is special
            else:
                res.append(False)  # The segment is not special

        return res
