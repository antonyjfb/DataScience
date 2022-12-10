# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 08:35:39 2022

@author: Alumno
"""

import logging
import time
import requests

formato_logging=\
'%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=formato_logging,level=logging.INFO,
                    datefmt='%H:%M:%S',force=True)

def descargar_todo(sitios):
    pass

def descargar_sitios(url,session):
    pass

if __name__ == '__main__':
    sitios_web=['http://imagenenlaciencia.blogspot.com/2017/11/los-sismos-de-septiembre-en-la-revista.html',
                'http://imagenenlaciencia.blogspot.com/2013/12/realidad-virtual-intracraneal.html',
                'http://imagenenlaciencia.blogspot.com/2013/06/sol-sticial.html',
                'http://imagenenlaciencia.blogspot.com/2013/06/mensajes-secretos.html']*10
    hora_inicio=time.time()
    descargar_todo(sitios_web)
    duracion=time.time()-hora_inicio
    print('\nSe descargaron {} sitios en {} segundos'.format(len(sitios_web),duracion))