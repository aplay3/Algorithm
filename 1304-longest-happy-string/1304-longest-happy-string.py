class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        cura,curb,curc =0,0,0
        total = a+b+c

        for i in range(total):
            if (a>=b and a>=c and cura != 2) or (a>0 and (curb ==2 or curc==2)):
                result.append('a')
                a -= 1
                cura += 1
                curb = 0
                curc = 0
            elif (b>=a and b>=c and curb != 2) or (b>0 and (cura ==2 or curc ==2) ):
                result.append('b')
                b -=1
                curb+=1
                cura = 0
                curc = 0
            elif( c>=a and c>=b and curc != 2) or (c>0 and (cura==2 or curb==2)):
                result.append('c')
                c -= 1
                curc +=1
                cura = 0
                curb = 0
            
        return "".join(result)

        