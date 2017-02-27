---
layout: post
categories: [机器学习]
title: 用sklearn封装的kmeans库
date: 2017-02-26
author: TTyb
desc: "由于需要海量的进行聚类，所以将 `k-means` 算法自我封装成一个方便利用的库"
---

由于需要海量的进行聚类，所以将 `k-means` 算法自我封装成一个方便利用的库，可以直接调用得到最优的 `k值` 和 `中心点`：

```
#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

# k-means算法

import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics


def calckmean(array, karr):
    # array是一个二维数组
    # X = [[1, 2, 3, 4], [5, 6, 7, 8], [3, 4, 5, 6]]

    # k是待选取K值的数组
    # karr = [2, 3, 4, 5, 8,...]

    # 将原始数据由数组变成矩阵

    x = np.array(array)

    # 用来储存轮廓系数的数组
    score = []
    # 用来储存中心坐标点的数组
    point = []

    for k in karr:
        kmeans_model = KMeans(n_clusters=k).fit(x)
        # title = 'K = %s, 轮廓系数 = %.03f' % (k, metrics.silhouette_score(X, kmeans_model.labels))
        # print(title)

        # 获取中心点的坐标
        counter_point = kmeans_model.cluster_centers_
        # print("k=" + str(k) + "时的中心点为" + "\n" + str(counter_point))

        # 记录分数
        # print(metrics.silhouette_score(x, kmeans_model.labels_))
        score.append("%.03f" % (metrics.silhouette_score(x, kmeans_model.labels_)))
        # 记录中心坐标
        point.append(counter_point)

    # 返回轮廓系数最大的k值和坐标
    maxscore = max(score, default=0)

    for i in range(0, len(score)):
        if maxscore == score[i]:
            return karr[i], point[i]

```

调用的时候直接可以：

`from kmeans import *`

测试数据：

```
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

k, point = calckmean(a, karr)
print("最好的可以分成" + str(k) + "个簇，中心点为" + "\n" + str(point))

```

![](http://images2015.cnblogs.com/blog/996148/201702/996148-20170226101819554-1837598147.png)

源文件可以在我的github下载：

[TTyb](https://github.com/TTyb/kmeans)