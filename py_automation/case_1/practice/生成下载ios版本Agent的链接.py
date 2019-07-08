
# -*- encoding: utf-8 -*-
import json
import base64
import urllib
# import logging
import sys
# proDir = os.path.split(os.path.realpath(__file__))[0]
#import os
#import codecs
#import configparser
# print(proDir)
# ios_appName = "SGAgent_iOS_3.1.0_143.ipa"

# test.cms.skyguard.com.cn

def download_ios_mobile(ios_appName, mag_domain_name):
    appName = ios_appName[-5:0:-1]
    namelength=len(appName)+1
    realName = ios_appName[0]+appName[-1:-namelength:-1]
    # print(realName)
    appDownloadUrl = "/mobile/v1/device/appFile/mobile_agent/"+ios_appName

    urlPrefix = "https://" + mag_domain_name + ":8082"

    params = {'ipaDownloadUrl': urlPrefix + appDownloadUrl, 'appName': realName, 'bundleId': "com.skyguard.endpoint.ios.agent.MobileAgent"}
    paramsStr = json.dumps(params)
    # print(paramsStr)
    plistUrl = urlPrefix + '/mobile/v1/device' + '/plist/' + base64.b64encode(paramsStr)
    appDownloadUrl = 'itms-services://?action=download-manifest&url='+urllib.quote(plistUrl, '')

    print("ios版本" + ios_appName + "下载链接是: " + appDownloadUrl)

    # logging.basicConfig(level=logging.DEBUG)
    # logging.debug(appDownloadUrl)

while(True):
    try:
        if sys.argv[1] == '' or sys.argv[2] == '':
            print("请输入iOS版本的客户端全称和MAG域名")
            continue
        else:
            ios_appName = sys.argv[1]
            mag_domain_name = sys.argv[2]
            download_ios_mobile(ios_appName, mag_domain_name)
            break
    except:
        print("请输入iOS版本的客户端全称和MAG域名，如 SGAgent_iOS_3.1.0_143.ipa test.cms.skyguard.com.cn")
        exit(1)

