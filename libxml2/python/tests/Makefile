# Makefile.in generated automatically by automake 1.4-p6 from Makefile.am

# Copyright (C) 1994, 1995-8, 1999, 2001 Free Software Foundation, Inc.
# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.


SHELL = /bin/sh

srcdir = .
top_srcdir = ../..

prefix = /Users/liyanage/cvs/entropy/TestXSLT/build/libxml2-gnustyle
exec_prefix = ${prefix}

bindir = ${exec_prefix}/bin
sbindir = ${exec_prefix}/sbin
libexecdir = ${exec_prefix}/libexec
datadir = ${prefix}/share
sysconfdir = ${prefix}/etc
sharedstatedir = ${prefix}/com
localstatedir = ${prefix}/var
libdir = ${exec_prefix}/lib
infodir = ${prefix}/info
mandir = ${prefix}/man
includedir = ${prefix}/include
oldincludedir = /usr/include

DESTDIR =

pkgdatadir = $(datadir)/libxml2
pkglibdir = $(libdir)/libxml2
pkgincludedir = $(includedir)/libxml2

top_builddir = ../..

ACLOCAL = /Users/liyanage/cvs/entropy/TestXSLT/libxml2/missing aclocal-1.4
AUTOCONF = autoconf
AUTOMAKE = /Users/liyanage/cvs/entropy/TestXSLT/libxml2/missing automake-1.4
AUTOHEADER = autoheader

INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL} $(AM_INSTALL_PROGRAM_FLAGS)
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_SCRIPT = ${INSTALL}
transform = s,x,x,

NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
host_alias = 
host_triplet = powerpc-apple-darwin7.0.0b1
AS = @AS@
C14N_OBJ = c14n.c
CATALOG_OBJ = catalog.o
CC = gcc
CFLAGS = -g -O2 -Wall
CPP = gcc -E
DEBUG_OBJ = debugXML.o
DLLTOOL = @DLLTOOL@
DOCB_OBJ = DOCBparser.o
ECHO = echo
EXEEXT = 
FTP_OBJ = nanoftp.o
HAVE_ISINF = 
HAVE_ISNAN = 
HTML_DIR = $(prefix)/doc
HTML_OBJ = HTMLparser.o HTMLtree.o
HTTP_OBJ = nanohttp.o
ICONV_LIBS = -L/Users/liyanage/cvs/entropy/TestXSLT/build/libiconv-gnustyle/lib -liconv
LIBTOOL = $(SHELL) $(top_builddir)/libtool
LIBXML_MAJOR_VERSION = 2
LIBXML_MICRO_VERSION = 4
LIBXML_MINOR_VERSION = 5
LIBXML_VERSION = 2.5.4
LIBXML_VERSION_INFO = 7:4:5
LIBXML_VERSION_NUMBER = 20504
LN_S = ln -s
MAINT = #
MAKEINFO = makeinfo
MV = /bin/mv
M_LIBS = -lm
OBJDUMP = @OBJDUMP@
OBJEXT = o
PACKAGE = libxml2
PYTHON = 
PYTHON_INCLUDES = 
PYTHON_SITE_PACKAGES = 
PYTHON_SUBDIR = 
PYTHON_VERSION = 
RANLIB = ranlib
RDL_LIBS = 
RELDATE = Thu Aug  7 2003
RM = /bin/rm
STATIC_BINARIES = 
STRIP = strip
TAR = /usr/bin/tar
TEST_REGEXPS = Regexptests Automatatests
TEST_SCHEMAS = Schemastests Relaxtests
TEST_THREADS = 
THREAD_CFLAGS = 
THREAD_LIBS = 
U = 
VERSION = 2.5.4
WITH_C14N = 1
WITH_CATALOG = 1
WITH_DEBUG = 1
WITH_DOCB = 1
WITH_FTP = 1
WITH_HTML = 1
WITH_HTTP = 1
WITH_ICONV = 1
WITH_MEM_DEBUG = 0
WITH_REGEXPS = 1
WITH_SCHEMAS = 1
WITH_THREADS = 0
WITH_TRIO = 0
WITH_XINCLUDE = 1
WITH_XPATH = 1
WITH_XPTR = 1
XINCLUDE_OBJ = xinclude.o
XML_CFLAGS = 
XML_INCLUDEDIR = -I${includedir}/libxml2 -I/Users/liyanage/cvs/entropy/TestXSLT/build/libiconv-gnustyle/include
XML_LIBDIR = -L${libdir}
XML_LIBS = -lxml2 -lz  -L/Users/liyanage/cvs/entropy/TestXSLT/build/libiconv-gnustyle/lib -liconv -lm 
XPATH_OBJ = xpath.o
XPTR_OBJ = xpointer.o
Z_CFLAGS = 
Z_LIBS = -lz

EXAMPLE_DIR = $(datadir)/doc/libxml2-python-$(LIBXML_VERSION)/examples

PYTESTS = \
    build.py	\
    attribs.py	\
    tst.py	\
    tstxpath.py	\
    xpathext.py	\
    push.py	\
    pushSAX.py	\
    pushSAXhtml.py \
    error.py	\
    serialize.py\
    validate.py	\
    tstURI.py	\
    cutnpaste.py\
    xpathret.py	\
    xpath.py	\
    outbuf.py	\
    inbuf.py	\
    resolver.py \
    regexp.py	\
    reader.py	\
    reader2.py	\
    reader3.py	\
    ctxterror.py\
    readererr.py\
    relaxng.py


XMLS = \
    tst.xml	\
    valid.xml	\
    invalid.xml


EXTRA_DIST = $(PYTESTS) $(XMLS)
mkinstalldirs = $(SHELL) $(top_srcdir)/mkinstalldirs
CONFIG_HEADER = ../../config.h
CONFIG_CLEAN_FILES = 
DIST_COMMON =  Makefile.am Makefile.in


DISTFILES = $(DIST_COMMON) $(SOURCES) $(HEADERS) $(TEXINFOS) $(EXTRA_DIST)

GZIP_ENV = --best
all: all-redirect
.SUFFIXES:
$(srcdir)/Makefile.in: # Makefile.am $(top_srcdir)/configure.in $(ACLOCAL_M4) 
	cd $(top_srcdir) && $(AUTOMAKE) --gnu --include-deps python/tests/Makefile

Makefile: $(srcdir)/Makefile.in  $(top_builddir)/config.status
	cd $(top_builddir) \
	  && CONFIG_FILES=$(subdir)/$@ CONFIG_HEADERS= $(SHELL) ./config.status

tags: TAGS
TAGS:


distdir = $(top_builddir)/$(PACKAGE)-$(VERSION)/$(subdir)

subdir = python/tests

distdir: $(DISTFILES)
	@for file in $(DISTFILES); do \
	  d=$(srcdir); \
	  if test -d $$d/$$file; then \
	    cp -pr $$d/$$file $(distdir)/$$file; \
	  else \
	    test -f $(distdir)/$$file \
	    || ln $$d/$$file $(distdir)/$$file 2> /dev/null \
	    || cp -p $$d/$$file $(distdir)/$$file || :; \
	  fi; \
	done
info-am:
info: info-am
dvi-am:
dvi: dvi-am
check-am: all-am
check: check-am
installcheck-am:
installcheck: installcheck-am
install-exec-am:
install-exec: install-exec-am

install-data-am: install-data-local
install-data: install-data-am

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am
install: install-am
uninstall-am:
uninstall: uninstall-am
all-am: Makefile
all-redirect: all-am
install-strip:
	$(MAKE) $(AM_MAKEFLAGS) AM_INSTALL_PROGRAM_FLAGS=-s install
installdirs:


mostlyclean-generic:

clean-generic:

distclean-generic:
	-rm -f Makefile $(CONFIG_CLEAN_FILES)
	-rm -f config.cache config.log stamp-h stamp-h[0-9]*

maintainer-clean-generic:
mostlyclean-am:  mostlyclean-generic

mostlyclean: mostlyclean-am

clean-am:  clean-generic mostlyclean-am

clean: clean-am

distclean-am:  distclean-generic clean-am
	-rm -f libtool

distclean: distclean-am

maintainer-clean-am:  maintainer-clean-generic distclean-am
	@echo "This command is intended for maintainers to use;"
	@echo "it deletes files that may require special tools to rebuild."

maintainer-clean: maintainer-clean-am

.PHONY: tags distdir info-am info dvi-am dvi check check-am \
installcheck-am installcheck install-exec-am install-exec \
install-data-local install-data-am install-data install-am install \
uninstall-am uninstall all-redirect all-am all installdirs \
mostlyclean-generic distclean-generic clean-generic \
maintainer-clean-generic clean mostlyclean distclean maintainer-clean


#tests: $(PYTESTS)
#	-@(PYTHONPATH="..:../.libs:$(srcdir)/.." ; export PYTHONPATH; \
#	   for test in $(PYTESTS) ; do echo "-- $$test" ; $(PYTHON) $(srcdir)/$$test ; done)
tests:

clean:
	rm -f *.pyc core

install-data-local:
	$(mkinstalldirs) $(DESTDIR)$(EXAMPLE_DIR)
	-(for test in $(PYTESTS) $(XMLS); \
	  do /usr/bin/install -c -m 0644 $$test $(DESTDIR)$(EXAMPLE_DIR) ; done)

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
