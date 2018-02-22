# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

import random


# 生成坐标字典
def buildclusters():
    clusters = {}
    keys = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # 生成小数坐标
    for i in range(0, int(len(keys) / 2)):
        temp = {}
        x = random.randint(0, 40)
        y = random.randint(0, 40)
        temp["x"] = x
        temp["y"] = y
        clusters[keys[i]] = temp

    # 生成大数坐标
    for i in range(int(len(keys) / 2), int(len(keys))):
        temp = {}
        x = random.randint(60, 100)
        y = random.randint(60, 100)
        temp["x"] = x
        temp["y"] = y
        clusters[keys[i]] = temp
    # {'V': {'y': 81, 'x': 61}, 'H': {'y': 19, 'x': 37}, 'X': {'y': 93, 'x': 66}, 'S': {'y': 81, 'x': 89}, 'E': {'y': 23, 'x': 39}, 'T': {'y': 81, 'x': 70}, 'Q': {'y': 87, 'x': 96}, 'K': {'y': 39, 'x': 37}, 'A': {'y': 14, 'x': 7}, 'B': {'y': 6, 'x': 17}, 'I': {'y': 15, 'x': 32}, 'W': {'y': 83, 'x': 78}, 'J': {'y': 20, 'x': 21}, 'R': {'y': 81, 'x': 74}, 'Y': {'y': 89, 'x': 65}, 'M': {'y': 1, 'x': 24}, 'Z': {'y': 62, 'x': 78}, 'D': {'y': 0, 'x': 0}, 'U': {'y': 65, 'x': 98}, 'O': {'y': 73, 'x': 75}, 'C': {'y': 8, 'x': 20}, 'F': {'y': 36, 'x': 38}, 'L': {'y': 38, 'x': 12}, 'G': {'y': 34, 'x': 10}, 'P': {'y': 69, 'x': 90}}
    return clusters


# 生成k个簇的质点/这里是以某个点为质点
def buildcluster(K):
    centroids = {}
    dic = buildclusters()
    keys = []
    for temp in dic.keys():
        keys.append(temp)

    for i in range(K):
        rand = random.randint(0, len(keys) - 1)
        name = "P" + str(i + 1)
        centroids[name] = dic[keys[rand]]
    # {'P1': {'y': 81, 'x': 79}, 'P2': {'y': 18, 'x': 5}}

    return centroids


# 两点间的距离公式/欧式距离
def distance(x1, x2, y1, y2):
    distan = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distan


# 最小值的键值
def minkey(dict):
    dict = sorted(dict.items(), key=lambda d: d[1], reverse=True)
    # {'P1': 5.385164807134504, 'P2': 6.708203932499369}
    # P1
    return dict[-1][0]


# 分簇/簇点距离哪个质心最近就属于哪个质心的
def splitcluster(centroids, clusters, K):
    # 分好的簇
    newclusters = {}
    # 新的质点
    newcentroids = {}

    # 分簇
    # 26个点距离哪个质点的距离小
    for key_clu in clusters.keys():
        distan = {}
        for key_cen in centroids.keys():
            distan[key_cen] = distance(centroids[key_cen]["x"], clusters[key_clu]["x"], centroids[key_cen]["y"],
                                       clusters[key_clu]["y"])
        # 最小值的键值
        name = "cluster" + minkey(distan).replace("P", "")
        # 构造新字典
        temp1 = clusters[key_clu]
        try:
            newclusters[name][key_clu] = temp1
        except:
            temp2 = {}
            temp2[key_clu] = temp1
            newclusters[name] = temp2
    # print(newclusters)
    # {'cluster2': {'J': {'x': 0, 'y': 36}, 'V': {'x': 72, 'y': 98}, 'N': {'x': 82, 'y': 71}, 'P': {'x': 82, 'y': 73}, 'Q': {'x': 93, 'y': 81}, 'X': {'x': 68, 'y': 89}, 'R': {'x': 65, 'y': 60}, 'Z': {'x': 74, 'y': 89}, 'S': {'x': 99, 'y': 99}, 'D': {'x': 20, 'y': 40}, 'O': {'x': 72, 'y': 66}, 'W': {'x': 89, 'y': 82}}, 'cluster1': {'A': {'x': 37, 'y': 1}, 'E': {'x': 16, 'y': 4}, 'M': {'x': 18, 'y': 2}, 'I': {'x': 3, 'y': 11}, 'H': {'x': 2, 'y': 2}, 'L': {'x': 39, 'y': 27}, 'T': {'x': 97, 'y': 60}, 'U': {'x': 98, 'y': 72}, 'K': {'x': 21, 'y': 10}, 'C': {'x': 1, 'y': 16}, 'G': {'x': 31, 'y': 19}, 'B': {'x': 5, 'y': 22}, 'Y': {'x': 76, 'y': 62}, 'F': {'x': 11, 'y': 1}}}

    # 更新质点
    i = 0
    for key in newclusters.keys():
        tempdict = getnewcentroids(newclusters[key])
        name = "P" + str(i + 1)
        newcentroids[name] = tempdict
        i += 1

    # 质点从差值
    difference = centroidsoffset(centroids, newcentroids)

    return newclusters, newcentroids, difference


# 根据簇的坐标得到新的质点
def getnewcentroids(dict):
    centroids = {}
    x = 0
    y = 0
    for key in dict.keys():
        x += dict[key]["x"]
        y += dict[key]["y"]
    centroids["x"] = x / len(dict)
    centroids["y"] = y / len(dict)

    return centroids


# 得到质点差值
def centroidsoffset(centroids, newcentroids):
    sum = 0
    for key in centroids.keys():
        sum += distance(centroids[key]["x"], newcentroids[key]["x"], centroids[key]["y"], newcentroids[key]["y"])
    return sum


if __name__ == '__main__':
    K = 2
    clusters = buildclusters()
    centroids = buildcluster(K)
    newclusters, newcentroids, difference = splitcluster(centroids, clusters, K)
    tempdiff = difference

    while True:
        newclusters, newcentroids, newdifference = splitcluster(newcentroids, clusters, K)
        if tempdiff == newdifference:
            print(newclusters)
            print(newcentroids)
            print(newdifference)
            break
        else:
            tempdiff = newdifference
            splitcluster(newcentroids, clusters, K)
# {'cluster1': {'I': {'x': 10, 'y': 39}, 'H': {'x': 29, 'y': 38}, 'J': {'x': 26, 'y': 0}, 'A': {'x': 31, 'y': 21}, 'B': {'x': 0, 'y': 31}, 'G': {'x': 4, 'y': 25}, 'L': {'x': 10, 'y': 24}, 'C': {'x': 8, 'y': 4}, 'E': {'x': 10, 'y': 26}, 'K': {'x': 14, 'y': 13}, 'D': {'x': 33, 'y': 0}, 'F': {'x': 23, 'y': 19}, 'M': {'x': 26, 'y': 26}}, 'cluster2': {'T': {'x': 99, 'y': 76}, 'U': {'x': 68, 'y': 80}, 'Q': {'x': 77, 'y': 78}, 'V': {'x': 93, 'y': 80}, 'P': {'x': 85, 'y': 97}, 'Y': {'x': 81, 'y': 75}, 'N': {'x': 60, 'y': 75}, 'O': {'x': 64, 'y': 70}, 'R': {'x': 88, 'y': 66}, 'X': {'x': 70, 'y': 60}, 'Z': {'x': 87, 'y': 82}, 'W': {'x': 63, 'y': 88}, 'S': {'x': 89, 'y': 71}}}
# {'P1': {'x': 17.23076923076923, 'y': 20.46153846153846}, 'P2': {'x': 78.76923076923077, 'y': 76.76923076923077}}
# 0.0