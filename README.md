NewsAPI Project
==============
This is a Flask app which has a single endpoint `POST/news`. The endpoint receives a keyword
in the form of JSON and makes an HTTP GET request to the [newsAPI](https://newsapi.org/) API.
The response is the first article from the current date, sorted by popularity, that contains the
above keyword, with the following schema:
```json
{
  "title": "The title of the article",
  "url": "The URL of the article"
}
```
In case of errors or a failure, the app will return a JSON response explaining the reason, along
with an appropriate HTTP status code.

The project is set up to run either through a virtual environment or a docker container.
You can run the app with one of the following ways:

For the *virtual environment* case:
* Create a new [virtual environment](https://docs.python.org/3/library/venv.html) in the app's directory:
python3 -m venv /path/to/new/virtual/environment
* Install the requirements from the requirements.txt
  1. activate the virtual environment: source {venv}/bin/activate
  2. run: pip install -r requirements.txt
* Run the app with: python3 run.py

To make an HTTP POST request to the app use the following cURL command:
~~~
curl -X POST -H "Content-Type: application/json" localhost:5000/news -d '{"keyword": "user's keyword"}'
~~~
For the *docker container* case:
* cd to the apps directory and create a docker image: docker build -t {name:tag} **.**
* Run the docker container: docker run {name:tag}

Then make an HTTP POST request with the following cURL command:
~~~
curl -X POST -H "Content-Type: application/json" 172.17.0.1:5000/news -d '{"keyword": "user's keyword"}'
~~~
Note that a keyword must be provided otherwise an exception is thrown.

Some unit and integration tests utilizing the pytest framework tested the application's functionality.
 A Dockerfile is included so that a docker image can be created.

Tools
====
1. [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
2. [pip 20.0.2](https://pypi.org/project/pip/20.0.2/)
3. [cURL 7.68.0](https://curl.se/mail/lib-2020-01/0028.html)
4. [Docker 20.10.16](https://docs.docker.com/engine/release-notes/)
5. [Git 2.25.1](https://git-scm.com/docs/git/2.25.1)
