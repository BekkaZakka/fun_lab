ves = [3, 2, 4, 1]
values = [5, 3, 8, 2]
max_ves = 3

def rukzak(ves, values, max_ves):
    n = len(ves)
    dp = [0] * (max_ves + 1)
    for i, v in enumerate(ves):
        for j in reversed(range(v, max_ves + 1)):
            dp[j] = max(dp[j], dp[j - v] + values[i])
    return dp[max_ves];

max_value = rukzak(ves, values, max_ves)
print("Max value:", max_value)