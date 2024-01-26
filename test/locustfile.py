from locust import HttpUser, task, between

class NextcloudUser(HttpUser):
    wait_time = between(1, 3)
    host = "localhost:8080"

    @task
    def on_start(self):
        self.client.post("/login", json={"username":"prova1", "password":"Willie7594"})



