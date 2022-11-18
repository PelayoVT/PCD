import threading								#libreria para hilos
import sys										#libreria para hablar con el sistema
import socket									#libreria para comunicarse con otra consola
import pickle									#pasar a binario (serializar y desserializar)
import os										#hablar con el sistema operativo

class Cliente():

	def __init__(self, host=input("Intoduzca la IP del servidor ?  "), port=int(input("Intoduzca el PUERTO del servidor ?  ")), nick=""): #pide el host y el puerto por el que se va a conectar
		self.s = socket.socket()
		while (nick ==""):
			nick = input ("Introduce tu nombre de usuario: ")
		self.nick = nick
		with open("nicknameList.txt", "a") as f:
			f.write(self.nick + "\n")
		self.s.connect((host, int(port)))
            
		print('\n\tProceso con PID = ',os.getpid(), '\n\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\n\tTotal Hilos activos en este punto del programa =', threading.active_count())
		threading.Thread(target=self.recibir, daemon=True).start()
		

		while True:
			msg = input('\nEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1 \n')
			if msg != '1' : self.enviar(msg)
			else:
				print(" **** Me piro vampiro; cierro socket y mato al CLIENTE con PID = ", os.getpid())
				self.deleteNick(nick)
				self.s.close()
				sys.exit()
                
	def deleteNick(self, nick):
		lines = []
		with open("nicknameList.txt", "r") as f:
			nicknames = f.readlines()
			for n in nicknames:
				if (nick not in n):
					lines.append(n)
		with open ("nicknameList.txt", "w") as f:
			for n in lines:
				f.write(n)

	def recibir(self):
		print('\nHilo RECIBIR con ID =',threading.currentThread().getName(), '\n\tPertenece al PROCESO con PID', os.getpid(), "\n\tHilos activos TOTALES ", threading.active_count())
		while True:
			try:
				data = self.s.recv(128)
				if data: print(pickle.loads(data))
			except: pass

	def enviar(self, msg):
		self.s.send(pickle.dumps(self.nick + ": " + msg))
        
		with open ("22166209.txt", "a") as f:
			f.write(self.nick + " : " + msg + "\n")

arrancar = Cliente()

		