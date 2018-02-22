# !/usr/bin/python3.4
# -*- coding: utf-8 -*-


# 获取所有元素种类
def getkinds(array):
    arr = []
    for item in array:
        for value in item:
            if value in arr:
                pass
            else:
                if value != "+":
                    arr.append(value)
    return arr


# 候选集长度
def getcount(array, support):
    # 第一次扫描
    # C1
    dict = {}
    for item in array:
        for key in item:
            if key in dict.keys():
                dict[key] += 1
            else:
                dict[key] = 1
    # 第一次剪枝
    newdict = judge_spport(dict, support)

    # 第二次扫描
    # 构造项集C2
    # 两两组合
    arr = []
    kinds = getkinds(newdict.keys())
    for m in range(0, len(kinds)):
        for n in range(m + 1, len(kinds)):
            arr.append(kinds[m] + "+" + kinds[n])
    # 计数
    dict = {}
    for item in array:
        for values in arr:
            value = values.split("+")
            if value[0] in item and value[1] in item:
                if values in dict:
                    dict[values] += 1
                else:
                    dict[values] = 1
    # print(dict)
    # {'B+A': 1, 'A+E': 1, 'C+E': 2, 'B+E': 3, 'C+B': 2, 'C+A': 2}

    # 第二次剪枝
    newdict = judge_spport(dict, support)
    # print(newdict)
    # {'C+E': 2, 'B+E': 3, 'C+B': 2, 'C+A': 2}

    # 第三次扫描
    # 构造项集C2
    # 两两组合
    arr = []
    kinds = getkinds(newdict.keys())
    for m in range(0, len(kinds)):
        for n in range(m + 1, len(kinds)):
            for k in range(n + 1, len(kinds)):
                arr.append(kinds[m] + "+" + kinds[n] + "+" + kinds[k])

    # 计数
    dict = {}
    for item in array:
        for values in arr:
            value = values.split("+")
            if value[0] in item and value[1] in item and value[2] in item:
                if values in dict:
                    dict[values] += 1
                else:
                    dict[values] = 1
    # print(dict)
    # {'E+B+A': 1, 'E+C+A': 1, 'E+B+C': 2, 'B+C+A': 1}

    # 第三次剪枝
    newdict = judge_spport(dict, support)
    # {'B+E+C': 2}
    return newdict


# 剪枝
# 删除不符合支持度的key
def judge_spport(dict, support):
    dic = dict.copy()
    for key in dict.keys():
        if dict[key] < support:
            del dic[key]
    return dic

# 计算强规则
def getconfidence(dict,array):
    # 一一组合
    kinds = getkinds(dict.keys())
    arr = kinds
    newdict = {}
    for i in range(0,len(arr)):
        denominator1 = 0
        numerator1 = 0
        denominator2 = 0
        numerator2 = 0
        for item in array:
            if arr[i] in item:
                denominator1 += 1
                temp = getkinds(dict.keys())
                temp.remove(arr[i])
                if temp[0] in item and temp[1] in item:
                    numerator1 += 1
        key1 = arr[i] + "->" + temp[0] + "+" + temp[1]

        for item in array:
            temp = getkinds(dict.keys())
            temp.remove(arr[i])
            if temp[0] in item and temp[1] in item:
                numerator2 += 1
                if arr[i] in item:
                    denominator2 += 1
        key2 = temp[0] + "+" + temp[1] + "->" + arr[i]
        if denominator1 == 0:
            newdict[key1] = str(numerator1) + "denominator1"
        else:
            newdict[key1] = str(numerator1) + "/" + str(denominator1)
        if numerator2 == 0:
            newdict[key2] = str(denominator2) + "numerator2"
        else:
            newdict[key2] = str(denominator2) + "/" + str(numerator2)

    return newdict

if __name__ == '__main__':
    support = 2
    info = [["A", "C", "D"], ["B", "C", "E"], ["A", "B", "C", "E"], ["B", "E"]]
    dict = getcount(info, support)
    # print(dict)
    # {'E+C+B': 2}
    newdict = getconfidence(dict,info)
    print(newdict)
