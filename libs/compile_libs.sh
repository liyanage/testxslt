#!/bin/sh

echo executing $0
echo ACTION is $ACTION


LIBS_TAR_DIR="`pwd`/libs"
LIBS_DEST_DIR="$BUILD_DIR/libs"
LIBS_INST_DIR="$LIBS_DEST_DIR/inst"
LIBS_SRC_DIR="$LIBS_DEST_DIR/src"

TAR_LIBXML2="$LIBS_TAR_DIR/libxml2-2.6.17.tar.gz"
TAR_LIBXSLT="$LIBS_TAR_DIR/libxslt-1.1.12.tar.gz"
TAR_EXPAT="$LIBS_TAR_DIR/expat-2005-01-28.tar.gz"
TAR_SABLOT="$LIBS_TAR_DIR/Sablot-1.0.2.tar.gz"

echo $LIBS_TAR_DIR / $LIBS_DEST_DIR / $LIBS_INST_DIR / $LIBS_BUILD_DIR

[ -e "$LIBS_TAR_DIR" ]  || exit 1
[ -e "$LIBS_DEST_DIR" ] || mkdir -p "$LIBS_DEST_DIR"  || exit 1
[ -e "$LIBS_INST_DIR" ] || mkdir -p "$LIBS_INST_DIR"  || exit 1
[ -e "$LIBS_SRC_DIR" ]  || mkdir -p "$LIBS_SRC_DIR"   || exit 1




#### setup libxml2
LIB="$LIBS_DEST_DIR/libxml2.dylib"
if [ ! -e "$LIB" ]; then

	echo building "$LIB"

	cd "$LIBS_SRC_DIR"
	tar -xzf "$TAR_LIBXML2"
	cd libxml2-*
	./configure --prefix="$LIBS_INST_DIR"
	make install

	cp "$LIBS_INST_DIR/lib/libxml2.dylib" "$LIB"
	perl "$LIBS_TAR_DIR/fix_install_paths.pl" "$LIB" "$BUILD_DIR"

fi


#### setup libxslt
LIB="$LIBS_DEST_DIR/libxslt.dylib"
if [ ! -e "$LIB" ]; then

	echo building "$LIB"

	cd "$LIBS_SRC_DIR"
	tar -xzf "$TAR_LIBXSLT"
	cd libxslt-*
	./configure --prefix="$LIBS_INST_DIR" --with-libxml-prefix="$LIBS_INST_DIR"
	make install

	cp "$LIBS_INST_DIR/lib/libxslt.dylib" "$LIB"
	perl "$LIBS_TAR_DIR/fix_install_paths.pl" "$LIB" "$BUILD_DIR"

	cp "$LIBS_INST_DIR/lib/libexslt.dylib" "$LIBS_DEST_DIR/libexslt.dylib"
	perl "$LIBS_TAR_DIR/fix_install_paths.pl" "$LIBS_DEST_DIR/libexslt.dylib" "$BUILD_DIR"

fi


#### setup libexpat
LIB="$LIBS_DEST_DIR/libexpat.dylib"
if [ ! -e "$LIB" ]; then

	echo building "$LIB"

	cd "$LIBS_SRC_DIR"
	tar -xzf "$TAR_EXPAT"
	cd expat-*
	./configure --prefix="$LIBS_INST_DIR"
	INSTALL_ROOT="/" make -e install

	cp "$LIBS_INST_DIR/lib/libexpat.dylib" "$LIB"
	perl "$LIBS_TAR_DIR/fix_install_paths.pl" "$LIB" "$BUILD_DIR"

fi


#### setup libSablot
LIB="$LIBS_DEST_DIR/libSablot.dylib"
if [ ! -e "$LIB" ]; then

	echo building "$LIB"

	cd "$LIBS_SRC_DIR"
	tar -xzf "$TAR_SABLOT"
	cd Sablot-*

	./configure --disable-adding-meta --with-expat="$LIBS_INST_DIR" --prefix="$LIBS_INST_DIR"
	make install

	cp "$LIBS_INST_DIR/lib/libSablot.dylib" "$LIB"
	perl "$LIBS_TAR_DIR/fix_install_paths.pl" "$LIB" "$BUILD_DIR"

fi


exit

SUBDIR=libxml2
GNUSTYLEPREFIX=$TARGET_BUILD_DIR/libxml2-gnustyle
ICONVPREFIX=$TARGET_BUILD_DIR/libiconv-gnustyle

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

		./configure --prefix=$GNUSTYLEPREFIX --without-python --with-iconv=$ICONVPREFIX

	fi

	
	if [ ! -d $GNUSTYLEPREFIX ]; then

		make install

	fi


fi




