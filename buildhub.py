import os, shutil

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            # print("copying", s, d)
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

try:
	shutil.rmtree("export")
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
	shutil.rmtree("../uiwow7.github.io/sets")
except:
	print("Couldn't remove from sets from uiwow7.github.io")

try:
	copytree("export", "../uiwow7.github.io/sets")
except:
	print("Couldn't move from export > uiwow7.github.io")

os.mkdir("../uiwow7.github.io/sets/versions")
os.mkdir("../uiwow7.github.io/sets/versions/changelogs")

os.chdir("../uiwow7.github.io")

os.system("python scripts/build_site.py")