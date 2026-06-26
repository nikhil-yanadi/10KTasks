class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            cnt=0
            while num>0:
                cnt+=num%10
                num//=10
            num=cnt
        return num