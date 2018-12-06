#!/usr/bin/env python

import sys,os
import httplib
import re

def get_connection( url ):
	return httplib.HTTPConnection( url )

if __name__ == '__main__':

	#banda = raw_input("Digite o nome da banda: ")
	banda = sys.argv[1]
	#musica = raw_input("Digite o nome da musica: ")
	musica = sys.argv[2]
	
	#banda = banda.lower()
	#musica = musica.lower()
	
	#print "GET %s.html"%(banda[0])
	
	# obter conexao
	conn = get_connection( "www.darklyrics.com" )
	
	# Obter as paginas com as bandas que comecam com a mesma letra
	
	url = "/{0}.html".format( banda[0] )
	conn.request("GET",url)
	response = conn.getresponse()
	htmlpage = response.read()
	
	# Obter a pagina da banda
	pattern = '<a href=".*%s.*</a>'%(banda.upper())
	result = re.search(pattern,htmlpage)
	path = result.group()
	init = path.find('"')
	end = path.rfind('"')
	url = "/" + path[init + 1:end]
	#print url
	conn.request("GET",url)
	response = conn.getresponse()
	htmlpage = response.read()
	
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
	conn.request("GET",url)
	response = conn.getresponse()
	htmlpage = response.read()
	#print htmlpage
	
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
	#	print string
		match = re.search(pattern,string,flags=re.IGNORECASE)
		if match: break
		pos = pos + 1
	#print result[pos]
	#print result[pos + 1]
	init = htmlpage.find(result[pos])
	end = htmlpage.find(result[pos + 1])
	print htmlpage[init:end]


