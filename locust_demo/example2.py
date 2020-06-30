import random

from locust import HttpUser, task, between

class MyTaskSet(HttpUser):
    wait_time = between(5, 9)

    def on_start(self):
        res = self.client.post('login',
                         {
                             "username": 'admin',
                             "password": 'default'
                         })
        res.raise_for_status()

    @task(1)
    def index(self):
        self.client.get("/")

    @task(1)
    def entry(self):
        entry = random.randint(1, 6)

        self.client.get(f"/entry/{entry}", name="Entry")

