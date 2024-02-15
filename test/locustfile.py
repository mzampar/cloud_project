from locust import HttpUser, task
from requests.auth import HTTPBasicAuth
import requests

class NextcloudUser(HttpUser):
    auth = None

    def on_start(self):
        self.user = 'prova1'
        self.password = 'Willie7594'
        self.auth = HTTPBasicAuth(self.user, self.password)
        self.verify_authentication()

    def verify_authentication(self):
        response = self.client.head("/remote.php/dav", auth=self.auth)
        if response.status_code != 200:
            with open("/mnt/locust/output.txt", "a") as f:
                f.write(f"Authentication failed for user {self.user}.\n")
            raise Exception(f"Authentication failed for user {self.user}")




    @task(10)
    def propfind(self):
        try:
            response = self.client.request("PROPFIND", "/remote.php/dav", auth=self.auth)
            response.raise_for_status()  # Raise an HTTPError if response status code is not 2xx
            with open("/mnt/locust/output.txt", "a") as f:
                f.write("PROPFIND request successful!\n")
        except Exception as e:
            with open("/mnt/locust/output.txt", "a") as f:
                f.write(f"Error during PROPFIND request: {e}\n")

    @task
    def upload_pdf(self):
        filename = "Lecture01.pdf"
        with open('/app/files/' + filename, 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                       auth=self.auth, data=f, name="/remote.php/dav/files/[user]/Lecture01.pdf")

        if response.status_code != requests.codes.created:
            return

        for i in range(0, 5):
            self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
                            auth=self.auth, name="/remote.php/dav/files/[user]/Lecture01.pdf")

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                           auth=self.auth, name="/remote.php/dav/files/[user]/Lecture01.pdf")
