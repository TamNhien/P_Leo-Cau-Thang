# Số cách leo cầu để leo cầu thang lên tới đỉnh
def count_ways(n, X):
    dp = [0]*(n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in X:
            if j <= i:
                dp[i] += dp[i -j]
                
    return dp[n]

# Nhập số bậc của cầu thang
N = int(input("Nhập số bậc của cầu thang: "))

# Nhập tập hợp các bước có thể leo
X = set(map(int, input("Nhập các bước có thể leo (cách nhau bởi dấu cách): ").split()))

# In ra số cách leo cầu thang và tập hợp các bước có thể leo
print("Số cách leo cầu thang: ", count_ways(N, X))
print("Tập hợp các bước có thể leo: ", sorted(X))
