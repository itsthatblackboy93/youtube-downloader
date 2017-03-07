from pytube import YouTube

"""
Downloader is used to download video and provides functions to handle video properties
"""


class Downloader:
    def __init__(self, url):
        self.url = url
        self.videos = None
        self.youTube = YouTube(url)
        self.createYoutube(self.url)

    # createYoutube(url) creates YouTube object using url so that videos can be
    # downloaded
    # createYoutube: self, String -> void
    def createYoutube(self, url):
        self.youTube = YouTube(url)

    # downloadVideos() download videos and store them in a list. If it fails to
    # download, it returns False otherwise it returns True
    # downloadVideos: self -> Bool
    def downloadVideos(self):
        try:
            self.videos = self.youTube.get_videos()
            return True
        except:
            return False

    # setUrl(url) updates the youTube url for the downloader
    # setUrl: self, String - > void
    def setUrl(self, url):
        self.url = url
        self.createYoutube(self.url)

