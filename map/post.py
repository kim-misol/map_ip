from flask import Blueprint

# from map.auth import login_required
# to save img file
from get_geolocation_data import get_geolocation_info

bp = Blueprint('post', __name__, url_prefix='/')


@bp.route('/')
def kakao_map():
    app_key = '14c32e894bc092b7b77d64d68100c5fa'
    map_api_html = f"""<!-- kakao map -->
<div id="map" style="width:100%;height:100vh; position: relative; z-index: 500;display: inline-block; margin-top:-100px;"></div>
<!-- KAKAO MAP API -->
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey={app_key}&libraries=clusterer"></script>
"""
    start_js = """<script>
    getSearchQuery()
    function getSearchQuery(){
        var query = ""
        var url = ""
    """
    map_html = """
    // 마커 생성
    var markers = [];
    var mapContainer = document.getElementById('map'), // 지도를 표시할 div
        mapOption = {
            center: new kakao.maps.LatLng(37.548864, 126.993926), // 지도의 중심좌표 남산
            level: 8, // 지도의 확대 레벨
            mapTypeId : kakao.maps.MapTypeId.ROADMAP // 지도종류
        };

    // 지도를 생성
    var map = new kakao.maps.Map(mapContainer, mapOption);
    // 마커 클러스터러를 생성
    var clusterer = new kakao.maps.MarkerClusterer({
        map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체
        averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정
        minLevel: 6 // 클러스터 할 최소 지도 레벨
    });
}"""
    # geolocation_dict = get_geolocation_info()
    geolocation_dict = [{'name': '223.38.8.247', 'description': 'Seoul Seoul South Korea', 'zip': '100-011', 'hit_date': '2021-02-20',
'hit_time': '18:30:55', 'lat': 37.56100082397461, 'lng': 126.98265075683594,
'location': {'geoname_id': 1835848, 'capital': 'Seoul',
'languages': [{'code': 'ko', 'name': 'Korean', 'native': '한국어'}],
'country_flag': 'http://assets.ipstack.com/flags/kr.svg', 'country_flag_emoji': '🇰🇷',
'country_flag_emoji_unicode': 'U+1F1F0 U+1F1F7', 'calling_code': '82', 'is_eu': False}, 'country_flag': 'http://assets.ipstack.com/flags/kr.svg'}]

    data = f""" 
    console.log("{geolocation_dict}");
    console.log("bb")
    var geolocation_dict = {[{'name': '223.38.8.247', 'description': 'Seoul Seoul South Korea', 'zip': '100-011', 'hit_date': '2021-02-20', 
'hit_time': '18:30:55', 'lat': 37.56100082397461, 'lng': 126.98265075683594, 
'location': {'geoname_id': 1835848, 'capital': 'Seoul', 
'languages': [{'code': 'ko', 'name': 'Korean', 'native': '한국어'}], 
'country_flag': 'http://assets.ipstack.com/flags/kr.svg', 'country_flag_emoji': '🇰🇷', 
'country_flag_emoji_unicode': 'U+1F1F0 U+1F1F7', 'calling_code': '82', 'is_eu': False}, 'country_flag': 'http://assets.ipstack.com/flags/kr.svg'}]};"""
    # var geolocation_dict = {geolocation_dict};"""
    markers = """
    console.log("cc")
    console.log(geolocation_dict)
for (var i = 0; i < geolocation_dict.length; i++) {
    let name = geolocation_dict[i]["ip"];
    let addr = geolocation_dict[i]["description"];
    let zip = geolocation_dict[i]["zip"];
    let hit_date = geolocation_dict[i]["hit_date"];
    let hit_time = geolocation_dict[i]["hit_time"];
    let lat = geolocation_dict[i]["lat"];
    let lng = geolocation_dict[i]["lng"];
    let country_flag = geolocation_dict[i]["country_flag"];

    // 마커이미지의 주소입니다
    imgSelect = 'https://raw.githubusercontent.com/kim-misol/map_coffee/master/img/marker_green_round.png'
    var imageSrc = imgSelect,
    imageSize = new kakao.maps.Size(30, 33), // 마커이미지의 크기입니다
    imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)

    var marker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(lat, lng)
        , map:map // 마커 표시할 지도
        , addr:addr
        , image: markerImage // 마커이미지 설정
    });
    markers.push(marker);
}"""
    zoom_controller = """
    // 지도 확대 축소를 제어할 수 있는 줌 컨트롤을 생성합니다
    var zoomControl = new kakao.maps.ZoomControl();
    map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
    
    // 지도가 확대 또는 축소되면 마지막 파라미터로 넘어온 함수를 호출하도록 이벤트를 등록합니다
    kakao.maps.event.addListener(map, 'zoom_changed', function() {
        // 지도의 현재 레벨을 얻어옵니다
        var level = map.getLevel();
    
        var message = '현재 지도 레벨은 ' + level + ' 입니다';
        var resultDiv = document.getElementById('result');
    
    });
clusterer.addMarkers(markers);"""

    end_js = "</script>"

    # return map_api_html + start_js + map_html + data + markers_html + zoom_controller + end_js
    return map_api_html + start_js + map_html + data + markers_html + end_js

