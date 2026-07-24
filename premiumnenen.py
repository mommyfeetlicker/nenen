#!/usr/bin/env python3

import time
import random

tcooldown = random.uniform(0.9,1.9)

def textp(stringt):
	print(stringt)
	time.sleep(tcooldown)

def osom():
	choice = input("ok pilih batu ke air ke burung: ").lower()
	if choice == "batu":
		print("aku pilih air noob")
	elif choice == "air":
		print("HAHAHA noob aku pilih bebet")
	elif choice == "burung":
		print("bodonye bebird aku  pilih batu")
	else:
		print("woi bodo pilih antara 3 je tapi kau kalah gak sbb aku pilih bom nuklear")	

name=input("hai wak apakah nama anda: ").lower()
print("")
if name == "omar":
	print("omar nga tol")
	time.sleep(tcooldown)
	print("goodbye nga")
else:
	print("hai" ,name, "kys")
	time.sleep(tcooldown)
	textp("i sory")
	textp("osom jom")
	print("")
	osom()
	time.sleep(tcooldown)
	textp("nk main lagi tak")
	nkmainlagitakoption = ""
	while nkmainlagitakoption not in ["nak", "tanak"]:
		nkmainlagitakoption=input("osom round 2 balik jom nak ke tanak: ").lower()
	if nkmainlagitakoption == "nak":
		osom()
	textp("dh la aku retired")
	textp("dh la lagi malas aku tulis lagi")
	print(name,"coli")
