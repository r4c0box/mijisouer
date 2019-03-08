#conding:utf-8
import requests
from optparse import OptionParser
import json
import re
base_url = 'https://mijisou.com/?'
def search(keyword,pageno):
    num = 0
    url = base_url+"q="+keyword+"&category_general=on"+"pageno="+pageno
    print url
    resp = requests.get(url,verify=False)
    #print resp.content
    result_headers =  re.findall('<!-- <div class="result result-default"> -->(.*?)<!-- </div> -->',resp.content,re.S)
    for i in result_headers:
        print '--------------'+str(num)
        num+=1
        #print "raw:"+i
        #print '-----'
        title = re.findall('<h4 class="result_header">.*?<a href=".*?">(.*?)</a>',i,re.S)[0]

        title = re.sub('</?span.*?>','',title)
        print "title:"+title
        url_pre = re.findall('h4 class="result_header">.*?<a href="(.*?)" target',i,re.S)[0]
        print "url_pre:"+url_pre
        url_under = re.findall('<span class="url">(.*?)</span>',i,re.S)[0]
        print "url_nuder:"+url_under
        content = re.findall('<p class="result-content">(.*?)</p>',i,re.S)
        if len(content) != 0:
            print "content:"+content[0]
        else:
            print "content:"+""
        engine=re.findall('<span class="engine">(.*?)</span>',i,re.S)
        print "engine:"+engine.__str__()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-q", "--query", dest="query",help="words to query")
    parser.add_option("-p","--page",dest="pageno",help="page to search")
    (options, args) = parser.parse_args()

    if  options.query is not None:
        if options.pageno is not None: 
            search(options.query,options.pageno)


