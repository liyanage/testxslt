#!/bin/sh

echo executing $0
echo ACTION is $ACTION
echo PWD is `pwd`

SUBDIR=libexpat
GNUSTYLEPREFIX=$TARGET_BUILD_DIR/libexpat-gnustyle

# make sure things match our expectations
#
if [ ! -d $SUBDIR ]; then
	echo no $SUBDIR dir in current dir `pwd`, cannot continue!
	exit 1
fi


if [ x$ACTION = "xclean" ]; then

	echo cleaning up...
	rm -rf $GNUSTYLEPREFIX
	cd $SUBDIR
	make distclean

elif [ x$ACTION = "x" ]; then

	echo building...

	cd $SUBDIR

	if [ ! -f Makefile ]; then

		echo no Makefile, running configure

		./configure --prefix=$GNUSTYLEPREFIX

	fi

	
	if [ ! -d $GNUSTYLEPREFIX ]; then

		make install

	fi


fi




