import requests
import json
import datetime

# r = requests.get('http://toolscdn.yobot.win/calender/jp.json').json()
with open('./test.json', 'r') as load_f:
    r = json.load(load_f)

today = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y/%m/%d')
hours = []
hourcall = {}
for i in range(0, 24):
    hours.append(f'{today} {i:02d}')
    hourcall[f'{i:02d}'] = []

hourcall['12'].append('体力刷新了')
hourcall['14'].append('竞技场时间')
hourcall['18'].append('体力刷新了')
for item in r:
    start_time = datetime.datetime.strptime(
        item['start_time'], r'%Y/%m/%d %H:%M:%S')
    s = start_time.strftime('%Y/%m/%d %H')
    if s in hours:
        hourcall[start_time.strftime('%H')].append(f"{item['name']} 开始了")

    end_time = datetime.datetime.strptime(
        item['end_time'], r'%Y/%m/%d %H:%M:%S')
    e = end_time.strftime('%Y/%m/%d %H')
    if e in hours:
        hourcall[end_time.strftime('%H')].append(f"{item['name']} 即将结束，请留意")

print(hourcall)

