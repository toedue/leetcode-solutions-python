class Solution:
    #abdulkadir
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set_ = set(range(left,right+1))
        for s,e in ranges:
            for i in range(s,e+1):
                set_.discard(i)
                if len(set_) == 0:
                    return True
        return False