from googletrans import Translator
import configparser
import os,sys
from questions import *
import time

baba_dir = get_baba_dir() #Initiates questioning sequence for the baba directory

lang = configparser.ConfigParser()

with open(os.path.join(baba_dir,"Data/Languages/lang_en.txt"),"r") as file:
	english_data = file.read()

english_data=english_data.replace("%","")

lang.read_string(english_data)

translator = Translator()

lang["general"]["Name"]="Google Translate"

language_sequence=["la","yi","ar","ru","hmn","ja","lo","ko","en"]
prev_langcode = "en"

texts = list(lang["texts"].values())

print("This will take a bit!")

translated=0

for langcode in language_sequence:
	for i in range(len(texts)):
		worked=False
		while not worked:
			try:
				texts[i]=translator.translate(texts[i],dest=langcode,src=prev_langcode).text
			except AttributeError:
				worked=False
				print(f"{translated}/{len(texts)*len(language_sequence)} translated-Error, retrying-",end="\r")
				time.sleep(3)
			else:
				worked=True
		translated+=1
		print(f"{translated}/{len(texts)*len(language_sequence)} translated-----------------",end="\r")
	prev_langcode=langcode
	print("\nTranslation to "+langcode+" done")

for i,text in enumerate(lang["texts"]):
	lang["texts"][text]=texts[i]

lang.write(os.path.join(baba_dir,"Data/Languages/lang_googletranslate.txt"))