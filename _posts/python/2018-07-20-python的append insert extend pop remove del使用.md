---
layout: post
categories: [python]
title: python的append insert extend pop del remove使用
date: 2018-07-20
author: TTyb
desc: "对于python数组的操作有点混乱，所以特此记录下来"
---

对于 `python` 数组的操作，有插入和删除，下面介绍各个函数的功能：

# 插入

插入的函数有 `append`、`insert` 、`extend`

## append

`append(i)` 是在数组的末尾插入一个元素 `i` ，如下代码为在数组 `array` 的末尾插入元素 `10`：

~~~ruby
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array.append(10)
print array
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
~~~

## insert

`insert(i, j)` 是在 `i` 位置插入 `j` 一个元素，如下代码为在数组第 `0` 个位置插入元素 `0`：

~~~ruby
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array.insert(0, 0)
print array
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
~~~

## extend

`extend(list)` 是在末尾插入一个数组 `list` 里面的所有元素，如下代码为在数组末尾插入数组 `list` 里面的所有元素 `10`、`11`：

~~~ruby
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = [10, 11]
array.extend(list)
print array
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
~~~

# 删除

## pop

`pop(i)` 是删除数组中第 `i` 个位置的元素，如下代码为删除了数组第 `0` 个位置的元素 `1` ，并且可以返回删除的元素 `1` ：

~~~ruby
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print array.pop(0)
print array
# 1
# [2, 3, 4, 5, 6, 7, 8, 9]
~~~

## del

`del array[i]` 是删除数组中第 `i` 个位置的元素，如下代码为删除了数组第 `8` 个位置的元素 `9`，没有返回值 ：

~~~ruby
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del array[8]
print array
# [1, 2, 3, 4, 5, 6, 7, 8]
~~~

## remove

`remove(item)` 是删除数组里面的元素 `item` ，如下代码为删除了数组里面的元素 `9`，没有返回值 ：

~~~ruby
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array.remove(9)
print array
# [1, 2, 3, 4, 5, 6, 7, 8]
~~~
