#!/bin/sh

cd libxslt

if [ x$1 = 'xclean' ]; then

	make clean
	rm config.log
	rm -rf $OBJROOT/libxslt/
	exit

fi

if [ ! -f config.log ]; then

	./configure --disable-static --enable-shared --with-libxml-prefix=$OBJROOT/libxml2/ --prefix=$OBJROOT/libxslt/

fi

if [ ! -d $OBJROOT/libxslt/ ]; then

	make install

	LIBNAME=`find $OBJROOT/libxslt/lib/ -name "libxslt.*dylib" -type f`
	LIBNAME=`basename $LIBNAME`
	install_name_tool -id @executable_path/$LIBNAME $OBJROOT/libxslt/lib/$LIBNAME

	LIBNAME=`find $OBJROOT/libxslt/lib/ -name "libexslt.*dylib" -type f`
	LIBNAME=`basename $LIBNAME`
	install_name_tool -id @executable_path/$LIBNAME $OBJROOT/libxslt/lib/$LIBNAME

	LIBNAME=`find $OBJROOT/libxslt/lib/ -name "libxsltbreakpoint.*dylib" -type f`
	LIBNAME=`basename $LIBNAME`
	install_name_tool -id @executable_path/$LIBNAME $OBJROOT/libxslt/lib/$LIBNAME
	
fi








