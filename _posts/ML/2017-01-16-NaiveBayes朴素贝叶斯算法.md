---
layout: post
categories: [ML]
title: NaiveBayes朴素贝叶斯算法
date: 2017-01-16
author: TTyb
desc: "最为广泛的两种分类模型是决策树模型(Decision Tree Model)和朴素贝叶斯模型（Naive Bayesian Model，NBM），本文讲解朴素贝叶斯"
---

最为广泛的两种分类模型是 [决策树模型(Decision Tree Model)](https://ttyb.github.io/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/ID3%E5%86%B3%E7%AD%96%E6%A0%91%E7%AE%97%E6%B3%95.html) 和 [朴素贝叶斯模型（Naive Bayesian Model，NBM）]()。

# 总结

>1. 贝叶斯定理是将先验概率做一次更新，得到后验概率
>2. 朴素贝叶斯是输入先验概率，找到后验概率，最后找到最大后验概率，作为最终的分类结果，以及分类概率

# 贝叶斯定理

$$ P(H|E) = \frac{P(E|H)P(H)}{P(E)} $$

## 实际问题
假设我们有两个装满了饼干的碗，第一个碗里有10个巧克力饼干和30个普通饼干，第二个碗里两种饼干都有20个。我们随机挑一个碗，再在碗里随机挑饼干。那么我们挑到的普通饼干来自一号碗的概率有多少？

## 解决方案
我们用 H1 代表一号碗，H2 代表二号碗。在H1中取到普通饼干的概率是$P(E|H1)=\frac{30}{10+30}\times\frac{1}{2}$，即抽到H1的概率是$\frac{1}{2}$，再在H1中抽到普通饼干的概率是$ \frac{30}{10+30}=\frac{3}{4} $，同理可得$ P(E|H2)=\frac{20}{20+20}\times\frac{1}{2} $。而问题中挑到挑到的普通饼干来自一号碗，已知挑到普通饼干，那么这个普通饼干来自一号碗的概率为：

$$
P(H1|E) = \frac{P(E|H1)P(H1)}{P(E)}
$$

其中拿到普通饼干的概率为：

$$P(E)=P(E|H1)P(H1)+ P(E|H2)P(H2)$$

计算为：

$$
P(H1|E) = \frac{P(E|H1)P(H1)}{P(E)}

=\frac{P(E|H1)P(H1)}{P(E|H1)P(H1)+ P(E|H2)P(H2)}

= \frac{0.75\times0.5}{0.75\times0.5+0.5\times0.5}=0.6
$$

# 朴素贝叶斯

## 实际问题

假设可疑消息中含有“sex”这个单词，平时大部分收到邮件的人都会知道，这封邮件可能是垃圾邮件。然而分类器并不知道这些，它只能计算出相应的概率。假设在用户收到的邮件中，“sex”出现在在垃圾邮件中的频率是5%，在正常邮件中出现的概率是0.5%。

我们用 S 表示垃圾邮件（spam），H 表示正常邮件（healthy）。两者的先验概率都是50%，即：$ P(S)=P(H)=\frac{1}{2} $

我们用 W 表示这个词，那么问题就变成了计算 P(S|W)的值，即已知“sex”这个次出现了，那么它出现在垃圾邮件的概率是多少。根据贝叶斯定理我们可以得到：

$$

P(S|W) = \frac{P(W|S)P(S)}{P(W|S)P(S)+P(W|H)P(H)}

=\frac{0.05\times0.5}{0.05\times0.5+0.005\times0.5}=90.9\%

$$

而 $P(W | S)$ 和 $P(W | H)$ 的含义是，这个词语在垃圾邮件和正常邮件中，分别出现的概率。通过计算可以得到 $P(S | W) = 90.9%$，说明“sex”的判断能力很强，将50%的先验概率提高到了90.9%的后验概率。

------------------------------------------
而再次计算这个“sex”出现在正常邮件的概率$P(H|W)$，计算得到为10.1%。那么假设一封邮件里面有词“sex”，那么它是垃圾邮件还是正常邮件。有上面计算得到是垃圾邮件的概率90.9%比正常邮件的概率要大，所以这个带有“sex”的邮件会被分类到垃圾邮件里面

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

<p style="text-align:center"><img src="/static/postimage/machinelearning/bayes/996148-20170116102921208-348877637.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

得贝叶斯定理：

<p style="text-align:center"><img src="/static/postimage/machinelearning/bayes/996148-20170116102942692-1121172338.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

得：

<p style="text-align:center"><img src="/static/postimage/machinelearning/bayes/996148-20170116103248474-799840570.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

又因为4个指标是相互独立的，所以：

<p style="text-align:center"><img src="/static/postimage/machinelearning/bayes/996148-20170116103307786-367494930.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

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