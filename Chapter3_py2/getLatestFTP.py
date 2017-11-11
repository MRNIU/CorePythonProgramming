import ftplib
import os
import socket

HOST='ftp.mozilla.org'
DIRN='pub/mozilla.org/wedtools'
FILE='bugzilla-LATEST.tar.gz'

def main():
    try:
        f=ftplib.FTP(HOST)
    except(socket.error,socket.gaierror) as e:
        print 'ERROR:cannot reach "%s"'%HOST
        return
    print '*** Connect to host "%s"'%HOST

    try:
