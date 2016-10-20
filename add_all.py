import os

projects = os.listdir(".")

files_to_add = ["fcstd", "rld"]

for project in projects:
    if project.find(".") < 0:
        print "add " + project
        files = os.listdir(project)
        print files
        for file in files:
            splitfile = file.split(".")
            if len(splitfile) > 0 and splitfile[1] in files_to_add:
                print "add " + file
                os.system("git add " + project + "/" + file)

