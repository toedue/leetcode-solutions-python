class Solution:
    def lastRemaining(self, n: int) -> int:
       
        def solve(n, left_to_right):

            #base case
            if n == 1:
                return 1

            if left_to_right:

                return 2*solve(n//2, False)
            else: 
                #right_to_left
                if n % 2 == 0: # leftmost survives
                    return 2*solve(n//2, True) - 1

                return 2*solve(n//2, True)


        return solve(n, True)



