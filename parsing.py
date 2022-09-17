# #function to parse the content of website in rss mode
def rss_reader(url):
    from urllib.request import urlopen
    from xml.etree.ElementTree import parse
    u = urlopen(url)
    doc = parse(u)

    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext("pubDate")
        link = item.findtext('link')
    
        print(title)
        print(date)
        print(link)
        print()

rss_reader("https://finance.yahoo.com/rss/")
