from flask import (
    Blueprint
)

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
    console.log("cc")
}"""
    geolocation_dict = get_geolocation_info()
    data = f""" 
    console.log("{geolocation_dict}");
    var geolocation_dict = [{geolocation_dict}];"""
    markers = """
    console.log("dd")
    console.log(geolocation_dict)
for (var i = 0; i < geolocation_dict.length; i++) {
    let name = geolocation_dict[i]["ip"];
    let addr = geolocation_dict[i]["description"];
    let zip = geolocation_dict[i]["zip"];
    let lat = geolocation_dict[i]["lat"];
    let lng = geolocation_dict[i]["lng"];
    let country_flag = geolocation_dict[i]["country_flag"];

    // 마커 이미지 선택
    switch(handle_coffee){
        case "o":
            remain_stat = "<span style='color:#3d853b;'>커피 판매 중</span>";
            imgSelect = 'https://raw.githubusercontent.com/kim-misol/map_coffee/master/img/marker_green_round.png'
            break;
        default:
            remain_stat = "커피 판매 안함"
            imgSelect = 'https://raw.githubusercontent.com/kim-misol/map_coffee/master/img/marker_green_round.png'
            break;
    }

    // 마커이미지의 주소입니다
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

    return map_api_html + start_js + map_html + data + markers + zoom_controller + end_js


#
# @bp.route('/posts', methods=['GET'])
# def get_posts():
#     posts = Post.query.all()
#     return render_template('post/index.html', posts=posts)
#
#
# @bp.route('/posts/<int:post_id>', methods=['GET'])
# def load(post_id):
#     # if click post, it needs to be passed correct post_id (currently, it's hard coded)
#     print(f"post_id: {post_id}")
#     post = Post.query.filter_by(id=post_id).first_or_404()
#     if post is None:
#         return redirect(url_for('.get_posts'))
#
#     return render_template('post/index.html', post=post)
#
#
# def saveImgFromBase64(codec, image_path="dev/flask_tutorial/flaskr/uploads/"):
#     base64_data = re.sub('^data:image/.+;base64,', '', codec)
#     byte_data = base64.b64decode(base64_data)
#     image_data = BytesIO(byte_data)
#     img = Image.open(image_data)
#     random_filename = str(uuid.uuid4())
#     file_url = image_path + random_filename + '.png'
#     img.save(file_url, "PNG")
#     return file_url
#
#
# @bp.route('/posts/new', methods=('GET',))
# def create():
#     form = PostEditForm()
#
#     return render_template('post/create.html', form=form)
#
# # @bp.route('/posts', methods=['POST'])
# # def create_post():
# #     form = PostEditForm()
# #     if form.validate_on_submit():
# #         data = request.form
# #         title = form.title.data
# #         content = data['content']
# #         content_preview = data['content_preview']
# #         # attachment = data['attachment']
# #         attachment = ""
# #         save_type = data['save_type']
# #         content_json = data['content_json']
# #         content_json = json.loads(content_json)
# #         # check if img is in content_json
# #         for item in content_json['ops']:
# #             insert = item['insert']
# #             # try except
# #             if isinstance(insert, dict) and 'image' in insert:
# #                 base64_data = insert['image']
# #                 file_url = saveImgFromBase64(base64_data)
# #                 insert['image'] = file_url
# #
# #         error = None
# #
# #         if not title:
# #             error = 'Title is required.'
# #         elif not content:
# #             error = 'Content is required.'
# #
# #         if error is not None:
# #             flash(error)
# #             return render_template('post/create.html', form=form)
# #         else:
# #             from datetime import datetime
# #             now = datetime.now()
# #             created_at = now.strftime("%Y-%m-%d %H:%M:%S")
# #             user_id = current_user.id
# #             new_post = Post(title=title, content=content, content_json=content_json,
# #                             content_preview=content_preview, attachment=attachment, save_type=save_type,
# #                             created_at=created_at, modified_at=created_at, user_id=user_id)
# #             db.session.add(new_post)
# #             db.session.commit()
# #             return make_response(jsonify({'redirect': url_for('post.get_posts')}))
# #     return make_response(jsonify({'error': 'failed to create a post'}))
