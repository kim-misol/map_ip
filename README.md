# IP Address to geolocation (Kakao Map)

[ipstack API](https://ipstack.com/quickstart) 와 [Kakao map API](https://apis.map.kakao.com/web/guide/) 를 사용하여
IP Address를 latitude와 longitude로 변환하여 카카오 맵에 표시


### Run this Application
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

### Build this Application
[installable project](https://flask.palletsprojects.com/en/1.1.x/tutorial/install/)

The setup.py file describes your project.  
install your project in the virtual environment.
```bash
pip install -e .
```
[build and install tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/)


When you want to deploy your application elsewhere, you build a distribution file. 
The current standard for Python distribution is the wheel format, with the .whl extension

````bash
pip install wheel
````

Running setup.py with Python gives you a command line tool to issue build-related commands. 
The bdist_wheel command will build a wheel distribution file.

````bash
python setup.py bdist_wheel
````

You can find the file in `dist/flaskr-1.0.0-py3-none-any.whl`. 
The file name is in the format of {project name}-{version}-{python tag} -{abi tag}-{platform tag}.


Copy this file to another machine, set up a new virtualenv, then install the file with pip.

```bash
pip install map_ip-1.0.0-py3-none-any.whl
```
Pip will install your project along with its dependencies.

Since this is a different machine, 
you need to run init-db again to create the database in the instance folder.


```bash
set FLASK_APP=map
flask init-db
```


### Run with a Production Server
When running publicly rather than in development, you should not use the built-in development server (flask run). The development server is provided by Werkzeug for convenience, but is not designed to be particularly efficient, stable, or secure.
```bash
pip install waitress
waitress-serve --call 'map:create_app'

Serving on http://0.0.0.0:8080
```
https://flask-docs-kr.readthedocs.io/ko/latest/deploying/index.html

https://gist.github.com/drengle/c31b64ab0377a22a2f69eff21a16b449

https://truehost.co.ke/support/knowledge-base/how-to-deploy-a-flask-app-in-cpanel/