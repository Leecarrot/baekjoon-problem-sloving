def solution(numbers, target):
    def dfs(i, total):
        if i == len(numbers):
            if total == target:
                return 1
            else:
                return 0
        return dfs(i + 1, total + numbers[i]) + dfs(i + 1, total - numbers[i])
    return dfs(0, 0)
    