# 元组 list set map


# a = (1, "xxx", 22)
# # 不支持修改操作
# idd, name, age = a
# print(idd, name, age)

# ========================================

# l = [1, 2, 3, 4, 5]
# l[2] = 99
# l.append(12)
# l.remove(2)
# print(l.__getitem__(1))
# print(l)
# for i in l:
#     print(i)

# ========================================

# a = {1, 2, 3, 4, 1}
# b = {3, 4, 6, 5, 7}
# a.add(7)
# # 取差集，取相同的
# print(a.intersection(b))

# ========================================

# a = {"name": "xxx", "age": 22}
# print(a["name"])
# a["x"] = "yyy"
# print(a)

# ========================================
import json

a = {"name": "xxx", "age": 22}
b = json.dumps(a)
print(b)
print(type(b))
c = json.loads(b)
print(type(c))
