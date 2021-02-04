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


link = F"http://api.ipstack.com/{IP_ADDRESS}?access_key={ACCESS_KEY}"
response = requests.get(link)
json_data = json.loads(response.text)

region_name = json_data['region_name']
city = json_data['city']
latitude = json_data['latitude']
longitude = json_data['longitude']
location = json_data['location']
country_flag = location['country_flag']