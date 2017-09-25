#! /usr/bin/env python
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
    import json, base64
except ImportError:
    # Fall back to Python 2's
    import urllib2, base64, json

with open('config.json') as data_file:    
    data = json.load(data_file)

auth = 'Basic ' + base64.b64encode(data["Login"]["User"]+':'+data["Login"]["Password"])

def makeRequest(url,heads):
    request = urllib2.Request(url, None, heads)
    return (urllib2.urlopen(request)).read()

def getTotalTarget(number):
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm?Page='+str(number)
    
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def addTarget(Description,domain1,domain2,domain3,domain4):
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm?target_type=0&targets_lists_name='+Description+ '&dst_ip_start=&dst_ip_end=&dst_port_start=&dst_port_end=&proto=0&Commonport=0&url_0='+domain1+'&url_1='+domain2+'&url_2='+domain3+'&url_3='+domain4+'&Changed=0&SelIndex=0&fromAdd=0&Page=1&Save=Save'
    
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def addHostLan(Description,ipStart,ipEnd):
    Description = Description.replace(" ", "+")
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlHostsListsRpm.htm?addr_type=1&hosts_lists_name='+Description+'&src_ip_start='+ipStart+'&src_ip_end='+ipEnd+'&mac_addr=&Changed=0&SelIndex=0&fromAdd=0&Page=1&Save=Save'
    
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlHostsListsRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def countTarget(number):
    page = getTotalTarget(number)
    devices = []

    #Parse out target list
    page = page.split("new Array(", 1)
    page = page[1].split('0,0 );', 1)
    page = page[0].replace('"',"").replace(' ',"")
    data = page.split("\n")

    for index in range(len(data)):
        if(index != 0):
            devices.append( data[index].split(",") )

    return (len(devices))-1

def countTargets():
    return countTarget(1)+countTarget(2)

def addRule(ruleName,numberTarget):
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm?rule_name='+ruleName+'&hosts_lists=0&targets_lists='+str(numberTarget)+'&scheds_lists=255&enable=1&Changed=0&SelIndex=0&Page=1&Save=Save'
    
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def reboot():
    print ("Reboot")
    url = 'http://' + data["IpRouter"] + '/userRpm/SysRebootRpm.htm?Reboot=%D6%D8%C6%F4%C2%B7%D3%C9%C6%F7'
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/SysRebootRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def enableAccessControl():
    print ("Enable Acces Control")
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm?enableCtrl=1&defRule=0&Page=1'
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def deleteAllRules():
    print ("Delete all rules")
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm?doAll=DelAll&Page=1'
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def deleteAllHosts():
    print ("Delete all host")
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlHostsListsRpm.htm?doAll=DelAll&Page=1'
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlHostsListsRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def deleteAllTarget():
    print ("Delete all target")
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm?doAll=DelAll&Page=1'
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def setIpDevice(ip,mask):
    print ("Set ip device "+ip)
    url = 'http://' + data["IpRouter"] + '/userRpm/NetworkCfgRpm.htm?lanip='+ip+'&lanmask=3&inputMask='+mask+'&igmp_proxy=0&Save=Save'
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/NetworkCfgRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

if __name__ == "__main__":
    # reboot()

    # setIpDevice("192.168.0.2","255.255.255.0")

    # addTarget("Description","domain1","domain2","domain3","domain4")
    # deleteAllTarget()

    # addHostLan("Description","ipStart","ipEnd")
    # deleteAllHosts()

    # addRule("ruleName","numberTarget"):
    # deleteAllRules()

    # print countTargets()

    # enableAccessControl():