class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count1=0
        count2=0
        for strs in s:
            if strs=="L":
                count1+=1
            if strs=="R":
                count1-=1
            if count1==0:
                count2+=1
        return count2
        