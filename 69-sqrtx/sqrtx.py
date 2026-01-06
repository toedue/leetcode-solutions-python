class Solution:
    def mySqrt(self, x: int) -> int:
         # Initialize binary search boundaries
        ## left starts at 0, right starts at x
        left, right = 0, x
      
        # Binary search to find the integer square root
        while left < right:
            # Calculate mid point, using (left + right + 1) // 2
            # The +1 ensures we round up to avoid infinite loop
            mid = (left + right + 1) >> 1  # Bit shift right by 1 is equivalent to // 2
          
            # Check if mid^2 > x by comparing mid with x // mid
            # This avoids potential overflow from mid * mid
            if mid > x // mid:
                # If mid is too large, search in the left half
                right = mid - 1
            else:
                # If mid^2 <= x, this could be our answer, search in the right half
                left = mid
      
        # Return the integer square root
        return left