import sys
import os
import subprocess
import shutil
from pathlib import Path

import getpass

from DisKoGraphY import DiscoG
from InHerAS4s7 import inA5S

dev = 0

m0D3 = 0
EdiT = 0
h3r3 = ""
MaN = 0

##Fix more than one - in title :) .

h3r3 = str(Path( __file__ ).parent.absolute())

source = []

def FrR():
	if "Installed" not in str(subprocess.check_output(["apt-cache", "policy","ffmpeg"])) and MaN != 1:
		acquire = input('\nMissing Packages: The software will run but won\'t output FLAC files.\n\n  Do you want to install missing packages (If you don\'t have apt you can install ffmpeg manually, THEN select no)? (Y/n) ')
		if (acquire == "" or acquire == "Y" or acquire == "y"):
			os.system('/bin/bash -c "sudo apt install ffmpeg -y"')

def Fr():
	global h3r3

	if (os.path.isfile(h3r3 + "/PreperationsDon3.txt")):
		if "47" in open(h3r3 + "/PreperationsDon3.txt", "r").read(): 
			dev = 1
			print("♥️")#print(open(h3r3 + "/PreperationsDon3.txt", "r").read())#if "47" in open(h3r3 + "/PreperationsDon3.txt", "r").read(): dev = 1
	else:
		SettingsF = open(h3r3 + "/settings.json", "r")
		Settings = SettingsF.read()

		open(os.path.join(h3r3, "/settings.json"), "w").write(Settings.replace('"/mnt/x/Music/FLAC/"', '"' + input('\nWhat directory do you want to download the music to? ') + '"'))

		shutil.copy(h3r3 + "/settings.json", "/home/" + getpass.getuser() + "/.config/tidal_dl_ng/settings.json")

		upForit = input('\nWould you like to edit your config (It\'s been premoded to the highest quality)? (Y/n) ') 
		
		if (upForit == "" or upForit == "Y" or upForit == "y"):
			os.system('/bin/bash -c "nano /home/' + getpass.getuser() + '/.config/tidal_dl_ng/settings.json"')

		open(os.path.join(h3r3, "/PreperationsDon3.txt"), "w").write("❤️")



def m0De():
	global source
	global m0D3
	global MaN

	if (len(sys.argv) == 2):
		if (sys.argv[1] == "2"):
			m0D3 = 1

			if (not os.path.isfile(h3r3 + "/PreperationsDon3.txt")):
				Fr()
			else:
				os.system('/bin/bash -c "nano /home/' + getpass.getuser() + '/.config/tidal_dl_ng/settings.json"')

			EdiT = 1
		if (sys.argv[1] == "man"):
			m0D3 = 1 
			print (open(h3r3 + "/bin/man.man", "r").read())
			MaN = 1
		what = sys.argv[1]

def DowNloaD():
	global source
	global h3r3

	D0neSOurc3 = []

	if (len(sys.argv) == 1): source = input('\nEnter TIDAL Song/Album or Playlist link(s) seperated by commas (","): ').split(",")

	if (len(sys.argv) == 2 and sys.argv[1].startswith("https://tidal")):
		if "," in sys.argv[1]: 
			source = sys.argv[1].split(",")
		else: 
			source.extend(sys.argv[1])

	if (m0D3 == 1 and len(sys.argv) == 2): 
		if (sys.argv[1] == "1"):
			source = open(h3r3 + "/Ingredients.txt", "r").read().split("\n")

	for hit in source:
		if "http" in hit:
			if "artist" in hit:
				D0neSOurc3 = D0neSOurc3 + DiscoG(hit)
			else: D0neSOurc3.append(hit)

	for hit in D0neSOurc3:
		os.system('/bin/bash -c "source ' + h3r3 + '/bin/activate && tidal-dl-ng dl ' + hit + '"')
		FixTitles()

	if (m0D3 == 1):
		open(os.path.join(h3r3, "/Ingredients.txt"), "w").write("")

def FixTitles():
	global dev

	i=0

	Folder = ""
	NewN = ""

	Heaven = open("/home/" + getpass.getuser() + "/.config/tidal_dl_ng/settings.json", "r").read().split('"download_base_path": "')[1].split('",')[0]

	if not os.path.isdir(Heaven + "/Albums"):
		os.mkdir(Heaven + "/Albums")
		if not os.path.isdir(Heaven + "/Albums/Done"):
			os.mkdir(Heaven + "/Albums/Done")
	if not os.path.isdir(Heaven + "/Tracks"):
		os.mkdir(Heaven + "/Tracks")
		if not os.path.isdir(Heaven + "/Tracks/Done"):
			os.mkdir(Heaven + "/Tracks/Done")
	if not os.path.isdir(Heaven + "/Playlists"):
		os.mkdir(Heaven + "/Playlists")
		if not os.path.isdir(Heaven + "/Playlists/Done"):
			os.mkdir(Heaven + "/Playlists/Done")

	if EdiT != 1 and MaN !=1:
		for x in os.walk(Heaven + "/Albums"):
			for y in os.walk(x[0]):
				if (y[0].count("(Explicit)") > 0 or y[0].count(",") > 0 or y[0].count("Done") == 0):
					if not "Done" in y[0]:
						for z in y[2]:
							if ("," in z):
								Folder = os.path.join(y[0], z)
								if "," in z.split("-")[0]:
									if dev == 1:
										NewN = os.path.join(y[0], z.split(",")[0] + " -" + z.split("-")[1].replace("(Explicit)", "") + " [FLAC] [TIDAL]-TRiPPERS")
									else:
										NewN = os.path.join(y[0], z.split(",")[0] + " -" + z.split("-")[1].replace("(Explicit)", ""))

								else:
									if dev==0:
										NewN = os.path.join(y[0], z.replace("(Explicit)", ""))
									else:
										NewN = os.path.join(y[0], z.replace("(Explicit)", "") + " [FLAC] [TIDAL]-TRiPPERS")

								if Folder != Heaven + "/Albums":
									ReNam3(Folder, NewN, 0)

					if not "Done" in y[0]:

						if ("," in y[0].split("-")[0]):
							LocationS = str(y[0].replace("Albums/", "Albums/Done/")).split(",")[0] + " -" + str(y[0]).split("-")[1].replace("(Explicit)", "").replace("(Explicit)", "").rstrip()
						else:
							LocationS = str(y[0].replace("Albums/", "Albums/Done/")).replace("(Explicit)", "").rstrip()

						if i!=0:
							ReNam3(y[0], LocationS, 0)
				i += 1

		LocationS = open("/home/" + getpass.getuser() + "/.config/tidal_dl_ng/settings.json", "r").read().split('"download_base_path": "')[1].split('",')[0]

		for x in os.walk(LocationS + "/Tracks/"):
			for y in x[2]:
				if (not "Done" in x[0]):
					artists = y.split(" -")
					if "," in artists[0]:
						ReNam3(os.path.join(x[0], y), os.path.join(x[0].replace("Tracks/", "Tracks/Done/"), artists[0].split(",")[0] + " -" + artists[1].replace("(Explicit)", "")), 0)
					else:
						ReNam3(os.path.join(x[0], y), os.path.join(x[0].replace("Tracks/", "Tracks/Done/"), y.replace("(Explicit)", "")), 0)

		#inA5S(LocationS + "/Playlists/")

		for x in os.walk(LocationS + "/Playlists/"):
			if (not "Done" in x[0]):
				for y in x[1]:
					for w in os.walk(os.path.join(x[0], y)):
						if ("Done" != y):
							for z in w[2]:
								artists = z.split(" -")
								if "," in artists[0]:
									os.rename(os.path.join(w[0], z), os.path.join(w[0], artists[0].split(",")[0] + " -" + artists[1].replace("(Explicit)", "")))
								elif ("(Explicit)" in z):
									os.rename(os.path.join(w[0], z), os.path.join(w[0], z.replace("(Explicit)", ""))) 
							#ReNam3(os.path.join(x[0], y), os.path.join(x[0].replace("Playlists/", "Playlists/Done/"), y.rstrip())) ##### Fixxx 0 na koncu, 4 argumenti

def ReNam3(Path, Location, run):
	try:
		if run == 0:
			if "." in Location: 
				os.rename(Path, Location)
			else: 
				os.rename(Path, Location)

		else:
			Loca7ionS = Location.rpartition(".")

			if not "." in Location:
				os.rename(Path, Location + " " + str(run))
			else: os.rename(Path, Loca7ionS[0] + " " + str(run) + Loca7ionS[1] + Loca7ionS[2])
	except:
		ReNam3(Path, Location, run + 1)


m0De()

if (EdiT != 1 and MaN != 1):
	if len(sys.argv) == 2:
		if sys.argv[1] != "2":
			FrR()

			Fr()

			DowNloaD()
	else:
		FrR()

		Fr()

		DowNloaD()