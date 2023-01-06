＃題目：每種商品無限制數量的情況下，ｎ公斤的背包要怎麼放才能獲得最大的價值

n = 5  # 背包總共5公斤重
value = [4, 9, 17]  # 3個物品每個物品的價值                                
weight = [1, 2, 4]  # 3個物品每個物品的重量                                  

dp = [0 for _ in range(n+1)]  # 動態規劃初始值都設定為 0

for i in range(n+1):      # 從第0公斤的背包開始放物品
    for j in range(len(weight)):　　　＃　物品總共有３樣
        if weight[j] <= i:
            dp[i] = max(dp[i], value[j] + dp[i-weight[j]])

print(dp)

                                  







   















