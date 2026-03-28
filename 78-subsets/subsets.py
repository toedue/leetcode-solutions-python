class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res , sol = [] , []
        n = len(nums)
        
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # choose to not pick
            backtrack(i+1)


            # choose to pick
            sol.append(nums[i])
            backtrack(i+1)
            # backtrack
            sol.pop()


        backtrack(0)

        return res

            