class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def findTheWinner(n):
            # base case
            # only one person left, they are at position/index 0
            if n == 1:
                return 0

            # get winner position in smaller circle
            smaller_winner = findTheWinner(n-1)

            # translate that position back to current circle
            current_winner = (smaller_winner + k) % n

            return current_winner

        # findTheWinner gives 0-indexed position so add 1 to get actual friend number
        return findTheWinner(n) + 1


            

