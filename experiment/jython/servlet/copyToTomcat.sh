#!/bin/bash -x 
##!/bin/bash -x # to debug
TOMCAT_APP_PATH=/cygdrive/c/apache/tomcat/apache-tomcat-7.0.56/webapps/servlet
COPY_JYTHON_PACKAGES=/home/mkershaw/python/experiment/jython/servlet/JythonPackages/Lib
JYTHON_LIB=/cygdrive/c/jython2.7.0/Lib
MOD_RPDB=/cygdrive/c/apache/tomcat/apache-tomcat-7.0.56/webapps/servlet/WEB-INF/lib/Lib/site-packages
if [ "$1" == "-lib" ]; then
	echo "Copying Jython Lib as well"
	# Was copying the packages directly from the Jython folders but had problems with this
	#cp -r ${JYTHON_LIB} ${TOMCAT_APP_PATH}/WEB-INF/lib
	cp -r ${COPY_JYTHON_PACKAGES} ${TOMCAT_APP_PATH}/WEB-INF/lib
	chmod -R +rw ${TOMCAT_APP_PATH}/WEB-INF/lib/Lib/*
	cp -r mod_rpdb/rpdb ${MOD_RPDB}
else
	echo "NOT copying jython Lib. Use -lib option to do this"
	rm -f mod_rpdb/rpdb/copy_of_init.py
	cp mod_rpdb/rpdb/__init__.py mod_rpdb/rpdb/copy_of_init.py
	cp -r mod_rpdb/rpdb ${MOD_RPDB}
fi
cp -r WAR/* ${TOMCAT_APP_PATH}
cp servlet1.py ${TOMCAT_APP_PATH}
cp servlet2.py ${TOMCAT_APP_PATH}
cp servlet_rpdb.py ${TOMCAT_APP_PATH}