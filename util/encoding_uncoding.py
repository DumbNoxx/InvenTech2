from cryptography.fernet import Fernet

def generar_clave():
	clave = Fernet.generate_key()
	with open("clave.key","wb") as archivo_clave:
		archivo_clave.write(clave)

def cargar_clave():
	return open('clave.key','rb').read()

generar_clave()

clave = cargar_clave()

def encrypted(password:str):
	f = Fernet(clave)
	b_password = bytes(password,'ascii')
	encrypted_password = f.encrypt(b_password)
	return encrypted_password.decode('ascii')


def decrypt(password:str):
	f = Fernet(clave)
	b_password = bytes(password,'ascii')
	b_password_decrypt = f.decrypt(b_password)
	return b_password_decrypt.decode('ascii')

