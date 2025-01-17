class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Initialize the first and last elements of the original array to 0.
        last, first = 0, 0

        # Iterate through the derived array (excluding the last element).
        for i in range(len(derived) - 1):
            if derived[i] == 1:
                # If the current derived element is 1, toggle the 'last' value.
                # A XOR operation is effectively being simulated.
                last = 1 if last == 0 else 0
            else:
                # If the current derived element is 0, keep the 'last' value unchanged.
                # This corresponds to no toggle.
                last = 0 if last == 0 else 1

        # At the end of the loop, 'last' represents the last element of the original array.
        
        # Check if the last element of the derived array is 1.
        if derived[-1]:
            # If it is 1, the first and last elements of the original array must be different.
            return first != last
        # If the last derived element is 0, the first and last elements of the original array must be the same.
        return first == last
