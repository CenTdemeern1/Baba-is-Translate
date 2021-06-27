import googletrans
import sys

def ask(question,answers=None,case_sensitive=True,print_possibilities=False):
	print("\n")
	if print_possibilities:
		print("Possible answers are: "+", ".join(list(answers)))
	if case_sensitive:
		print("[Case sensitive] ",end="")
	a = input(question+"\n> ").lower()
	if answers!=None:
		while not a in answers:
			print("Invalid answer.\nPossible answers are: "+", ".join(list(answers)))
			a = input(question+"\n> ")
		return answers[a]
	else: return a

baba_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baba Is You"

ask_for_path = True
default_location = False

owns_baba_on_steam = ask("Do you own Baba on Steam?",{"yes":True,"no":False},case_sensitive=False)

if owns_baba_on_steam:
	default_location = ask("Do you have Baba and Steam installed in the default location?\n"+baba_dir,{"yes":1,"no":0,"i don't know":2},case_sensitive=False,print_possibilities=True)
	if default_location==2:
		print("If you don't know, you probably do. So I'll default to yes.")
	default_location=bool(default_location)
	if default_location:
		ask_for_path=False

if ask_for_path:
	where_is_the_baba_dir = ask("Where do you have Baba installed?")
	if where_is_the_baba_dir.lower()=="i don't know":
		print("Sorry, then you should probably figure that out first.\nIf you have a shortcut on your desktop, you can right-click it, and select \"Open file location\".")
		input("Press enter to close the program.")
		sys.exit(0)
	baba_dir = where_is_the_baba_dir

