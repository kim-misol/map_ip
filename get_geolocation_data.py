'''
https://ipstack.com/quickstart
{
    ip: "211.44.79.144",
    type: "ipv4",
    continent_code: "AS",
    continent_name: "Asia",
    country_code: "KR",
    country_name: "South Korea",
    region_code: "11",
    region_name: "Seoul",
    city: "Seoul",
    zip: "100-011",
    latitude: 37.56100082397461,
    longitude: 126.98265075683594,
    location: {
        geoname_id: 1835848,
        capital: "Seoul",
        languages: [
            {
            code: "ko",
            name: "Korean",
            native: "한국어"
            }
        ],
        country_flag: "http://assets.ipstack.com/flags/kr.svg",
        country_flag_emoji: "🇰🇷",
        country_flag_emoji_unicode: "U+1F1F0 U+1F1F7",
        calling_code: "82",
        is_eu: false
    }
}
'''
import json
from datetime import date

import requests

from api_response import res
from instance.config import ACCESS_KEY


def get_ip_addresses():
    datas = res['data']
    ips = []
    for data in datas:
        ips.append(f"{data['hit_ip_address']} {data['hit_date']} {data['hit_time']}")
    return ips


def get_geolocation_info_test_one_response():
    geolocation_dict = []
    response = get_ip_addresses()

    line = response[0]
    r = line.split("  ")
    ip_address = r[0]
    hit_date = r[1].split(" ")[0]
    hit_time = r[1].split(" ")[1]
    link = F"http://api.ipstack.com/{ip_address}?access_key={ACCESS_KEY}"
    response = requests.get(link)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        # hit date과 time 추가
        temp_dict = {
            "name": json_data['ip'],
            "description": f"{json_data['city']} {json_data['region_name']} {json_data['country_name']}",
            "zip": json_data['zip'],
            "hit_date": hit_date,
            "hit_time": hit_time,
            "lat": json_data['latitude'],
            "lng": json_data['longitude'],
            "country_flag": json_data['location']['country_flag'],
        }
        geolocation_dict.append(temp_dict)
    else:
        pass

    return geolocation_dict


def get_geolocation_info(date_from=date.today()):
    geolocation_dict = []
    response = get_ip_addresses()

    for line in response:
        r = line.split("  ")
        ip_address = r[0]
        hit_date = r[1].split(" ")[0]
        d = hit_date.split('-')
        hit_date_d = date(int(d[0]), int(d[1]), int(d[2]))
        hit_time = r[1].split(" ")[1]
        if hit_date_d < date_from:
            break
        else:
            link = F"http://api.ipstack.com/{ip_address}?access_key={ACCESS_KEY}"
            response = requests.get(link)
            if response.status_code == 200:
                json_data = json.loads(response.text)
                # hit date과 time 추가
                temp_dict = {
                    "name": json_data['ip'],
                    "description": f"{json_data['city']} {json_data['region_name']} {json_data['country_name']}",
                    "zip": json_data['zip'],
                    "hit_date": hit_date,
                    "hit_time": hit_time,
                    "lat": json_data['latitude'],
                    "lng": json_data['longitude'],
                    "country_flag": json_data['location']['country_flag'],
                }
                geolocation_dict.append(temp_dict)

    return geolocation_dict


def save_data(data):
    fname = 'data.py'
    f = open(f"{fname}", 'w', encoding='UTF-8')
    content = f"data = {data}"
    f.write(content)
    f.close()


def get_saved_data():
    from data import data
    return data


if __name__ == "__main__":
    # api response 업데이트 시 아래 코드 실행
    '''
    1. admin web에서 visitor traffic response를 받아온다
    2. 복사해서 api_response.py에 json 형태로 저장
    3. 아래 코드 실행 
    '''
    addr_dict = get_geolocation_info()
    save_data(addr_dict)
    d = get_saved_data()
    print(d)
