# Shell 1: application under test
Start test app:

```
cd /d/1d-mx/workspace/locust_pres/sample_app
export FLASK_APP=`pwd`/flaskr/flaskr.py
flask initdb
flask run -h 0.0.0.0
```

# Shell 2: locust tests

## Install locust

```
pip3 install locust
```

You might need to adapt your path to get pip modules into your path:
```
export PATH="$HOME/.local/bin:$PATH"
```

## Check example 1: Quick start

`cat locust_demo/example1.py`

```
from locust import HttpUser, task, between

class QuickStart(HttpUser):
    wait_time = between(5, 9)

    @task
    def index(self):
        self.client.get("/")
```

Open the browser: http://127.0.0.1:8089/

```
cd /d/1d-mx/workspace/locust_pres
locust -f locust_demo/example1.py
```

## Check example 2

> Check error rates - not all blogs exists

## Check example 3

Call the slow endpoint andobserve  that the system throttles (due to single threaded model of Flask)

> One small delay in an endpoint is delaying all others...

then use gunicorn which is multi-threaded
```
sudo apt install gunicorn
```

```
gunicorn -w 2 -b 0.0.0.0:3000 myapp:app
```

## Interesting features

- Load Mode: `--step-load`
- csv exports: `--csv=example`
- ...

