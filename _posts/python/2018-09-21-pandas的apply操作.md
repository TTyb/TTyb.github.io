---
layout: post
categories: [python]
title: pandas的apply操作
date: 2018-09-21
author: TTyb
desc: "pandas的apply操作类似于Scala的udf一样方便"
---

pandas的apply操作类似于Scala的udf一样方便，假设存在如下`dataframe`：

~~~ruby
  id_part                  pred               pred_class v_id
0       d  [0.722817, 0.650064]                  cat,dog   d1
1       5  [0.119208, 0.215449]  other_label,other_label   d2
~~~

需要把 `v_id=d1` 中，`pred` 与 `pred_class` 一一对应，需要将 `pred` 大于0.5的`pred_class`取出来作为新的一列，如果小于0.5则不取出来：

~~~ruby
import pandas as pd


# 提取类别
def get_pred_class(pred_class, pred):
    pred_class_list = pred_class.split(",")
    result_class_list = []
    for i in range(0, len(pred)):
        if float(pred[i]) >= 0.5:
            result_class_list.append(pred_class_list[pred.index(pred[i])])
    return result_class_list


# 新建一个dataframe
data = pd.DataFrame({
    'v_id': ["d1", 'd2'],
    'pred_class': ["cat,dog", 'other_label,other_label'],
    'pred': [[0.722817,0.650064], [0.119208,0.215449]],
    'id_part': ["d", '5'],
})

df = data.copy()
df["pos_labels"] = data.apply(lambda row: get_pred_class(row['pred_class'], row['pred']), axis=1)
print(df)
~~~

得到结果为：

~~~ruby
  id_part                  pred               pred_class v_id  pos_labels
0       d  [0.722817, 0.650064]                  cat,dog   d1  [cat, dog]
1       5  [0.119208, 0.215449]  other_label,other_label   d2          []
~~~

PS：如果没有`df = data.copy()`将会出现错误：

~~~ruby
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead
~~~