---
layout: post
categories: [python]
title: TensorFlow使用GPU
date: 2018-09-29
author: TTyb
desc: "记录在TensorFlow中使用GPU的一些操作"
---

查看机器 `GPU` 的信息：

~~~ruby
nvidia-smi
~~~

持续更新查看：

~~~ruby
nvidia-smi -l
~~~

<p style="text-align:center"><img src="/static/postimage/python/gpu/20180929185107.png" class="img-responsive" style="display: block; margin-right: auto; margin-left: auto;"></p>

其他方式如下：

~~~ruby
# 查看可用GPU
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

import tensorflow as tf
import os

# 使用GPU0 和 GPU1
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1'  

# 通过 allow_soft_placement 参数自动将无法放在 GPU 上的操作放回 CPU
gpuConfig = tf.ConfigProto(allow_soft_placement=True)

# 限制一个进程使用 60% 的显存
gpuConfig.gpu_options.per_process_gpu_memory_fraction = 0.6

# 运行时需要多少再给多少
gpuConfig.gpu_options.allow_growth = True  

with tf.Session(config=gpuConfig) as sess:
     pass
~~~
