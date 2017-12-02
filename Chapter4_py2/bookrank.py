
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGX=compile('#([\d,]+) in Books ')
AMZN="http://amazon.com/dp/"
ISBNs={
    '0132269937':"Core Python Programming",
    '0132356139':"Python Web Development with Django",
    '0137143419':"Python Fundamentals",
}

def getRanking(isbn):
    page=uopen('%s%s' % (AMZN,isbn)) # or str.format()
    data=page.read()
    page.close()
    return REGX.findall(data)[0]

def _showRanking(isbn):
    print "- %r ranked %s" % (ISBNs[isbn],getRanking(isbn))
    #Thread(target=_showRanking, args=(isbn,)).start()

def _main():
    print "At",ctime(),"on Amanon..."
    for isbn in ISBNs:
        _showRanking(isbn)

@register
def _atexit():
    print "all Done at:",ctime()

if __name__ == '__main__':
    _main()