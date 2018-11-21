---
layout: post
categories: [python]
title: pandas和spark的dataframe互转
date: 2018-11-21
author: TTyb
desc: "pandas和spark的dataframe互转"
---

# pandas的dataframe转spark的dataframe

~~~ruby
from pyspark.sql import SparkSession
# 初始化spark会话
spark = SparkSession \
    .builder \
    .getOrCreate()

spark_df = spark.createDataFrame(pandas_df)
~~~

# spark的dataframe转pandas的dataframe

~~~ruby
import pandas as pd

pandas_df = spark_df.toPandas()
~~~

由于`pandas`的方式是单机版的，即`toPandas()`的方式是单机版的，所以参考[breeze_lsw](https://www.jianshu.com/p/16e3c0ad7bc7)改成分布式版本：

~~~ruby
import pandas as pd
def _map_to_pandas(rdds):
    return [pd.DataFrame(list(rdds))]
    
def topas(df, n_partitions=None):
    if n_partitions is not None: df = df.repartition(n_partitions)
    df_pand = df.rdd.mapPartitions(_map_to_pandas).collect()
    df_pand = pd.concat(df_pand)
    df_pand.columns = df.columns
    return df_pand
	
pandas_df = topas(spark_df)
~~~
