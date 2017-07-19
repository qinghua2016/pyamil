#coding=utf-8
import urllib
import urllib2
import gzip
import json
import sys
from cStringIO import StringIO
print('------天气查询------')
def gzip_uncompress(c_data):
    buf = StringIO(c_data)
    f = gzip.GzipFile(mode = 'rb', fileobj = buf)
    try:
        r_data = f.read()
    finally:
        f.close()
    return r_data
def get_weather_data(city_name) :
    # city_name = raw_input('请输入要查询的城市名称：')
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.pathname2url(city_name)
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    #网址1只需要输入城市名，网址2需要输入城市代码
    #print(url1)
    # weather_data = urllib2.Request(url1)
    # weather_data = urllib2.ulropen(weather_data)
    res = urllib.urlopen(url1)
    data = res.read()
    #读取网页数据
    weather_data = gzip_uncompress(data).decode('utf-8')
    #解压网页数据
    weather_dict = json.loads(weather_data)
    #将json数据转换为dict数据
    return weather_dict

def show_weather(weather_data):
    weather_dict = weather_data
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        print('你输入的城市名有误，或者天气中心未收录你所在城市')
    elif weather_dict.get('desc') =='OK':
        forecast = weather_dict.get('data').get('forecast')
        print(u'城市：'+weather_dict.get('data').get('city'))
        print(u'温度：'+weather_dict.get('data').get('wendu')+u'℃ ')
        print(u'感冒：'+weather_dict.get('data').get('ganmao'))
        print(u'风向：'+forecast[0].get('fengxiang'))
        print(u'风级：'+forecast[0].get('fengli'))
        print(u'高温：'+forecast[0].get('high'))
        print(u'低温：'+forecast[0].get('low'))
        print(u'天气：'+forecast[0].get('type'))
        print(u'日期：'+forecast[0].get('date'))
        # print('*******************************')
    #     four_day_forecast =raw_input('是否要显示未来四天天气，是/否：')
    #     if four_day_forecast == '是' or 'Y' or 'y':
    #         for i in range(1,5):
    #             print(u'日期：'+forecast[i].get('date'))
    #             print(u'风向：'+forecast[i].get('fengxiang'))
    #             print(u'风级：'+forecast[i].get('fengli'))
    #             print(u'高温：'+forecast[i].get('high'))
    #             print(u'低温：'+forecast[i].get('low'))
    #             print(u'天气：'+forecast[i].get('type'))
    #             print('--------------------------')
    # print('***********************************')

# show_weather(get_weather_data())
def main():

    # city = sys.argv[1]
    # city='厦门'
    city=''.join(sys.argv[1:])
    # print('city is '+city)
    show_weather(get_weather_data(city))

if __name__ == '__main__':
    main()