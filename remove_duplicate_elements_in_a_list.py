l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = list(set(l1))

# 保持原来顺序, set去重, 转为list后使用sort排序
l3 = list(set(l1)).sort(key=l1.index)

# set去重, 对set使用sorted排序, 因为sorted返回的就是list, 节省了list()的调用
l4 = sorted(set(l1), key=l1.index)

# 列表推导式
l5 = []
l5 = [i for i in l1 if i not in l5]
