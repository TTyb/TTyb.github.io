# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

from collections import Counter


# 计算出现的概率
def CalcProbability(array, result):
    # 统计result的个数
    resultkey = list(result.keys())[0]
    resultcount = Counter(result[resultkey])
    # Counter({'yes': 9, 'no': 5})

    dict = {}
    count = Counter(array)
    for item in count:
        if item == "yes":
            dict[item] = count[item] / resultcount["yes"]
        elif item == "no":
            dict[item] = count[item] / resultcount["no"]
    return dict


# 重新整理数据
def Statistics(condition, result):
    # 不同条件下外出的概率
    conditiondict = {}
    # 外出
    resultkey = list(result.keys())[0]

    # 统计各种情况下外出的情况
    for item in condition:
        for i in range(0, len(condition[item])):
            conditionelement = condition[item][i]
            resultelement = result[resultkey][i]
            if conditionelement in conditiondict:
                conditiondict[conditionelement].append(resultelement)
            else:
                temparr = []
                temparr.append(resultelement)
                conditiondict[conditionelement] = temparr

    # print(conditiondict)
    # {'下雨': ['yes', 'yes', 'no', 'yes', 'no'], '寒冷': ['yes', 'no', 'yes', 'yes'], '高温': ['no', 'no', 'yes', 'yes'], '无风': ['no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes'], '晴朗': ['no', 'no', 'no', 'yes', 'yes'], '正常': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes'], '温暖': ['yes', 'no', 'yes', 'yes', 'yes', 'no'], '多云': ['yes', 'yes', 'yes', 'yes'], '高': ['no', 'no', 'yes', 'yes', 'no', 'yes', 'no'], '有风': ['no', 'no', 'yes', 'yes', 'yes', 'no']}

    # 获得各种情况下外出和不外出的概率
    newcondition = {}
    for key in conditiondict:
        newcondition[key] = CalcProbability(conditiondict[key], result)

    # 外出的概率
    newresult = {}
    resultkey = list(result.keys())[0]
    for item in result[resultkey]:
        if item in newresult:
            newresult[item] += 1
        else:
            newresult[item] = 1
    newresult["yes"] = newresult["yes"] / len(result[resultkey])
    newresult["no"] = newresult["no"] / len(result[resultkey])

    # print(newcondition)
    # {'高温': {'no': 0.4, 'yes': 0.2222222222222222}, '高': {'no': 0.8, 'yes': 0.3333333333333333}, '有风': {'no': 0.6, 'yes': 0.3333333333333333}, '温暖': {'no': 0.4, 'yes': 0.4444444444444444}, '多云': {'yes': 0.4444444444444444}, '寒冷': {'no': 0.2, 'yes': 0.3333333333333333}, '正常': {'no': 0.2, 'yes': 0.6666666666666666}, '下雨': {'no': 0.4, 'yes': 0.3333333333333333}, '无风': {'no': 0.4, 'yes': 0.6666666666666666}, '晴朗': {'no': 0.6, 'yes': 0.2222222222222222}}
    # print(newresult)
    # {'no': 0.35714285714285715, 'yes': 0.6428571428571429}
    return newcondition, newresult


# 判断是否外出
def judgeresult(newcondition, newresult, weather):
    yesresult = 1
    noresult = 1
    for item in weather:
        # 外出的概率
        yesresult = yesresult * newcondition[item]["yes"]
        noresult = noresult * newcondition[item]["no"]

    yesresult = yesresult * newresult["yes"]
    noresult = noresult * newresult["no"]

    if yesresult >= noresult:
        print("外出概率：" + str(yesresult) + "，不外出概率：" + str(noresult) + "，适合外出！")
    else:
        print("外出概率：" + str(yesresult) + "，不外出概率：" + str(noresult) + "，不适合外出！")


if __name__ == '__main__':
    condition = {'风': ['无风', '有风', '无风', '无风', '无风', '有风', '有风', '无风', '无风', '无风', '有风', '有风', '无风', '有风'],
                 '湿度': ['高', '高', '高', '高', '正常', '正常', '正常', '高', '正常', '正常', '正常', '高', '正常', '高'],
                 '天气': ['晴朗', '晴朗', '多云', '下雨', '下雨', '下雨', '多云', '晴朗', '晴朗', '下雨', '晴朗', '多云', '多云', '下雨'],
                 '气温': ['高温', '高温', '高温', '温暖', '寒冷', '寒冷', '寒冷', '温暖', '寒冷', '温暖', '温暖', '温暖', '高温', '温暖']}
    result = {'外出': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']}
    newcondition, newresult = Statistics(condition, result)
    evidence = ['晴朗', '寒冷', '高', '有风']

    judgeresult(newcondition, newresult, evidence)
