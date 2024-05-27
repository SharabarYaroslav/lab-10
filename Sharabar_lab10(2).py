"""
Дано рядок без пробілів і словник слів.
Потрібно визначити, чи можна розбити цей рядок на послідовність слів зі словника.
"""


def word_break(s, word_dict):
    word_set = set(word_dict)  
    dp = [False] * (len(s) + 1)
    dp[0] = True  

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    print(dp)
    return dp[len(s)]


s = "blackdoor"
word_dict = ["black", "door"]
print(word_break(s, word_dict))  
