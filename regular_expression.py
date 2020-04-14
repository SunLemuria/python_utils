import re


a = "abbbccc"

# 不管有多少个b, 替换成一个
re.sub(r'b+', 'b', a)
