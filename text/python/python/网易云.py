#游戏思路：通过攻击目标玩家获得装备
#爬虫思路：通过攻击目标网站获得数据

#导入工具包
import requests
from lxml import etree
#隐藏身份 伪装
yincang={'User-Agent':'Mozilla/5.0(windows NT 10,0)'}
#拿好武器 穿上伪装 发起攻击
gongji=requests.get(url:https://music.163.com/'')
#确认结果
print(gongji.text)
#解析数据
shujv=
