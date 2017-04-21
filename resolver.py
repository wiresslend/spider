from bs4 import BeautifulSoup
import lxml


class Resolver(object):
    def __init__(self, f):
        data = self.resolve_url(f)
        self.tag_imgs = data[1]
        self.tag_as = data[0]
        self.srcs = self.get_imgs_src(self.tag_imgs)
        self.links = self.get_a_href(self.tag_as)

    def resolve_url(self, f):
        soup = BeautifulSoup(f, 'lxml')
        tag_imgs = soup.find_all('img')
        tag_as = soup.find_all('a')
        return [tag_as, tag_imgs]

    def get_imgs_src(self, tag_imgs):
        srcs = []
        for img in tag_imgs:
            src = img.get('src')
            srcs.append(src)
        return srcs

    def get_a_href(self, tag_as):
        links = []
        for tag_a in tag_as:
            href = tag_a.get('href')
            links.append(href)
        return links

