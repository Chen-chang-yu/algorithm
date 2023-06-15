
def knapsack(W, wt, val, item):
    ''' 動態規劃演算法 '''
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]   # 最初化表格
    table_goods = [['Null' for x in range(W + 1)] for x in range(n + 1)]   # 最初化表格

    for r in range(n + 1):                                  # 填入表格row
        for c in range(W + 1):                              # 填入表格column
            if r == 0:
                table_goods[r][c] = ''
            elif c == 0:
                table_goods[r][c] = item[r-1]
            elif wt[r-1] <= c:
                temp = 0
                if val[r-1] + table[r-1][c-wt[r-1]] > table[r-1][c]:
                    temp = val[r-1] + table[r-1][c-wt[r-1]]
                    if c-wt[r-1] == 0:
                        temp_good = item[r-1]
                    else:
                        temp_good = item[r-1] + table_goods[r-1][c-wt[r-1]]
                else:
                    temp = table[r-1][c]
                    temp_good = table_goods[r-1][c]
                table[r][c] = temp
                table_goods[r][c] = temp_good
                #table[r][c] = max(val[r-1] + table[r-1][c-wt[r-1]], table[r-1][c])
            else:
                table[r][c] = table[r-1][c]
                table_goods[r][c] = table_goods[r-1][c]
    return table, table_goods

item = ['S', 'T', 'P', 'N']
value = [50000,40000,25000, 20000]                           # 商品價值
weight = [4, 3, 1, 1]                                       # 商品重量
bag_weight = 4                                              # 背包可容重量
print('商品價值 : ', knapsack(bag_weight, weight, value, item)[0])
print('訂單內容 : ', knapsack(bag_weight, weight, value, item)[1])









   















