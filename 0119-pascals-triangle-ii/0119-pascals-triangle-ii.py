class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for _ in range(rowIndex):
            temp = [0] + triangle[-1] + [0]
            row = []
            for i in range(len(triangle[-1]) + 1):
                row.append(temp[i] + temp[i+1])
            triangle.append(row)
        return triangle[-1]