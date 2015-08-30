
#!/usr/bin/python
import os
def accepted(path,lines):
	word='Accepted'
	b=0
	ipcont=[]
	ip=[]
	ipIndex=0
	
	for line in lines:
		palabras = line.split(' ')
		
		for p in palabras:
			if p==word and (palabras[7]=='password' or palabras[6]=='password') and (palabras[8]=='for' or palabras[7]=='for'):			
				ipIndex=0
				for c in range(len(ip)):
					if palabras[11]==ip[c] or palabras[10]==ip[c]:
						b=1
						ipcont[c]=ipcont[c]+1
					
		

				if b==0:		
					#print(palabras[11])
					if palabras[7]=='password':
						ip.append(palabras[11])
					if palabras[6]=='password':
						ip.append(palabras[10])
					ipcont.append(1)
				
				
		b=0	

		

	for i in range(len(ip)):
		print "IP ",ip[i], "has entered",ipcont[i]," times."


def failed(path,lines):
	word='Failed'
	b=0
	ipcont=[]
	ip=[]
	ipIndex=0;
	for line in lines:
		palabras = line.split(' ')
		
		for p in palabras:
			#print palabras
			if p==word and (palabras[6]=='Failed' or palabras[5]=='Failed') and (palabras[6]=='password' or palabras[7]=='password') and (palabras[8]!='invalid' and palabras[9]!='invalid'):		

				ipIndex=0
				for c in range(len(ip)):
					if palabras[11]==ip[c] or palabras[10]==ip[c]:
						b=1
						ipcont[c]=ipcont[c]+1
						
					
		

				if b==0:		
					#print(palabras[11])
					if palabras[6]=='Failed':
						ip.append(palabras[11])
					if palabras[5]=='Failed':
						ip.append(palabras[10])
					ipcont.append(1)
			
					
				
		b=0	
	num=len(ip)	
	for i in range(num):
		print "IP ",ip[i], "has failed the password ",ipcont[i]," times."

path='/var/log/auth.log'

infile=open(path,'r')
lines=infile.readlines()
function = { '1': failed,'2':accepted}
operation=raw_input("1.- Failed\n2.- Accepted ")
function[operation](path,lines)



# CLosing the file
infile.close()



