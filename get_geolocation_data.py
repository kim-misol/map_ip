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
import requests
from instance.config import IP_ADDRESS, ACCESS_KEY
from api_response import res


def get_ip_addresses():
    datas = res['data']
    ips = []
    for data in datas:
        ips.append(data['hit_ip_address'])
    return ips


def get_geolocation_info_1():
    region_name, city, latitude, longitude, location, country_flag = [], [], [], [], [], []
    ips = get_ip_addresses()

    i = 0
    for ip_address in ips:
        link = F"http://api.ipstack.com/{ip_address}?access_key={ACCESS_KEY}"
        response = requests.get(link)
        json_data = json.loads(response.text)

        region_name.append(json_data['region_name'])
        city.append(json_data['city'])
        latitude.append(json_data['latitude'])
        longitude.append(json_data['longitude'])
        location.append(json_data['location'])
        country_flag.append(location[i]['country_flag'])
        i += 1

    geolocation_dict = {
        "region_name": region_name,
        "city": city,
        "latitude": latitude,
        "longitude": longitude,
        "location": location,
        "country_flag": country_flag,
    }
    return geolocation_dict


def get_geolocation_info():
    geolocation_dict = []
    ips = get_ip_addresses()

    i = 0
    for ip_address in ips:
        link = F"http://api.ipstack.com/{ip_address}?access_key={ACCESS_KEY}"
        response = requests.get(link)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            temp_dict = {
                "name": json_data['ip'],
                "description": f"{json_data['city']} {json_data['region_name']} {json_data['country_name']}",
                "zip": json_data['zip'],
                "lat": json_data['latitude'],
                "lng": json_data['longitude'],
                "location": json_data['location'],
                "country_flag": json_data['location']['country_flag'],
            }
            geolocation_dict.append(temp_dict)
        else:
            pass

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
    addr_dict = get_geolocation_info()
    # save_data(addr_dict)
    d = get_saved_data()
    print(d)