#!/bin/bash
# #!/bin/bash -x
#cmd /C "jython -J-cp java/build/jar/HelloWorld.jar $1"
if [ "$1" == "" ]; then
   echo "USAGE: run <somepythonfile.py>"
else
	jython -J-cp java/build/jar/HelloWorld.jar $1
fi