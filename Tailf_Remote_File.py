#!/usr/bin/env python
# coding:utf8
#
#       The script is cat AllServer logs file for windows
#			by: catmint
#

import os, sys

ServerLog = "tailf /data/project/game-service/logs/all.log"
GatewayLog = "tailf /data/project/game-gateway/logs/all.log"  # java logs
FlumeLog = "tailf /data/bigdata/flume/apache-flume-1.6.0-bin/flume.log"

HdfsBase = "tailf /data/bigdata/hadoop/hadoop-2.7.2/logs/"
NameFile = HdfsBase + "hadoop-root-namenode-VM_0_123_centos.log"  # HDFS Logs dir
DataFile1 = HdfsBase + "hadoop-root-datanode-VM_0_7_centos.log"
DataFile2 = HdfsBase + "hadoop-root-datanode-VM_0_181_centos.log"

ServerIp = ["172.16.0.242", "172.16.0.149", "172.16.0.2"]
GatewayIp = ["172.16.0.53", "172.16.0.134", "172.16.0.228"]  # IPlist
NameIp = ["172.16.0.123"]
DataIp = ["172.16.0.7", "172.16.0.181"]
HdfsIp = NameIp + DataIp

global TailList

TailList = []



def Command(host):
    cmd = "multitail" + host
    #print cmdi					#DEBUG
    os.system(cmd)


def Remote(ip, file):
    host = " -l " + '"ssh root@' + ip + " '" + file + "'" + '"'
    TailList.append(host)


def CatServer():
    for ip in ServerIp:
        Remote(ip, ServerLog)


def CatGateway():
    for ip in GatewayIp:
        Remote(ip, GatewayLog)


def CatFlume():
    for ip in HdfsIp:
        Remote(ip, FlumeLog)


def CatHdfs():
    # for nameip in NameIp:
    #     Remote(nameip, NameFile)
    Remote(NameIp[0], NameFile)
    Remote(DataIp[0], DataFile1)
    Remote(DataIp[1], DataFile2)


def help():
    print '''

    ./Logs.py flume          Flume日志
    ./Logs.py hdfs           查看hdfs日志
    ./Logs.py server         游戏服日志
    ./Logs.py gateway        网关服日志


    '''

def main():
    try:
        choice = sys.argv[1]
    except:
	help()
	exit()
    if choice == "flume":
        CatFlume()
    elif choice == "server":
        CatServer()
    elif choice == "gateway":
        CatGateway()
    elif choice == "hdfs":
        CatHdfs()
    else:
        help()
        exit()
    str_tail = "".join(TailList)
    Command(str_tail)
	
	
if __name__ == '__main__':
        main()
