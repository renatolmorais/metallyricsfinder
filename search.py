#!/usr/bin/env python

import sys,os
#import httplib
import requests
import re

proxies = { "http_proxy": "http://proxy.almg.uucp:3128/", "https_proxy": "http://proxy.almg.uucp:3128/", "ftp_proxy": "http://proxy.almg.uucp:3128/" }

def get_url( path ):
    host = "http://www.darklyrics.com"
    return requests.get( host + "/" + path, proxies=proxies )

if __name__ == '__main__':

	#banda = raw_input("Digite o nome da banda: ")
	banda = sys.argv[1]
	#musica = raw_input("Digite o nome da musica: ")
	musica = sys.argv[2]
        htmlpage = ''
	
	#banda = banda.lower()
	#musica = musica.lower()
	
	#print "GET %s.html"%(banda[0])
	
	# obter conexao
        try:
            # Obter as paginas com as bandas que comecam com a mesma letra
            url = "{0}.html".format( banda[0] )
            response = get_url( url )
            if response.status_code != 200: raise Exception('status code not 200')
            htmlpage = response.text
        except Exception as err:
            print err.message

        try:	
            # Obter a pagina da banda
            pattern = '<a href=".*%s.*</a>'%(banda.upper())
            result = re.search(pattern,htmlpage)
            path = result.group()
            init = path.find('"')
            end = path.rfind('"')
            url = path[init + 1:end]
            #print url
            response = get_url( url )
            if response.status_code != 200: raise Exception('status code not 200')
            htmlpage = response.text
        except Exception as err:
            print err.message

        try:
            # Obter a pagina da musica
            pattern = '<a.*%s.*</a>'%(musica)
            #print pattern
            result = re.search(pattern,htmlpage,flags=re.IGNORECASE)
            path = result.group()
            init = path.find('"')
            end = path.rfind('"')
            url = path[init + 1:end]
            url = url[2:]
            #print url
            response = get_url( url )
            if response.status_code != 200: raise Exception('status code not 200')
            htmlpage = response.text
        except Exception as err:
            print err.message

        try:
            # Obter a letra da musica
            pattern = '<h3.*%s.*</h3>'%(musica)
            #print pattern
            #pattern = '<h3.+</h3>'
            #result = re.search(pattern,htmlpage,flags=re.IGNORECASE)
            result = re.findall('<h3.+</h3>',htmlpage,flags=re.IGNORECASE)
            #print re.split(pattern,htmlpage)
            #if result: print result
            pos = 0
            for string in result:
            	match = re.search(pattern,string,flags=re.IGNORECASE)
            	if match: break
            	pos = pos + 1
            init = htmlpage.find(result[pos])
            print len(result)
            print init
            print pos + 1
            if pos + 1 < len(result): end = htmlpage.find( result[pos + 1] )
            else: end = len(htmlpage) 
            print htmlpage[init:end]
        except Exception as err:
            print err.message
