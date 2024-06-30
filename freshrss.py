"""Google Reader/FreshRSS API code for Youtube2FreshRSS."""

import requests


class FreshRss:
    """FreshRSS greader API helper class."""
    base_path = "/api/greader.php"
    base_api_path = f"{base_path}/reader/api/0/"

    def __init__(self, baseurl, username, password):
        self.base_url = baseurl
        self.username = username
        self.password = password
        self.auth_header = ""

    def get_auth_token(self):
        "Retrieve greader auth token"
        res = requests.post(
            f"{self.base_url}{self.base_path}/accounts/ClientLogin",
            params={'Email': self.username, 'Passwd': self.password},
            timeout=15
        )
        auth_token = res.text.split("=")[-1].strip()
        self.auth_header = f"GoogleLogin auth={auth_token}"

    def post(self, path, params=None, data=None):
        "Make a POST request to a greader API."
        res = requests.post(
            f"{self.base_url}{self.base_api_path}{path}",
            data=data,
            params=params,
            headers={"Authorization": self.auth_header},
            timeout=15
        )
        return res.text

    def get(self, path, params=None):
        """Make a GET request to a greader API."""
        res = requests.get(
            f"{self.base_url}{self.base_api_path}{path}?output=json",
            params=params,
            headers={"Authorization": self.auth_header},
            timeout=15
        )
        return res.json()

    def get_starred(self):
        """Retrieve starred items."""
        return self.get("/stream/contents/user/-/state/com.google/starred")

    def parse_items(self, items):
        """Parse URLs from a list of items."""
        parsed = []

        for item in items:
            cat = ["rss"]
            for category in item['categories']:
                if category.startswith("user/-/label/"):
                    cat.append(category[13:])

            parsed.append({
                "id": item['id'],
                "title": item['title'],
                "url": item['canonical'][0]['href'],
                "categories": ",".join(cat)
            })

        return parsed

    def unstarr(self, item_id):
        """Unstar an item given its ID."""
        self.post(
            "/edit-tag",
            data={
                "i": item_id,
                "r": "user/-/state/com.google/starred"
            }
        )
