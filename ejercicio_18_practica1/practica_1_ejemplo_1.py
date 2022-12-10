import logging
import time

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
    retrasar_mensaje(2, numero_a_palabra[2])
    retrasar_mensaje(2, numero_a_palabra[4])
    logging.info('Main terminado')
    
main()
