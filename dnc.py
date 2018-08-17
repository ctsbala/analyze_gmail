import urllib.request
import time
# Download the file from `url` and save it locally under `file_name`:

for x in range(29,5000):
	if x%20== 0:
		print("sleeping")
		time.sleep(10);
	try:
		print ("downloading email id " +str(x)) 
		urllib.request.urlretrieve("http://wikileaks.com/dnc-emails//get/"+str(x),"/Users/ss2688/Documents/EML/E"+str(x)+".EML")
	except:
		print("some error "+str(x))


