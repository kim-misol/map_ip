# IP Address to geolocation (Kakao Map)

[ipstack API](https://ipstack.com/quickstart) 와 [Kakao map API](https://apis.map.kakao.com/web/guide/) 를 사용하여
IP Address를 latitude와 longitude로 변환하여 카카오 맵에 표시


### Run The Application
Now you can run your application using the flask command. From the terminal, tell Flask where to find your application, then run it in development mode. 
Remember, you should still be in the top-level __flask-tutorial__ directory, __not the flaskr__ package.

Development mode shows an interactive debugger whenever a page raises an exception, and restarts the server whenever you make changes to the code.

For Linux and Mac:
```bash
$ export FLASK_APP=map
$ export FLASK_ENV=development
$ flask run
```
For Windows cmd, use set instead of export:
```bash
> set FLASK_APP=map
> set FLASK_ENV=development
> flask run
```

You’ll see output similar to this:
```
* Serving Flask app "map"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761
```