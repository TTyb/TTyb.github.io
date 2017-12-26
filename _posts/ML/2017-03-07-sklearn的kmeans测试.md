---
layout: post
categories: [ML]
title: sklearn的kmeans测试
date: 2017-03-07
author: TTyb
desc: "sklearn的kmeans测试代码"
---

~~~ruby
#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics


font = FontProperties(fname=r"c:/Windows/Fonts/msyh.ttf", size=10)
# figsize绘图的宽度和高度，也就是像素
plt.figure(figsize=(8, 10))
# 创建3行2列，p1为第一个的图形合集
plt.subplot(3, 2, 1)
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
print(X)

# x,y轴的绘图范围
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('样本', fontproperties=font)
plt.scatter(x1, x2)
# 点的颜色
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
# 点的形状
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
# 测试的k值
tests = [2, 3, 4, 5, 8]
subplot_counter = 1
for t in tests:
    subplot_counter += 1
    plt.subplot(3, 2, subplot_counter)
    kmeans_model = KMeans(n_clusters=t).fit(X)
    #     print kmeans_model.labels_:每个点对应的标签值
    for i, l in enumerate(kmeans_model.labels_):
        plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l], ls='None')
        print(kmeans_model.labels_)
        plt.xlim([0, 10])
        plt.ylim([0, 10])
        plt.title(
            'K = %s, 轮廓系数 = %.03f' % (t, metrics.silhouette_score(X, kmeans_model.labels_, metric='euclidean')),
            fontproperties=font)
        # print(metrics.silhouette_score(X, kmeans_model.labels_))
    # 获取中心点的坐标
    counter_point = kmeans_model.cluster_centers_
    print("k=" + str(t) + "时的中心点为" + "\n" + str(counter_point))
    # print(counter_point)


plt.show()
plt.close()

~~~

<p style="text-align:center"><img src="/static/postimage/machinelearning/sklearnkmeans/996148-20170307144756406-976833755.png"/></p>