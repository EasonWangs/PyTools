import requests
from datetime import datetime, timedelta

# 定义基本的请求参数
base_url = 'https://cloudserver.hugehuge.net/common/test'
params = {'startTimeStr': None}

# 生成日期列表
start_date = datetime(2023, 2, 19)
end_date = datetime(2023, 2, 20)
date_range = end_date - start_date
date_list = [start_date + timedelta(days=i) for i in range(date_range.days + 1)]

# 循环发送请求
for date in date_list:
    # 格式化日期参数
    date_str = date.strftime('%Y-%m-%d')
    params['date'] = date_str

    # 发送请求
    response = requests.get(base_url, params=params)

    # 处理响应
    print(response.text)