from locust import HttpUser, task, between

class NextcloudUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Perform login when a new user starts the scenario
        self.login()

    @task
    def login(self):
        # Specify the login credentials
        login_payload = {
            "user": "prova1",  # Replace with your Nextcloud username
            "password": "Willie7594"  # Replace with your Nextcloud password
        }

        # Make a POST request to the Nextcloud login endpoint
        response = self.client.post("/login", data=login_payload)

        # Check if the login was successful (you may need to adjust this based on Nextcloud's response)
        if response.status_code == 200:
            print("Login successful!")
        else:
            print(f"Login failed with status code: {response.status_code}")
