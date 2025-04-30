#Program for Creating Folders  Hierarchy
#makedirsex.py
import os
try:
	os.makedirs("D:\\India\\Hyd\\ampt\\python\\python")
	print("Folder Created Successfully-verify")
except FileExistsError:
	print("The specified folder already exist")
except OSError:
	print("Check ur path of folder names")
