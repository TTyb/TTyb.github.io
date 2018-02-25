---
layout: post
categories: [ML]
title: NaiveBayes朴素贝叶斯算法
date: 2017-01-16
author: TTyb
desc: "最为广泛的两种分类模型是决策树模型(Decision Tree Model)和朴素贝叶斯模型（Naive Bayesian Model，NBM），本文讲解朴素贝叶斯"
---

最为广泛的两种分类模型是 [决策树模型(Decision Tree Model)](https://ttyb.github.io/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/ID3%E5%86%B3%E7%AD%96%E6%A0%91%E7%AE%97%E6%B3%95.html) 和 [朴素贝叶斯模型（Naive Bayesian Model，NBM）]()。

### 朴素贝叶斯算法思路

朴素贝叶斯法是基于 `贝叶斯定理与特征条件独立假设` 的分类方法，按照以前 [决策树](https://ttyb.github.io/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/ID3%E5%86%B3%E7%AD%96%E6%A0%91%E7%AE%97%E6%B3%95.html) 的数据，利用朴素贝叶斯进行分类：

假设存在如下一组信息：


| 天气 | 气温 | 湿度 |  风  | 外出 |
|:----:|:----:|:----:|:----:|:----:|
| 晴朗 | 高温 |  高  | 无风 |  no  |
| 晴朗 | 高温 |  高  | 有风 |  no  |
| 多云 | 高温 |  高  | 无风 |  yes |
| 下雨 | 温暖 |  高  | 无风 |  yes |
| 下雨 | 寒冷 | 正常 | 无风 |  yes |
| 下雨 | 寒冷 | 正常 | 有风 |  no  |
| 多云 | 寒冷 | 正常 | 有风 |  yes |
| 晴朗 | 温暖 |  高  | 无风 |  no  |
| 晴朗 | 寒冷 | 正常 | 无风 |  yes |
| 下雨 | 温暖 | 正常 | 无风 |  yes |
| 晴朗 | 温暖 | 正常 | 有风 |  yes |
| 多云 | 温暖 |  高  | 有风 |  yes |
| 多云 | 高温 | 正常 | 无风 |  yes |
| 下雨 | 温暖 |  高  | 有风 |  no  |


将上面的表格整理一下如下：


|天气|yes | no |气温|yes | no |湿度|yes | no | 风 |yes | no |外出|yes | no |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|晴朗| 2  | 3  |高温| 2  | 2  | 高 | 3  | 4  |无风| 6  | 2  |外出| 9  | 5  |
|多云| 4  | 0  |温暖| 4  | 2  |正常| 6  | 1  |有风| 3  | 3  |    |    |    |
|下雨| 3  | 2  |寒冷| 3  | 1  |    |    |    |    |    |    |    |    |    |


假设所有的变量都是 `独立的` ，那么在以下天气中是否该外出：

~~~ruby
evidence = ['晴朗', '寒冷', '高', '有风']
~~~

将上述事件记为 `E` ， `E = [E1, E2, E3, E4]` , 当A、B相互独立时，由：

<p style="text-align:center"><img src="/static/postimage/machinelearning/bayes/996148-20170116102921208-348877637.png" class="img-responsive"/></p>

得贝叶斯定理：

<p style="text-align:center"><img src="/static/postimage/machinelearning/bayes/996148-20170116102942692-1121172338.png" class="img-responsive"/></p>

得：

<p style="text-align:center"><img src="/static/postimage/machinelearning/bayes/996148-20170116103248474-799840570.png" class="img-responsive"/></p>

又因为4个指标是相互独立的，所以：

<p style="text-align:center"><img src="/static/postimage/machinelearning/bayes/996148-20170116103307786-367494930.png" class="img-responsive"/></p>

带入计算得到：

~~~ruby
P(yes|E)*P(E)=2/9×3/9×3/9×3/9×9/14=0.0053
P(no|E)*P(E)=3/5×1/5×4/5×3/5×5/14=0.0206
~~~

`外出概率：0.005291005291005291，不外出概率：0.02057142857142857，不适合外出！`


### 朴素贝叶斯算法代码

朴素贝叶斯最重要的是构造 `训练样本` ，将表：


|天气|yes | no |气温|yes | no |湿度|yes | no | 风 |yes | no |外出|yes | no |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|晴朗| 2  | 3  |高温| 2  | 2  | 高 | 3  | 4  |无风| 6  | 2  |外出| 9  | 5  |
|多云| 4  | 0  |温暖| 4  | 2  |正常| 6  | 1  |有风| 3  | 3  |    |    |    |
|下雨| 3  | 2  |寒冷| 3  | 1  |    |    |    |    |    |    |    |    |    |


转化为字典：

~~~ruby
newcondition = {'高温': {'no': 0.4, 'yes': 0.2222222222222222}, '高': {'no': 0.8, 'yes': 0.3333333333333333}, '有风': {'no': 0.6, 'yes': 0.3333333333333333}, '温暖': {'no': 0.4, 'yes': 0.4444444444444444}, '多云': {'yes': 0.4444444444444444}, '寒冷': {'no': 0.2, 'yes': 0.3333333333333333}, '正常': {'no': 0.2, 'yes': 0.6666666666666666}, '下雨': {'no': 0.4, 'yes': 0.3333333333333333}, '无风': {'no': 0.4, 'yes': 0.6666666666666666}, '晴朗': {'no': 0.6, 'yes': 0.2222222222222222}}

newresult = {'no': 0.35714285714285715, 'yes': 0.6428571428571429}
~~~

最后相乘计算出概率即可：

~~~ruby
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
~~~

最终结果为：

~~~ruby
外出概率：0.005291005291005291，不外出概率：0.02057142857142857，不适合外出！
~~~

源码下载：

<a href="/static/postimage/machinelearning/bayes/NaiveBayes.py" target="_blank">NaiveBayes.py</a>