
from scapy.all import *
import sys
import configparser

config=configparser.ConfigParser()
config.read('config.conf')
mac=[]
ip=[]
def printConf():
	for i in range(len(mac)):
        	config['ARP'][ip[i]]=mac[i]
        	i=i+1
        	with open('config.conf','w') as configfile:
                	config.write(configfile)

def findKey():
	keyList=[]
	for key in config['ARP']:
		keyList.append(key)
	return keyList

def findValue():
	valueList=[]
	for value in config['ARP'].values():
		valueList.append(value)
	return valueList

if(config['FIRSTTIME']['firsttime']=='0'):
	config['FIRSTTIME']['firsttime']='1'
    	with open('config.conf','w') as configfile:
    		config.write(configfile)
	sbx=config['SETTINGS']['subnet']
	ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sbx),timeout=2)
	for s,r in ans:
		mac.append(r.sprintf("%Ether.src%"))
		ip.append(r.sprintf("%ARP.psrc%"))
	printConf()
else:
	key=findKey()
	value=findValue()
	
	subnet=config['SETTINGS']['subnet']
        ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=subnet),timeout=2)
        for s,r in ans:
                mac.append(r.sprintf("%Ether.src%"))
                ip.append(r.sprintf("%ARP.psrc%"))
        for i in range (len(mac)):
		if mac[i] in value:
                	for j in range (len(value)):
				if(mac[i]==value[j]):
                        		if(ip[i]!=key[j]):
						answer=raw_input("Aginizdaki bir cihazin IP adresi ("+key[j]+") degismis guncellemek istiyor musunuz?\n-Yeni IP adresi=("+ip[i]+")(e/h):\n")
						if(answer=='e' or answer=='E'):
							with open('config.conf','w') as configfile:
								config.remove_option('ARP',key[j])
								config.write(configfile)
							config['ARP'][ip[i]]=mac[i]
							with open('config.conf','w') as configfile:
                                       				config.write(configfile)
						elif(answer=='h' or answer=='H'):
							continue
		else:
			answer2=raw_input("Aga yeni cihaz katilmis eklenmesini istiyor musunuz?\n-MAC=("+mac[i]+")-IP=("+ip[i]+")(e/h):\n")
			if(answer2=='e' or answer2=='E'):
				config['ARP'][ip[i]]=mac[i]
				with open('config.conf','w') as configfile:
                               		config.write(configfile)
			elif(answer2=='h' or answer2=='H'):
				continue
