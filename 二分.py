# 假设条件准备
# 这里模拟一个升序数组 a 和要查找的数 x
a = [1, 3, 5, 7, 9, 11, 13, 15]
x = 9

# 初始化左右边界（对应原代码的 l = 1, r = n）
# Python 习惯从 0 开始，所以 l = 0, r = 数组长度减 1
l = 0
r = len(a) - 1
ret = -1 # 未找到时返回 -1

# 核心二分查找逻辑
while l <= r:
    mid = (l + r) >> 1  # 对应原代码的 (l + r) >> 1，也可以用 (l + r) // 2
    
    if a[mid] < x:
        l = mid + 1
    elif a[mid] > x:
        r = mid - 1
    else:
        # 最后检测相等
        ret = mid
        break

# 输出结果
print(ret) # 此时会输出 4，因为 a[4] == 9
