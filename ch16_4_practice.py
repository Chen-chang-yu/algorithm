def travel(W, wt, val):
    ''' 動態規劃演算法 '''
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]   # 最初化表格
    for r in range(n + 1):                                  # 填入表格row
        for c in range(W + 1):                              # 填入表格column
            if r == 0 or c == 0:                            # 把表格第一行/第一列變成 0
                table[r][c] = 0
            elif wt[r-1] <= c:
                table[r][c] = max(val[r-1] + table[r-1][c-wt[r-1]], table[r-1][c])
            else:
                table[r][c] = table[r-1][c]
    return table[n][W]

value = [7, 6, 9, 9, 8]                           # 商品價值
weight = [ int(x*2) for x in [0.5, 0.5, 1, 2, 0.5]]                                       # 商品重量
bag_weight = 4                                              # 背包可容重量
print('商品價值 : ', travel(bag_weight, weight, value))







   















