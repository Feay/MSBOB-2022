import os
f = open("UPIC.MDB", "rb")
# b sets binmode
file_size = (os.path.getsize("./UPIC.MDB"))
# makes a int long
print("File Size is: "+ str(file_size) +" bytes")
index=file_size-1 
# indexing at 0
i=-1
flip = 0
hit=0
exlen=0
header = b"\xd7\xcd\xc6\x9a"
footfake = b"\x00\x00\x00\xC6\x59\x03\x00"
footer = b"\x03\x00\x00\x00\x00\x00"
# hit is the frist instance of a header, we ignore ALL until we get a matching footer
# needed for logics
while i != index:
	i += 1
	f.seek(i)
	if flip == 0 :
		# if found hit move seek forwards case of doubles  IF symerical is found
		
		if header == f.read(4)	:
			flip = 1
			hit=i
			print("header found at:"+str(i))
			print("seeking")
	if flip == 1:
		if footfake == f.read(7) :
			flip = 0
			print("fake found at:"+str(i))
			print("printing file")
			exlen=(i-hit)+6
			f.seek(hit)
			# above works
			waffles = open(str(hit)+"bob.wmf", "wb")
			f.seek(hit)
			# f.seek(hit) is needed AGAIN else the blow fails and acts like it was f.seek(i)
			waffles.write(f.read(exlen))
			waffles.close()
		f.seek(i)
		#just incase
		if footer == f.read(6) :
			flip = 0
			print("footer found at:"+str(i))
			print("printing file")
			exlen=(i-hit)+6
			f.seek(hit)
			# above works
			waffles = open(str(hit)+"bob.wmf", "wb")
			f.seek(hit)
			# f.seek(hit) is needed AGAIN else the blow fails and acts like it was f.seek(i)
			waffles.write(f.read(exlen))
			waffles.close()
			
# it is possible that a footer of d7 30 46 00 causes the file to be invalid...could this be something to do with thumbnails or exrta stuff of apps/?
#  03 00 00 00 00 C6 59 03 00	 03 00 00 00 00 C6 59 03 00 filtering fixes many more files
# 20 07 00 00 00 00 A0 30 46 00 
# A0 02 00 00 00 00 C6 59 03 00 this works
	
# comment seek starts at 0
print("end")
