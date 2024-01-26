from locust import HttpUser, task, between

class NextcloudUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def on_start(self):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"
        }
        data = {"username": "prova1", "password": "Willie7594"}
        self.client.post("/login", headers=headers, json=data)
