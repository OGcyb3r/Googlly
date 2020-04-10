#!/usr/bin/env python3.5
#coded by OGcyb3r

import socket,re,sys,os,re
import urllib
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urlparse

def clz():
    zl="clear"
    os.system(zl)
def header():
    clz()
    print(("""\x1b[30;38;5;236m* googlly will print the result as url ..\x1b[0m
\x1b[30;38;5;68m
  .oooooo.                                   oooo  oooo
 d8P'  `Y8b                                  `888  `888
888            .ooooo.   .ooooo.   .oooooooo  888   888  oooo    ooo
888           \x1b[30;38;5;67md88' `88b d88' `88b 888' `88b   888   888   `88.  .8'
888     ooooo 888   888 888  \x1b[1;38;5;104m 888 888   888   888   888    `88..8'
`88.    .88'  888   888 888   888 `88bod8P'  \x1b[1;38;5;103m 888   888     `888'
 `Y8bood8P'   `Y8bod8P' `Y8bod8P' `8oooooo.  o888o o888o     .8'
                                  d"   \x1b[30;38;5;105m  YD              .o..P'
                                  "Y88888P'              `Y8P'\x1b[0m

\x1b[1;38;5;118m*\x1b[1;38;5;255m How to use it :\x1b[0m add \x1b[30;38;5;119m+\x1b[0m between words..\x1b[1;38;5;160m!\x1b[0m


[✔]\x1b[1;38;5;255m python3.5\x1b[0m googlly.py "site:.com\x1b[30;38;5;119m+\x1b[0msomething\x1b[30;38;5;119m+\x1b[0melse"
[✔]\x1b[1;38;5;255m python3.5\x1b[0m googlly.py "website.com"
[✔]\x1b[1;38;5;255m python3.5\x1b[0m googlly.py "21.1.13.11"
\x1b[0m"""))
def main():
    if len(sys.argv) == 1:
        header()
        sys.exit(0)
    askme=sys.argv[1]
    file1="result_of_"+askme+".txt"
    file2="short_links_"+askme+".txt"
    try:
        url = "https://www.google.com/search?q=%s"%askme
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:75.0) Gecko/20100101 Firefox/75.0"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+[\w+]', str(respData))
        checkphp = re.findall(r'[\w\.-?]+[\w\.-=]+[\w\.-?&=]+', str(urls))
        if checkphp:
            for xx in checkphp:
                urls2 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+[/0-9a-zA-Z]', str(xx))
                if urls2:
                    x=('\n'.join(map(str, urls2)))
                    d="[\x1b[1;38;5;119m+\x1b[0m]"
                    parsed_uri = urlparse(x)
                    pure_target = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                    url = re.compile(r"https?://(www\.)?")
                    pure_target = url.sub('', pure_target).strip().strip('/')
                    print(("""%sFound:\x1b[1;38;5;72m %s\x1b[0m"""%(d,x)))
                    SaveToIn = open("%s"%(file1), "a+")
                    SaveToIn.write("%s\n"%(x))
                    SaveToIn.close()
                    ## Remove # from SaveToIn2 if u want more info (junk links)
                    #SaveToIn4 = open("respData-%s.txt"%(askme), "a+")
                    #SaveToIn4.write("%s\n"%(str(respData)))
                    #SaveToIn4.close()
                    #SaveToIn3 = open("urls-%s.txt"%(askme), "a+")
                    #SaveToIn3.write("%s\n"%(str(urls)))
                    #SaveToIn3.close()
                    SaveToIn2 = open("%s"%(file2), "a+")
                    SaveToIn2.write("%s\n"%(str(pure_target)))
                    SaveToIn2.close()
                else:pass
        else:pass

    except Exception as e:
        print((str(e)))
    print(("\x1b[0m"))
    print(("""


    [+]Done saving to:

    %s

    %s


    """%(file1,file2)))
if __name__ == '__main__':
    main()
