# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

from collections import Counter


# 遍历数据，进行计数
def countitem(array):
    temp = []
    for item in array:
        for value in item:
            temp.append(value)

    # 写入字典
    dict = {}
    for key in Counter(temp).keys():
        dict[key] = Counter(temp)[key]

    # {'G': 2, 'B': 7, 'D': 6, 'A': 3, 'E': 4, 'C': 8, 'F': 1}
    return dict


# 删除支持度不够的key
def deletekey(dict, support):
    temp = dict.copy()
    detele = []
    for key in dict.keys():
        if dict[key] < support:
            temp.pop(key)
            detele.append(key)
    # {'A': 3, 'B': 7, 'E': 4, 'D': 6, 'C': 8}
    # ['F', 'G']
    return temp, detele


# 得到从大到小排序的数组
def sorfarray(array, dict, delect):
    newarray = []
    # 删除支持度不够的元素
    for item in array:
        temp = {}
        for value in item:
            if value in delect:
                pass
            else:
                # 排除被删除的元素
                # [['E', 'B', 'C'], ['D', 'C'], ['B', 'A', 'C'], ['B', 'D'], ['D', 'C', 'B'], ['E', 'A', 'C'], ['D', 'C'], ['A', 'E', 'B'], ['B', 'C', 'D'], ['E', 'C', 'B', 'D']]
                temp[value] = dict[value]
        temp = sorted(temp.items(), key=lambda d: d[1], reverse=True)
        # 排序后得到
        # [('C', 8), ('B', 7), ('E', 4)]
        # [('C', 8), ('D', 6)]
        # [('C', 8), ('B', 7), ('A', 3)]
        # [('B', 7), ('D', 6)]
        # [('C', 8), ('B', 7), ('D', 6)]
        # [('C', 8), ('E', 4), ('A', 3)]
        # [('C', 8), ('D', 6)]
        # [('B', 7), ('E', 4), ('A', 3)]
        # [('C', 8), ('B', 7), ('D', 6)]
        # [('C', 8), ('B', 7), ('D', 6), ('E', 4)]
        # temp[0][0] = C
        tem = []
        for tuple in temp:
            tem.append(tuple[0])
        newarray.append(tem)
    # 得到排序后的新数组
    # [['C', 'B', 'E'], ['C', 'D'], ['C', 'B', 'A'], ['B', 'D'], ['C', 'B', 'D'], ['C', 'E', 'A'], ['C', 'D'], ['B', 'E', 'A'], ['C', 'B', 'D'], ['C', 'B', 'D', 'E']]
    return newarray


# info里面元素的种类
def getkinds(array):
    temp = []
    for item in array:
        for value in item:
            if value in temp:
                pass
            else:
                temp.append(value)
    # ['C', 'B', 'E', 'D', 'A']
    # ['A', 'B', 'C', 'D', 'E']
    return sorted(temp)


# 得到每一个种类的所有路径
def getrootpath(kinds, newinfo, dict):
    allinfo = {}
    for kind in kinds:
        kindarr = []
        for item in newinfo:
            # 如果这一条路径包含某个种类
            itemarr = []
            if kind in item:
                for value in item:
                    if kind == value:
                        break
                    else:
                        itemarr.append(value)
            if itemarr:
                kindarr.append(itemarr)
        # print(kind, kindarr)
        # A [[('C', 8), ('B', 7)], [('C', 8), ('E', 4)], [('B', 7), ('E', 4)]]
        # B [[('C', 8)], [('C', 8)], [('C', 8)], [('C', 8)], [('C', 8)]]
        # C []
        # D [[('C', 8)], [('B', 7)], [('C', 8), ('B', 7)], [('C', 8)], [('C', 8), ('B', 7)], [('C', 8), ('B', 7)]]
        # E [[('C', 8), ('B', 7)], [('C', 8)], [('B', 7)], [('C', 8), ('B', 7), ('D', 6)]]
        allinfo[kind] = kindarr

    return allinfo


# 得到所有组合的字典
def getrange(rootpath):
    alldict = {}
    for key in rootpath.keys():
        root = rootpath[key]
        # 一个元素的路径
        onearr = []
        dict = {}

        # 实现一个元素路径
        for item in root:
            for value in item:
                onearr.append(value)
                dict[value] = onearr.count(value)
        alldict[key] = dict
        # {'B': {'C': 5}, 'C': {}, 'E': {'C': 3, 'B': 3, 'D': 1}, 'A': {'E': 2, 'C': 2, 'B': 2}, 'D': {'C': 5, 'B': 4}}

        # 实现两个元素路径
        for item1 in root:
            tempdict = {}
            for item2 in root:
                if item1 == item2:
                    if len(item1) > 1:
                        x = "".join(item1)
                        if x in tempdict.keys():
                            tempdict[x] += 1
                        else:
                            tempdict[x] = 1
            # print(tempdict)
            if tempdict:
                for x in tempdict:
                    alldict[key][x] = tempdict[x]
    # print(alldict)
    # {'D': {'CB': 3, 'C': 5, 'B': 4}, 'A': {'E': 2, 'B': 2, 'CB': 1, 'C': 2, 'BE': 1, 'CE': 1}, 'E': {'D': 1, 'C': 3, 'CB': 1, 'B': 3, 'CBD': 1}, 'B': {'C': 5}, 'C': {}}

    return alldict


# 得到每个种类的置信度
def confidence(alldict, support, newinfo):
    newdict = {}
    for kind in alldict:
        copydict = alldict[kind].copy()
        for key in alldict[kind]:
            if alldict[kind][key] < support:
                copydict.pop(key)
        if copydict:
            newdict[kind] = copydict
    # print(newdict)
    # {'E': {'C': 3, 'B': 3}, 'B': {'C': 5}, 'D': {'C': 5, 'CB': 3, 'B': 4}}

    # 计算置信度
    for kind in newdict:
        for key in newdict[kind].keys():
            tempnum = newdict[kind][key]
            denominator = 0
            for item in newinfo:
                if len(key) == 1:
                    if key in item:
                        denominator += 1
                elif len(key) == 2:
                    if key[0] in item and key[1] in item:
                        denominator += 1
                elif len(key) == 3:
                    if key[0] in item and key[1] in item and key[2] in item:
                        denominator += 1

            newdict[kind][key] = str(tempnum) + "/" + str(denominator)
    # {'E': {'B': '3/7', 'C': '3/8'}, 'B': {'C': '5/8'}, 'D': {'B': '4/7', 'C': '5/8', 'CB': '3/5'}}
    # 买了C人，有3/8概率买E，有5/8概率买B，有5/8概率买D，且买了C又买了B的人有3/5的概率买D
    return newdict


if __name__ == '__main__':
    support = 3
    info = [["E", "B", "C"], ["D", "C"], ["B", "A", "C"], ["B", "D"], ["D", "F", "C", "B"], ["E", "A", "C", "G"],
            ["D", "G", "C"], ["A", "E", "B"], ["B", "C", "D"], ["E", "C", "B", "D"]]

    # 遍历数据，进行计数
    dict = countitem(info)
    # 删除支持度不够的key
    dict, delete = deletekey(dict, support)
    # 得到从大到小排序的数组
    newinfo = sorfarray(info, dict, delete)
    # info里面元素的种类
    kinds = getkinds(newinfo)
    # 得到每一个种类的所有路径
    rootpath = getrootpath(kinds, newinfo, dict)
    # 得到所有组合的字典
    alldict = getrange(rootpath)
    # 得到每个种类的置信度
    confidence(alldict, support, newinfo)
