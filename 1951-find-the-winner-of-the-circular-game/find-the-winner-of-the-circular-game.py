class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # create the circle
        circle = list(range(1, n + 1))  # [1, 2, 3, ... n]

        index = 0  # start at position 0 (friend 1)

        while len(circle) > 1:

            # move k-1 steps forward from current position
            # % len(circle) handles wrapping around!
            index = (index + k - 1) % len(circle)

            # remove this friend
            circle.pop(index)

            # index now automatically points to next friend
            # BUT if we removed the last element, wrap to 0
            if index == len(circle):
                index = 0

        return circle[0]  # last one standing!