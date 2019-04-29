import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)

data = {
    'rating_people': [352730, 131918, 272601, 211175, 234210, 456742, 304744, 225847, 311514, 343714, 345652, 314417,
                      330249, 392469, 323444, 286741, 284969, 313013, 556841, 319209, 280710, 290800],
    'start5': [0.295,0.099,0.183,0.112,0.119,0.315,0.225,0.159,0.256,0.286,0.176,0.172,0.256,0.189,0.284,0.143,0.158,0.062,0.333,0.121,0.107,0.576],
    'start4': [0.498,0.344,0.427,0.331,0.317,0.465,0.459,0.432,0.496,0.480,0.405,0.501,0.446,0.472,0.467,0.453,0.441,0.270,0.437,0.461,0.363,0.299],
    'start3': [0.193,0.496,0.349,0.476,0.460,0.195,0.282,0.364,0.227,0.208,0.360,0.301,0.256,0.301,0.222,0.357,0.350,0.542,0.198,0.379,0.454,0.106],
    'start2': [0.011,0.056,0.036,0.072,0.088,0.019,0.028,0.038,0.017,0.021,0.049,0.022,0.032,0.033,0.023,0.039,0.044,0.122,0.024,0.036,0.064,0.013],
    'start1': [0.002,0.006,0.005,0.010,0.015,0.005,0.006,0.006,0.004,0.005,0.010,0.004,0.011,0.005,0.005,0.008,0.007,0.023,0.008,0.004,0.011,0.006]
    }

df = pd.DataFrame(data, index=range(1, 23))

# 计算对象现有平均分
def average_stars_apply(rating_people,start5,start4,start3,start2,start1):
    average_stars = (rating_people*start5*5+rating_people*start4*4+rating_people*start3*3+rating_people*start2*2+rating_people*start1*1)/rating_people
    return round(average_stars,2)

# 计算贝叶斯平均
def bayes_score_apply(R,v,m,C):
    return (v*R+m*C)/(v+m)

# 主函数
def bayes_score(dataFrame):
    df = dataFrame.copy()
    df["average_stars"] = dataFrame.apply(lambda row: average_stars_apply(row['rating_people'], row['start5'],row['start4'], row['start3'],row['start2'],row['start1']), axis=1)
    m = df.mean().rating_people
    C = df.mean().average_stars
    df["bayes_score"] = df.apply(lambda row: bayes_score_apply(row['average_stars'], row['rating_people'], m, C), axis=1)
    return df

if __name__=='__main__':
    print(bayes_score(df))