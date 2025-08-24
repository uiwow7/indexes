import os, shutil

try:
	os.rmdir("export")
except:
	print("Couldn't remove export")

os.mkdir("export")

print("Exporting sets...")

listed_dir = os.listdir()

for set in listed_dir:
	print(set + "...")
	if set.endswith(".mse-set"):
		set_name = set.split(".mse-set")[0]
		os.system(f'mse --export "magic-egg-allinone-exporter.mse-export-template" "{set}" export/{set_name}.txt')

print("Moving to github repo")

try:
	shutil.copytree("export", "../uiwow7.github.io/sets")
except:
	print("Couldn't move from export > uiwow7.github.io")

os.chdir("../uiwow7.github.io")

os.system("python scripts/build_site.py")