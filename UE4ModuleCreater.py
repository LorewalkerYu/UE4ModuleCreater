
import os

# Input your module name here
NewModuleName = "ImageFileHelper"

# Don't touch any thing below if you don't know what's about
outPutDir = "OutPut/"
rootDir = outPutDir + NewModuleName + "/"
publicDir = rootDir + "/Public/"
privateDir = rootDir + "/Private/"
os.makedirs(rootDir)
os.makedirs(publicDir)
os.makedirs(privateDir)
with open("XXXXXXX/XXXXXXX.Build.cs", "r") as BuildFile:
    with open(rootDir + NewModuleName + ".Build.cs","w") as NewBuildFile:
        lines = BuildFile.readlines()
        for each in lines:
            replaced = str(each).replace("XXXXXXX", NewModuleName)
            NewBuildFile.write(replaced)
with open("XXXXXXX/Public/XXXXXXX.h", "r") as HeaderFile:
    with open(publicDir + NewModuleName + ".h","w") as NewHeaderFile:
        lines = HeaderFile.readlines()
        for each in lines:
            replaced = str(each).replace("XXXXXXX", NewModuleName)
            NewHeaderFile.write(replaced)

with open("XXXXXXX/Private/XXXXXXX.cpp", "r") as CppFile:
    with open(privateDir + NewModuleName + ".cpp","w") as NewCppFile:
        lines = CppFile.readlines()
        for each in lines:
            replaced = str(each).replace("XXXXXXX", NewModuleName)
            NewCppFile.write(replaced)

