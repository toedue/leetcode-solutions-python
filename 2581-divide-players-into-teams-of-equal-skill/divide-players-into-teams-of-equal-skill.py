class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left, right = 0, len(skill)-1
        result = 0
        skill.sort()

        sum = skill[left] + skill[right]

        while left < right:
            if sum != skill[left] + skill[right]:
                return -1
            else:
                result += skill[left] * skill[right]

            left += 1
            right -= 1

        return result 
            