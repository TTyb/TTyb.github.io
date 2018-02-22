# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

import math
from collections import Counter


# 计算出现的概率
def CalcProbability(array):
    dict = {}
    count = Counter(array)
    for item in count:
        dict[item] = count[item] / len(array)
    return dict


# 计算信息熵
def CalcEntropy(array):
    entropy = 0
    for i in range(0, len(array)):
        entropy = entropy + (-array[i] * math.log2(array[i]))
    return entropy

# 重新整理数据
def Statistics(condition, result):
    # 获得各种结果出现的概率
    for k in result:
        resultProbability = CalcProbability(result[k])
    # {'no': 0.35714285714285715, 'yes': 0.6428571428571429}
    # 获得结果的信息熵
    resultarr = []
    for key in resultProbability:
        resultarr.append(resultProbability[key])
    resultEntropy = CalcEntropy(resultarr)
    # print(resultEntropy)
    # 0.9402859586706311


    # 统计各个条件下的外出结果
    dict = {}
    for key in condition.keys():
        tempdict = {}
        for i in range(0, len(condition[key])):
            if condition[key][i] in tempdict:
                for k in result:
                    tempdict[condition[key][i]].append(result[k][i])
            else:
                arr = []
                for k in result:
                    arr.append(result[k][i])
                tempdict[condition[key][i]] = arr
        dict[key] = tempdict
        # print(dict)
        # {'风': {'有风': ['no', 'no', 'yes', 'yes', 'yes', 'no'], '无风': ['no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes']}, '湿度': {'正常': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes'], '高': ['no', 'no', 'yes', 'yes', 'no', 'yes', 'no']}, '天气': {'晴朗': ['no', 'no', 'no', 'yes', 'yes'], '下雨': ['yes', 'yes', 'no', 'yes', 'no'], '多云': ['yes', 'yes', 'yes', 'yes']}, '气温': {'温暖': ['yes', 'no', 'yes', 'yes', 'yes', 'no'], '寒冷': ['yes', 'no', 'yes', 'yes'], '高温': ['no', 'no', 'yes', 'yes']}}
    # 计算不同外出情况下的信息熵
    newdict = {}
    for keys in dict:
        tempdict = {}
        for key in dict[keys]:
            temp = CalcProbability(dict[keys][key])
            temparr = []
            for value in temp:
                temparr.append(temp[value])
                tempdict[key] = CalcEntropy(temparr)
            newdict[keys] = tempdict
    # print(newdict)
    # {'风': {'无风': 0.8112781244591328, '有风': 1.0}, '天气': {'多云': 0.0, '晴朗': 0.9709505944546686, '下雨': 0.9709505944546686}, '湿度': {'高': 0.9852281360342516, '正常': 0.5916727785823275}, '气温': {'温暖': 0.9182958340544896, '寒冷': 0.8112781244591328, '高温': 1.0}}


    # 不同条件出现的概率
    conditiondict = {}
    for item in condition:
        conditiondict[item] = CalcProbability(condition[item])
    # print(conditiondict)
    # {'气温': {'高温': 0.2857142857142857, '温暖': 0.42857142857142855, '寒冷': 0.2857142857142857}, '风': {'有风': 0.42857142857142855, '无风': 0.5714285714285714}, '湿度': {'高': 0.5, '正常': 0.5}, '天气': {'晴朗': 0.35714285714285715, '下雨': 0.35714285714285715, '多云': 0.2857142857142857}}

    return resultEntropy, newdict, conditiondict


# 计算信息增益
def CalcGain(resultEntropy, conditionEntropy, conditionProbability):
    conditionGain = {}
    for keys in conditionEntropy:
        number = 0
        for key in conditionEntropy[keys]:
            number = number + conditionEntropy[keys][key] * conditionProbability[keys][key]
        conditionGain[keys] = resultEntropy - number
    # reverse=True值按照从大到小排序
    conditionGain = sorted(conditionGain.items(), key=lambda d: d[1], reverse=True)

    return conditionGain

# 递归计算咯
def recursion(condition, result):
    resultEntropy, conditionEntropy, conditionProbability = Statistics(condition, result)
    # print(resultEntropy)
    # print(conditionEntropy)
    # print(conditionProbability)
    conditionGain = CalcGain(resultEntropy, conditionEntropy, conditionProbability)
    # print(conditionGain)

    # 哦按段是否为零
    key = conditionGain[0][0]
    value = ""
    for values in conditionEntropy[key]:
        if conditionEntropy[key][values] == 0:
            value = values

    kinds = []
    for item in condition[key]:
        if item in kinds:
            pass
        else:
            kinds.append(item)
    # ['晴朗', '多云', '下雨']

    # 删除天气这个key
    arrcondition = condition[key]
    condition.pop(key)
    # print("sssssssss",key)
    newcondition = {}
    newresult = {}
    for item in kinds:
        dict = {}
        resultarr = []
        for i in range(0, len(arrcondition)):
            if arrcondition[i] == item:
                for keys in condition:
                    if keys in dict:
                        dict[keys].append(condition[keys][i])
                    else:
                        temparr = []
                        temparr.append(condition[keys][i])
                        dict[keys] = temparr
                for key in result:
                    resultarr.append(result[key][i])
                    newresult[item] = resultarr
            newcondition[item] = dict

    # print(newcondition)
    # {'多云': {'气温': ['高温', '寒冷', '温暖', '高温'], '风': ['无风', '有风', '有风', '无风'], '湿度': ['高', '正常', '高', '正常']}, '晴朗': {'气温': ['高温', '高温', '温暖', '寒冷', '温暖'], '风': ['无风', '有风', '无风', '无风', '有风'], '湿度': ['高', '高', '高', '正常', '正常']}, '下雨': {'气温': ['温暖', '寒冷', '寒冷', '温暖', '温暖'], '风': ['无风', '无风', '有风', '无风', '有风'], '湿度': ['高', '正常', '正常', '正常', '高']}}
    # print(newresult)
    # {'多云': ['yes', 'yes', 'yes', 'yes'], '晴朗': ['no', 'no', 'no', 'yes', 'yes'], '下雨': ['yes', 'yes', 'no', 'yes', 'no']}

    if value in newcondition:
        newcondition[value] = "yes"
    # 得到的新condition为dict：
    # '多云': 'yes'
    # 下雨 {'风': ['无风', '无风', '有风', '无风', '有风'], '湿度': ['高', '正常', '正常', '正常', '高'], '气温': ['温暖', '寒冷', '寒冷', '温暖', '温暖']}
    # 晴朗 {'风': ['无风', '有风', '无风', '无风', '有风'], '湿度': ['高', '高', '高', '正常', '正常'], '气温': ['高温', '高温', '温暖', '寒冷', '温暖']}

    # 得到的新result为newresult：
    # 多云 ['yes', 'yes', 'yes', 'yes']
    # 晴朗 ['no', 'no', 'no', 'yes', 'yes']
    # 下雨 ['yes', 'yes', 'no', 'yes', 'no']

    print(newcondition)
    tempresult = {}
    for key in newcondition:
        if key == value:
            pass
        else:
            tempresult[key] = newresult[key]
            recursion(newcondition[key], tempresult)


if __name__ == '__main__':
    condition = {'风': ['无风', '有风', '无风', '无风', '无风', '有风', '有风', '无风', '无风', '无风', '有风', '有风', '无风', '有风'],
                 '湿度': ['高', '高', '高', '高', '正常', '正常', '正常', '高', '正常', '正常', '正常', '高', '正常', '高'],
                 '天气': ['晴朗', '晴朗', '多云', '下雨', '下雨', '下雨', '多云', '晴朗', '晴朗', '下雨', '晴朗', '多云', '多云', '下雨'],
                 '气温': ['高温', '高温', '高温', '温暖', '寒冷', '寒冷', '寒冷', '温暖', '寒冷', '温暖', '温暖', '温暖', '高温', '温暖']}
    result = {'外出': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']}

    recursion(condition, result)

    '''
    resultEntropy, conditionEntropy, conditionProbability = Statistics(condition, result)
    # print(resultEntropy)
    # print(conditionEntropy)
    # print(conditionProbability)
    conditionGain = CalcGain(resultEntropy, conditionEntropy, conditionProbability)
    # print(conditionGain)

    # 哦按段是否为零
    key = conditionGain[0][0]
    value = ""
    for values in conditionEntropy[key]:
        if conditionEntropy[key][values] == 0:
            value = values

    kinds = []
    for item in condition[key]:
        if item in kinds:
            pass
        else:
            kinds.append(item)
    # ['晴朗', '多云', '下雨']

    # 删除天气这个key
    arrcondition = condition[key]
    condition.pop(key)
    newcondition = {}
    newresult = {}
    for item in kinds:
        dict = {}
        resultarr = []
        for i in range(0, len(arrcondition)):
            if arrcondition[i] == item:
                for keys in condition:
                    if keys in dict:
                        dict[keys].append(condition[keys][i])
                    else:
                        temparr = []
                        temparr.append(condition[keys][i])
                        dict[keys] = temparr
                for key in result:
                    resultarr.append(result[key][i])
                    newresult[item] = resultarr
            newcondition[item] = dict

    # print(newcondition)
    # {'多云': {'气温': ['高温', '寒冷', '温暖', '高温'], '风': ['无风', '有风', '有风', '无风'], '湿度': ['高', '正常', '高', '正常']}, '晴朗': {'气温': ['高温', '高温', '温暖', '寒冷', '温暖'], '风': ['无风', '有风', '无风', '无风', '有风'], '湿度': ['高', '高', '高', '正常', '正常']}, '下雨': {'气温': ['温暖', '寒冷', '寒冷', '温暖', '温暖'], '风': ['无风', '无风', '有风', '无风', '有风'], '湿度': ['高', '正常', '正常', '正常', '高']}}
    # print(newresult)
    # {'多云': ['yes', 'yes', 'yes', 'yes'], '晴朗': ['no', 'no', 'no', 'yes', 'yes'], '下雨': ['yes', 'yes', 'no', 'yes', 'no']}

    if value in newcondition:
        newcondition[value] = "yes"
    # 得到的新condition为dict：
    # '多云': 'yes'
    # 下雨 {'风': ['无风', '无风', '有风', '无风', '有风'], '湿度': ['高', '正常', '正常', '正常', '高'], '气温': ['温暖', '寒冷', '寒冷', '温暖', '温暖']}
    # 晴朗 {'风': ['无风', '有风', '无风', '无风', '有风'], '湿度': ['高', '高', '高', '正常', '正常'], '气温': ['高温', '高温', '温暖', '寒冷', '温暖']}

    # 得到的新result为newresult：
    # 多云 ['yes', 'yes', 'yes', 'yes']
    # 晴朗 ['no', 'no', 'no', 'yes', 'yes']
    # 下雨 ['yes', 'yes', 'no', 'yes', 'no']

    # 得到晴朗和下雨的子节点
    tempresult = {}
    for key in newcondition:
        if key == value:
            pass
        else:
            tempresult[key] = newresult[key]
            resultEntropy, conditionEntropy, conditionProbability = Statistics(newcondition[key], tempresult)
            print(resultEntropy)
            print(conditionEntropy)
            print(conditionProbability)
            conditionGain = CalcGain(resultEntropy, conditionEntropy, conditionProbability)
            print(conditionGain)
            # 晴朗：[('湿度', 0.9709505944546686), ('气温', 0.5709505944546686), ('风', 0.01997309402197489)]
            # 下雨：[('风', 0.09546184423832171), ('气温', 0.09546184423832171), ('湿度', -0.02904940554533142)]

    '''
