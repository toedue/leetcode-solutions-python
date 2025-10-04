class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range (2,len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])

        return min(cost[-1],cost[-2])

'''
cost = [1,100,1,1,1,100,1,1,100,1]

step 0 = 1
step 1 = 100
so totalCost = [1,100]

---

To reach step 2:
from step 1 → 100 + 1 = 101
from step 0 → 1 + 1 = 2
2 < 101 → totalCost = [1,100,2]

---

To reach step 3:
from step 2 → 2 + 1 = 3
from step 1 → 100 + 1 = 101
3 < 101 → totalCost = [1,100,2,3]

---

To reach step 4:
from step 3 → 3 + 1 = 4
from step 2 → 2 + 1 = 3
3 < 4 → totalCost = [1,100,2,3,3]

---

To reach step 5:
from step 4 → 3 + 100 = 103
from step 3 → 3 + 100 = 103
103 = 103 → totalCost = [1,100,2,3,3,103]

---

To reach step 6:
from step 5 → 103 + 1 = 104
from step 4 → 3 + 1 = 4
4 < 104 → totalCost = [1,100,2,3,3,103,4]

---

To reach step 7:
from step 6 → 4 + 1 = 5
from step 5 → 103 + 1 = 104
5 < 104 → totalCost = [1,100,2,3,3,103,4,5]

---

To reach step 8:
from step 7 → 5 + 100 = 105
from step 6 → 4 + 100 = 104
104 < 105 → totalCost = [1,100,2,3,3,103,4,5,104]

---

To reach step 9:
from step 8 → 104 + 1 = 105
from step 7 → 5 + 1 = 6
6 < 105 → totalCost = [1,100,2,3,3,103,4,5,104,6]

---

To reach the top:
Take min(totalCost[8], totalCost[9]) = min(104, 6) = 6

Final Answer = 6

'''