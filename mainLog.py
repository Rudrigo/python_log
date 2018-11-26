#!/usr/bin/python

# By Rudrigo Lima 
# rudrigo@musca.io
# 81-998011720
# Script de log - conexao 

import sys
import os
import subprocess
import urllib
import re
from time import sleep
import time 

global ipExt
ipExt =  '8.8.8.8'

def reStart():
    print 'Rebooting...'
    os.system('sudo reboot')

def system_call(command):
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()

def get_gateway(): # pega ip do gateway
    valor = system_call("ip route | grep default | awk '{print $3}'").strip(" ")
    valor = valor.rstrip('\n')
    return valor

def get_ipreal(): # pega ip real do modem 
    ipreal = urllib.urlopen("http://api.ipify.org").read()
    return ipreal


def main():

    while True:
      arq = open('/home/pi/log/logMusca.txt','a')
      arq.write('----Log '+time.strftime('%Y/%m/%d %H:%M:%S')+ '------------------------ \n')

      responseRoute = os.system ("ping -c 1 " + get_gateway())
      if responseRoute == 0:
          print 'Ip Route  '+get_gateway()+' Status - ON'
          arq.write('Ip Route  '+get_gateway()+' Status - ON \n')
          sleep(5)

          responseExt = os.system ("ping -c 1 " + ipExt)
          if responseExt == 0:
             print 'Ip Ext    '+ipExt+' Status - ON'
             arq.write('Ip Ext    '+ipExt+' Status - ON \n')
             sleep(5)

             responseIpReal = os.system ("ping -c 1 " + get_ipreal())
             if responseIpReal == 0:
                print 'Ip Real   '+get_ipreal()+' Status - ON'
                arq.write('Ip Real   '+get_ipreal()+' Status - ON \n')
                sleep(5)
             else:
                print 'Ip Real  0.0.0.0  Status - OFF'
                arq.write('Ip Real  0.0.0.0  Status - OFF \n')

          else:
             print 'Ip Ext    0.0.0.0  Status - OFF'
             arq.write('Ip Ext    0.0.0.0 Status - OFF \n')

             print 'Ip Real  0.0.0.0  Status - OFF'
             arq.write('Ip Real  0.0.0.0  Status - OFF \n')

      else:
        print 'Ip Route  0.0.0.0  Status - OFF'
        arq.write('Ip Route  0.0.0.0 Status - OFF \n')

        print 'Ip Ext    0.0.0.0  Status - OFF'
        arq.write('Ip Ext    0.0.0.0 Status - OFF \n')

        print 'Ip Real   0.0.0.0  Status - OFF'
        arq.write('Ip Real   0.0.0.0  Status - OFF \n')

        print 'Reboot Raspberry'
        arq.write('Rebooting... '+time.strftime('%Y/%m/%d %H:%M:%S') +'...\n')
        arq.write('----Fim---------------------------------------------\n\n')
        sleep(15)
        arq.close()
        reStart()


      arq.write('----Fim---------------------------------------------\n\n')
      arq.close()
      sleep(5)
      arq.close()
      print'Fim do script!'

if __name__ == '__main__':
    main()
