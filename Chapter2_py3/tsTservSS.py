from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST=''
PORT=21567
ADDR=(HOST,PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...co nnected from',self.client_addres)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline().decode("UTF-8"))).encode("UTF-8"))
tcpSer=TCP(ADDR,MyRequestHandler)
print('waiting for connection...')
tcpSer.serve_forever()

#文本有错误

