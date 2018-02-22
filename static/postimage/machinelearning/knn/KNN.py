# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

import random


# 随机生成一个点
def buildpoint():
    temp = {}
    x = random.randint(0, 100)
    y = random.randint(0, 100)

    temp["x"] = x
    temp["y"] = y
    return temp


# 两点间的距离公式/欧式距离
def distance(x1, x2, y1, y2):
    distan = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distan


# 取得point与K个值的距离
def classify(K, clusters, point):
    dict = {}
    distan = {}
    for cluster in clusters:
        for key in clusters[cluster].keys():
            distan[key] = distance(clusters[cluster][key]["x"], point["x"], clusters[cluster][key]["y"], point["y"])

    # reverse=False值按照从小到大排序
    distan = sorted(distan.items(), key=lambda d: d[1], reverse=False)
    # [('E', 21.02379604162864), ('F', 21.095023109728988), ('H', 30.805843601498726), ('G', 31.622776601683793), ('D', 32.01562118716424), ('C', 32.28002478313795), ('A', 33.06055050963308), ('M', 33.734255586866), ('I', 35.805027579936315), ('J', 36.49657518178932), ('K', 40.607881008493905), ('S', 45.45327270945405), ('T', 46.61544808322666), ('X', 50.60632371551998), ('B', 51.78802950489621), ('L', 52.81098370604357), ('O', 55.362442142665635), ('P', 56.22277118748239), ('V', 60.166435825965294), ('U', 62.00806399170998), ('N', 65.29931086925804), ('Z', 65.62011886609167), ('Q', 67.47592163134935), ('R', 68.9492567037528), ('Y', 73.40980860893181), ('W', 75.15317691222374)]
    for i in range(K):
        key = distan[i][0]
        value = distan[i][1]
        dict[key] = value
    # {'H': 30.805843601498726, 'E': 21.02379604162864, 'F': 21.095023109728988}
    return dict


def judgecluster(dict, clusters):
    newdict = {}
    for cluster in clusters:
        for key in dict.keys():
            if key in clusters[cluster]:
                if cluster in newdict:
                    newdict[cluster] += 1
                else:
                    newdict[cluster] = 1

    newdict = sorted(newdict.items(), key=lambda d: d[1], reverse=True)
    print("Point属于分簇" + str(newdict[0][0]))
    print(newdict)
    # [('cluster2', 3), ('cluster1', 2)]
    # [('cluster2', 2), ('cluster1', 1)]
    return newdict


if __name__ == '__main__':
    K = 3

    clusters = {
        'cluster2': {'H': {'y': 25, 'x': 27}, 'F': {'y': 30, 'x': 36}, 'G': {'y': 14, 'x': 31}, 'A': {'y': 34, 'x': 24},
                     'D': {'y': 33, 'x': 25}, 'I': {'y': 11, 'x': 28}, 'C': {'y': 23, 'x': 26}, 'E': {'y': 23, 'x': 38},
                     'B': {'y': 23, 'x': 6}, 'L': {'y': 15, 'x': 7}, 'K': {'y': 25, 'x': 17}, 'M': {'y': 39, 'x': 24},
                     'J': {'y': 26, 'x': 21}},
        'cluster1': {'R': {'y': 97, 'x': 80}, 'N': {'y': 82, 'x': 99}, 'U': {'y': 81, 'x': 95}, 'V': {'y': 88, 'x': 79},
                     'O': {'y': 85, 'x': 73}, 'Y': {'y': 99, 'x': 87}, 'X': {'y': 72, 'x': 88},
                     'Q': {'y': 84, 'x': 100}, 'T': {'y': 70, 'x': 84}, 'W': {'y': 100, 'x': 89},
                     'S': {'y': 67, 'x': 86}, 'Z': {'y': 97, 'x': 66}, 'P': {'y': 88, 'x': 62}}}

    point = buildpoint()
    dict = classify(K, clusters, point)

    judgecluster(dict, clusters)
