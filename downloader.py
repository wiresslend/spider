import urllib2


class DownLoader(object):
    def __init__(self, url):
        self.url = url
        self.url_content = self.url_with_headers(self.url)

    def url_with_headers(self, url, headers=None):
        if headers:
            fun_headers = headers
        else:
            fun_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6)\
                 Gecko/20091201 Firefox/3.5.6'
            }
        seq = urllib2.Request(url, headers=fun_headers)
        content = urllib2.urlopen(seq)
        return content

