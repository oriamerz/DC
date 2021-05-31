


class Solution:
    def combinationSum(self, candidates: list[int], target: int):
        result=[]
        y=0
        for i in candidates:
            x=target/i

            if int(x) == x:
                result.append([i for j in range(x)])
