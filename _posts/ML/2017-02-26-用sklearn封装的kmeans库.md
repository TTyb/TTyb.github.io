---
layout: post
categories: [ML]
title: 用sklearn封装的kmeans库
date: 2017-02-26
author: TTyb
desc: "由于需要海量的进行聚类，所以将 `k-means` 算法自我封装成一个方便利用的库"
---

由于需要海量的进行聚类，所以将 `k-means` 算法自我封装成一个方便利用的库，可以直接调用得到最优的 `k值` 和 `中心点`：

~~~ruby
#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# k-means算法

import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics

# sklearn官方文档
# http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
def calckmean(array, karr):
    # array是一个二维数组
    # X = X = [[1, 1], [2, 3], [3, 2], [1, 2], [5, 8], [6, 6], [5, 7], [5, 6], [6, 7], [7, 1], [8, 2], [9, 1], [7, 1], [9, 3]]

    # k是待选取K值的数组
    # karr = [2, 3, 4, 5, 8,...]

    # 将原始数据由数组变成矩阵

    x = np.array(array)

    # 用来储存轮廓系数的数组
    score = []
    # 用来储存中心坐标点的数组
    point = []
    # 用来储存各个簇的坐标
    coordinates = []
    # 用来储存各个簇点的与中心的距离
    distances = []

    for k in karr:
        # n_clusters为聚类的个数
        # max_iter为迭代的次数，这里设置最大迭代次数为300
        # n_init=10使用不同质心种子运行k-means算法的次数
        kmeans_model = KMeans(n_clusters=k, max_iter=300,n_init=10).fit(x)
        # title = 'K = %s, 轮廓系数 = %.03f' % (k, metrics.silhouette_score(X, kmeans_model.labels))
        # print(title)

        # 获取中心点的坐标
        counter_point = kmeans_model.cluster_centers_
        # print("k=" + str(k) + "时的中心点为" + "\n" + str(counter_point))

        # 记录分数
        # print(metrics.silhouette_score(x, kmeans_model.labels_,metric='euclidean'))
        score.append("%.03f" % (metrics.silhouette_score(x, kmeans_model.labels_)))
        # 记录中心坐标
        point.append(counter_point)

        # 将坐标属于哪个簇的标签储存到数组
        # k = 3 : [0 0 0 0 2 2 2 2 2 1 1 1 1 1]
        # k = 4 : [1 1 1 1 0 0 0 0 0 3 2 2 3 2]
        coordinates.append(kmeans_model.labels_)

        # 每个点和中心点的距离
        distances.append(KMeans(n_clusters=k, max_iter=300).fit_transform(x))

    # 返回轮廓系数最大的k值\中心坐标\分簇坐标
    maxscore = max(score, default=0)

    for i in range(0, len(score)):
        if maxscore == score[i]:
            # 储存分簇坐标的数组
            coordinate = []
            # 储存簇点与中心点的距离数组
            distance = []
            for j in range(0, len(point[i])):
                # 这里是得到分簇坐标
                tempcoor = []
                for item in zip(coordinates[i], array):
                    if item[0] == j:
                        tempcoor.append(item[1])
                coordinate.append(tempcoor)
                # 得到的样式为k=3，每个簇点的坐标群
                # [[[7, 1], [8, 2], [9, 1], [7, 1], [9, 3]],
                # [[5, 8], [6, 6], [5, 7], [5, 6], [6, 7]],
                # [[1, 1], [2, 3], [3, 2], [1, 2]]]

                # 这里是得到分簇与中心点的距离
                tempdis = []
                for item in zip(coordinates[i], distances[i]):
                    if item[0] == j:
                        tempdis.append(min(item[1]))
                distance.append(tempdis)
                # 得到k=3的各个簇点对中心的距离
                # [[1.1661903789690597, 0.39999999999999575, 1.166190378969066, 1.1661903789690597, 1.7204650534085277],
                # [1.2649110640673495, 0.9999999999999858, 0.4472135954999452, 0.8944271909999063, 0.6324555320336579],
                # [1.25, 1.0307764064044151, 1.25, 0.75]]

            # 得到k=3的中心点
            # [[8.0, 1.6],
            # [5.4, 6.8],
            # [1.75, 2.0]]
            return karr[i], point[i], coordinate, distance

~~~

调用的时候直接可以：

`from kmeans import *`

测试数据：

~~~ruby
#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from kmeans import *

x1 = np.array([1, 2, 3, 1, 5, 6, 5])
x2 = np.array([1, 3, 2, 2, 8, 6, 7])

# a = [[1, 2, 3, 1, 5, 6, 5], [1, 3, 2, 2, 8, 6, 7], [3, 5, 9, 4, 7, 6, 1], [1, 5, 3, 4, 8, 6, 7], [5, 1, 2, 3, 6, 9, 4],[8, 4, 6, 2, 1, 6, 3]]
a = [[1, 1], [2, 3], [3, 2], [1, 2], [5, 8], [6, 6], [5, 7], [5, 6], [6, 7], [7, 1], [8, 2], [9, 1], [7, 1], [9, 3]]
karr = [2, 3, 4, 5, 8]
# print(np.array(a))
# print(list(zip(x1, x2)))

K, point, coordinate, distance = calckmean(X, tests)
print("------------------------")
print("k=" + str(K) + "时的中心点为" + "\n" + str(point) + "\n" + "各个簇点为" + "\n" + str(coordinate))
print(distance)

~~~

<p style="text-align:center"><img src="/static/postimage/machinelearning/sklearnkmeans/996148-20170226101819554-1837598147.png" class="img-responsive"style="display: block; margin-right: auto; margin-left: auto;"></p>
