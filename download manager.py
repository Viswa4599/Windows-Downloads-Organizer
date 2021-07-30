'''
Script borrowed from https://medium.com/better-programming/how-i-organise-my-downloads-folder-with-python-6c76358968ea
Few modifications made.
'''


from os import listdir
from os.path import isfile, join
import os
import shutil

IMAGES = ['png','jpeg','jpg']
DOCUMENTS = ['pdf','docx','doc','ppt','pptx']
APPLICATIONS = ['exe']
COMPRESSED  = ['iso','rar','zip']
SCRIPTS = ['py','c','cpp','jar']
SHEETS = ['xls','xlsx']


FOLDERS = {'IMAGES':IMAGES,'DOCUMENTS':DOCUMENTS,'APPLICATIONS':APPLICATIONS,'COMPRESSED':COMPRESSED,'SCRIPTS':SCRIPTS,'SHEETS':SHEETS}

def sort_files_in_a_folder(mypath):    
	'''
    A function to sort the files in a download folder
    into their respective categories
	''' 
	files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	file_type_variation_list=[]

	filetype_folder_dict={}  
	broad_filetype = None
	for file in files:
		print(file)
		filetype=file.split('.')[-1]
		if filetype not in file_type_variation_list:
			for folder in FOLDERS:
				if filetype in FOLDERS[folder]:
					broad_filetype = folder #image, documents etc

			print(broad_filetype)
			if broad_filetype is None:
				continue
			file_type_variation_list.append(filetype)
			new_folder_name=mypath+'/'+broad_filetype
			filetype_folder_dict[str(filetype)]=str(new_folder_name)

			if os.path.isdir(new_folder_name)==True:  #folder exists
				continue
			else:
				os.mkdir(new_folder_name)    

	dest_path = ''
	for file in files:
		src_path=mypath+'/'+file
		filetype=file.split('.')[-1]
		#	print(filetype_folder_dict.keys())
		if filetype in filetype_folder_dict.keys():
			print('hi')
			dest_path=filetype_folder_dict[str(filetype)]
			try:
				shutil.move(src_path,dest_path)    
			except:
				print('Redundant copy')
				print(src_path)
				os.rename(src_path,mypath+'/'+'COPY-'+file)
				shutil.move(src_path,dest_path)    
				

	#try:
	print(src_path + '>>>' + dest_path)
	#xcept:
	#	print('No new files')

if __name__=="__main__":
	mypath="C:/Users/Acer/Downloads"	
	sort_files_in_a_folder(mypath)