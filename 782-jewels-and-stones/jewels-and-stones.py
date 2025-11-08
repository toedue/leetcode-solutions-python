class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set1 = set()
        list1 = []
        for jewel in jewels:
            set1.add(jewel)
            
        for stone in stones:
            if stone in set1:
                list1.append(stone)
        return len(list1)
        