# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

import random


# 生成坐标字典
def buildclusters():
    clusters = {}
    keys = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # 生成第一个分簇坐标
    for i in range(0, 9):
        # A-I
        temp = {}
        x = random.randint(0, 40)
        y = random.randint(0, 40)
        temp["x"] = x
        temp["y"] = y
        clusters[keys[i]] = temp

    # 生成第二个分簇坐标
    for i in range(9, 18):
        # J-R
        temp = {}
        x = random.randint(60, 100)
        y = random.randint(0, 40)
        temp["x"] = x
        temp["y"] = y
        clusters[keys[i]] = temp

    # 生成第三个分簇坐标
    for i in range(18, 26):
        # S-Z
        temp = {}
        x = random.randint(40, 60)
        y = random.randint(60, 100)
        temp["x"] = x
        temp["y"] = y
        clusters[keys[i]] = temp
    # {'K': {'y': 34, 'x': 81}, 'V': {'y': 68, 'x': 50}, 'G': {'y': 1, 'x': 10}, 'C': {'y': 2, 'x': 9}, 'T': {'y': 78, 'x': 40}, 'A': {'y': 20, 'x': 12}, 'B': {'y': 21, 'x': 39}, 'N': {'y': 37, 'x': 67}, 'S': {'y': 92, 'x': 56}, 'Q': {'y': 7, 'x': 62}, 'D': {'y': 18, 'x': 4}, 'E': {'y': 0, 'x': 38}, 'Z': {'y': 92, 'x': 46}, 'H': {'y': 30, 'x': 32}, 'I': {'y': 21, 'x': 35}, 'U': {'y': 71, 'x': 51}, 'L': {'y': 1, 'x': 96}, 'W': {'y': 99, 'x': 59}, 'F': {'y': 10, 'x': 14}, 'O': {'y': 16, 'x': 97}, 'J': {'y': 37, 'x': 76}, 'X': {'y': 86, 'x': 49}, 'Y': {'y': 67, 'x': 50}, 'P': {'y': 17, 'x': 76}, 'M': {'y': 32, 'x': 88}, 'R': {'y': 6, 'x': 70}}
    return clusters


# 两点间的距离公式/欧式距离
def distance(x1, x2, y1, y2):
    distan = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distan


# 计算各个分簇直到达到分簇的效果
def splitcluster(clusters):
    dict = {}
    newdict = {}
    arr = []
    i = 1
    for key1 in clusters:
        temp = {}
        for key2 in clusters:
            if key1 != key2:
                if key1 in arr or key2 in arr:
                    pass
                else:
                    name = str(key1 + "->" + key2)
                    temp[name] = distance(clusters[key1]["x"], clusters[key2]["x"], clusters[key1]["y"],
                                          clusters[key2]["y"])
                    arr.append(key1)
                    arr.append(key2)

        if temp:
            # reverse=False值按照从小到大排序
            temp = sorted(temp.items(), key=lambda d: d[1], reverse=False)
            newdict[temp[0][0]] = temp[0][1]

    newdict = sorted(newdict.items(), key=lambda d: d[1], reverse=False)
    for item in newdict:
        name = "cluster" + str(i)
        i += 1

        dict[name] = item[0]

    # {'cluster13': 'B->T', 'cluster11': 'U->M', 'cluster10': 'Z->H', 'cluster5': 'L->D', 'cluster1': 'F->E', 'cluster4': 'G->A', 'cluster12': 'I->S', 'cluster3': 'W->V', 'cluster8': 'C->R', 'cluster9': 'P->X', 'cluster2': 'K->N', 'cluster7': 'O->Q', 'cluster6': 'Y->J'}
    return dict


# 判断分簇
def judgecluster(clusters, firstcluster, K):
    dict = {}
    i = 1
    arr = []
    for item in firstcluster:
        temparr = firstcluster[item].split("->")
        distan = {}
        for judge in temparr:
            if judge in arr:
                pass
            else:
                for value in clusters:
                    if value in temparr:
                        pass
                    elif value in arr:
                        pass
                    else:
                        for key in temparr:
                            name = value + "->" + key
                            distan[name] = distance(clusters[key]["x"], clusters[value]["x"], clusters[key]["y"],
                                                    clusters[value]["y"])
                            if key in arr:
                                pass
                            else:
                                arr.append(key)
        if distan:
            distan = sorted(distan.items(), key=lambda d: d[1], reverse=False)
            # print(distan)
            element = distan[0][0].split("->")[0]
            for ele in firstcluster:
                elearr = firstcluster[ele].split("->")
                if element in elearr:
                    values = firstcluster[item]
                    for va in elearr:
                        values = values + "->" + va
                        arr.append(va)
            cluster = "cluster" + str(i)
            i += 1
            dict[cluster] = values

    if len(arr) != 26:
        # 生成26个字母
        letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        # 得到剩下没有被放到dict的字母
        remain = []
        for letter in letters:
            if letter in arr:
                pass
            else:
                remain.append(letter)
        dis = {}
        for letter in remain:
            for item in dict:
                elearr = dict[item].split("->")
                for ele in elearr:
                    name = letter + "->" + ele
                    dis[name] = distance(clusters[letter]["x"], clusters[ele]["x"], clusters[letter]["y"],
                                         clusters[ele]["y"])
        if dis:
            dis = sorted(dis.items(), key=lambda d: d[1], reverse=False)
            element = dis[0][0].split("->")

            for cluster in dict:
                array = dict[cluster].split("->")
                for item in element:
                    if item in array:
                        values = "->".join(remain)
                        dict[cluster] = dict[cluster] + "->" + values

    if len(dict) == K:
        print(dict)
        # {'cluster1': 'M->X->P->Y->J->U->T->R->L->O', 'cluster3': 'V->B->W->N->E->A->I->G', 'cluster2': 'C->H->Q->F->D->S->Z->K'}
        return dict
    else:
        judgecluster(clusters, dict, K)


if __name__ == '__main__':
    K = 3
    clusters = buildclusters()
    firstcluster = splitcluster(clusters)
    judgecluster(clusters, firstcluster, K)
