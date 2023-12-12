import pandas as pd

# 读取数据
data = pd.read_excel("data.xlsx")

# 缺失值处理
data.fillna(0, inplace=True)

# 异常值处理
data = data[(data["使用小程序上传数"] >= 0) & (data["使用平台上传数"] >= 0) & (data["总数量"] >= 0)]

# 去重
data.drop_duplicates(inplace=True)

# 规范化
data["城区"] = data["城区"].str.lower()

# 类型转换
data["使用小程序上传数"] = data["使用小程序上传数"].astype(int)
data["使用平台上传数"] = data["使用平台上传数"].astype(int)
data["总数量"] = data["总数量"].astype(int)

# 保存处理后的数据
data.to_csv("cleaned_data.csv", index=False)