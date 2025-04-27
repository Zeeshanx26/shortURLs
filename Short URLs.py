import hashlib


class URLShortener:
    def __init__(self):
        self.url_map = {}  # Stores short:long URL mappings

    def shorten_url(self, long_url):
        # Create a short hash of the URL
        hash_object = hashlib.md5(long_url.encode())
        short_code = hash_object.hexdigest()[:6]

        # Store the mapping
        self.url_map[short_code] = long_url
        return f"short.url/{short_code}"

    def expand_url(self, short_code):
        return self.url_map.get(short_code, "URL not found")


# Usage
shortener = URLShortener()
short_url = shortener.shorten_url("https://www.linkedin.com/in/zeeshan-khawar-467bb4206/")
print(short_url)
original = shortener.expand_url(short_url.split('/')[-1])
print(original)