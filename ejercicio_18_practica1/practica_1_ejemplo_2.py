# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 07:53:15 2022

@author: Alumno
"""

import logging
import time
import threading

formato_logging=\
'%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=formato_logging,level=logging.INFO,
                    datefmt='%H:%M:%S',force=True)


numero_a_palabra={1:'Uno',2:'Dos',3:'Tres',4:'Cuatro',5:'Cinco'}

def retrasar_mensaje(retraso,mensaje):
    logging.info('{} recibido'.format(mensaje))
    time.sleep(retraso)
    logging.info('Imprimiendo {}'.format(mensaje))
    
def main():
    logging.info('Main iniciado')
    hilos=[threading.Thread(target=retrasar_mensaje,args=(retraso,mensaje)) 
           for retraso,mensaje in zip([2,4], [numero_a_palabra[2],numero_a_palabra[4]])]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    logging.info('Main terminado')
    
main()
