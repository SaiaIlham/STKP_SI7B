import threading
import urllib.request, urllib.parse, urllib.error

class FetchUrls (threading.Thread):
    #Thread checking URLs.
    def _init__(self, urls, output):
        """
    Constructor.
    @param urls list of urls to check
    @param output file to write urls output
    """
    threading.Thread.__init__(self)
    self.urls = urls
    self.output = output
    
    def run(self):
        #Thread run method. Check URLs one by one.
        while self.urls:
            url = self.urls.pop()
        
            try:
                d = urllib.request.urlopen(url)
            except (urllib.error, e):
                print ('URL %s failed: %s' % (url, e.reason))

            self.output.write(d.read().decode())
            print ('write done by %s' % self.name)
            print ('URL %s fetched by %s' % (url, self.name))

    def main():
        #list 1 of urls to fetch
        urls1 =['http://www.google.com', 'http://www.Instagram.com']
        # list 2 of urls to fetch
        urls2 = ['http://www.google.com', 'http://www.Twiter.com']
        f = open('output_not_correct.txt', 'w+')
        t1 = FetchUrls(urls1, f)
        t2 =FetchUrls (urls2, f)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        f.close()

    if __name__== '__main__':
        main()
