class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        row,col = len(box),len(box[0])

        res = [["."] * row for _ in range(col)]

        for r in range(row):
            i = col - 1
            for c in reversed(range(col)):
                if box[r][c]=="#":
                    res[i][row-r-1]="#"
                    i-=1
                elif box[r][c] =='*':
                    res[c][row-r-1]="*"
                    i= c-1
        return res