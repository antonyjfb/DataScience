# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 08:10:53 2022

@author: Alumno
"""

import logging
import time
import concurrent.futures as cf

formato_logging=\
'%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=formato_logging,level=logging.INFO,
                    datefmt='%H:%M:%S',force=True)


numero_a_palabra={1:'Uno',2:'Dos',3:'Tres',4:'Cuatro',5:'Cinco'}

def retrasar_mensaje(retraso,mensaje):
    logging.info('{} recibido'.format(mensaje))
    time.sleep(retraso)
    logging.info('Imprimiendo {}'.format(mensaje))
    return mensaje
    
if __name__=='__main__':
    with cf.ThreadPoolExecutor(max_workers=2) as ejecutor:
        mapeo={ejecutor.submit(retrasar_mensaje,i,numero_a_palabra[i]):numero_a_palabra[i] for i in [2,4]}
        for futuro in cf.as_completed(mapeo):
            logging.info('{} Completado'.format(futuro.result()))
