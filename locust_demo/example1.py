from locust import HttpUser, task, between


class QuickStart(HttpUser):
    wait_time = between(5, 9)

    @task
    def index(self):
        self.client.get("/")


