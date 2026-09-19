class Codec:
    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl):
        shortUrl = "http://tinyurl.com/" + str(self.counter)
        self.url_map[shortUrl] = longUrl
        self.counter += 1
        
        return shortUrl

    def decode(self, shortUrl):
        return self.url_map.get(shortUrl, "")