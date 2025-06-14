try:
   file=open('sample.txt','r')
   file_read=file.read()
   print(file_read)
except:
   print('the file ''sample.txt'' was not found exit')
