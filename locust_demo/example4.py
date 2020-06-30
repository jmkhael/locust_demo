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

    @task(30)
    def index(self):
        self.client.get("/")

    @task(10)
    def entry(self):
        entry = random.randint(1, 5)

        self.client.get(f"entry/{entry}", name="Entry")

    @task(10)
    def slow(self):
        self.client.get('slow')

    @task(50)
    def flaky(self):
        with self.client.get("flaky", catch_response=True) as response:
            if 'AWESOME!' not in response.content.decode('ascii'):
                response.failure("Got wrong response.")
            else:
                response.success()


