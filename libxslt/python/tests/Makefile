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

prefix = 
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

pkgdatadir = $(datadir)/libxslt
pkglibdir = $(libdir)/libxslt
pkgincludedir = $(includedir)/libxslt

top_builddir = ../..

ACLOCAL = /Users/liyanage/cvs/entropy/TestXSLT/libxslt/missing aclocal-1.4
AUTOCONF = autoconf
AUTOMAKE = /Users/liyanage/cvs/entropy/TestXSLT/libxslt/missing automake-1.4
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
host_triplet = powerpc-apple-darwin7.8.0
AS = @AS@
CC = gcc
CFLAGS = -g -O2 -Wall
CPPFLAGS = 
DLLTOOL = @DLLTOOL@
ECHO = echo
EXEEXT = 
EXTRA_LIBS =  -L/Users/liyanage/cvs/entropy/TestXSLT/build/libxml2-gnustyle/lib -lxml2 -lz -lpthread -L/Users/liyanage/cvs/entropy/TestXSLT/build/libiconv-gnustyle/lib -liconv -lm 
HTML_DIR = $(prefix)/doc
INSTALLED_XSLT_LIB = 
LDFLAGS = 
LIBEXSLT_MAJOR_VERSION = 0
LIBEXSLT_MICRO_VERSION = 18
LIBEXSLT_MINOR_VERSION = 7
LIBEXSLT_VERSION = 0.7.18
LIBEXSLT_VERSION_INFO = 7:18:7
LIBEXSLT_VERSION_NUMBER = 718
LIBTOOL = $(SHELL) $(top_builddir)/libtool
LIBXML_CFLAGS =  -I/Users/liyanage/cvs/entropy/TestXSLT/build/libxml2-gnustyle/include/libxml2 -I/Users/liyanage/cvs/entropy/TestXSLT/build/libiconv-gnustyle/include
LIBXML_LIBS =  -L/Users/liyanage/cvs/entropy/TestXSLT/build/libxml2-gnustyle/lib -lxml2 -lz -lpthread -L/Users/liyanage/cvs/entropy/TestXSLT/build/libiconv-gnustyle/lib -liconv -lm
LIBXML_REQUIRED_VERSION = 2.5.2
LIBXSLTBREAK_MAJOR_VERSION = 1
LIBXSLTBREAK_MICRO_VERSION = 8
LIBXSLTBREAK_MINOR_VERSION = 0
LIBXSLTBREAK_VERSION = 1.0.8
LIBXSLTBREAK_VERSION_INFO = 1:8:0
LIBXSLTBREAK_VERSION_NUMBER = 10008
LIBXSLT_MAJOR_VERSION = 1
LIBXSLT_MICRO_VERSION = 27
LIBXSLT_MINOR_VERSION = 0
LIBXSLT_VERSION = 1.0.27
LIBXSLT_VERSION_INFO = 1:27:0
LIBXSLT_VERSION_NUMBER = 10027
LN_S = ln -s
MAINT = #
MAKEINFO = makeinfo
M_LIBS = 
OBJDUMP = @OBJDUMP@
OBJEXT = o
PACKAGE = libxslt
PERL = perl
PYTHON = 
PYTHONSODV = 
PYTHON_INCLUDES = 
PYTHON_SITE_PACKAGES = 
PYTHON_SUBDIR = 
PYTHON_VERSION = 
RANLIB = ranlib
RELDATE = Sun Feb 20 2005
STRIP = strip
VERSION = 1.0.27
WITH_DEBUGGER = 1
WITH_MEM_DEBUG = 0
WITH_TRIO = 0
WITH_XSLT_DEBUG = 1
XML_CONFIG = /Users/liyanage/cvs/entropy/TestXSLT/build/libxml2-gnustyle/bin/xml2-config
XSLTPROCDV = 
XSLT_INCLUDEDIR = -I${includedir}
XSLT_LIBDIR = -L${libdir}
XSLT_LIBS = -lxslt  -L/Users/liyanage/cvs/entropy/TestXSLT/build/libxml2-gnustyle/lib -lxml2 -lz -lpthread -L/Users/liyanage/cvs/entropy/TestXSLT/build/libiconv-gnustyle/lib -liconv -lm 

EXAMPLE_DIR = $(datadir)/doc/libxslt-python-$(LIBXSLT_VERSION)/examples

TESTSPY = \
    basic.py	\
    exslt.py	\
    extfunc.py


XMLS = \
    test.xml	\
    test.xsl


EXTRAS = \
    pyxsltproc.py


EXTRA_DIST = $(TESTSPY) $(XMLS) $(EXTRAS)
mkinstalldirs = $(SHELL) $(top_srcdir)/mkinstalldirs
CONFIG_HEADER = ../../config.h
CONFIG_CLEAN_FILES = 
DIST_COMMON =  Makefile.am Makefile.in


DISTFILES = $(DIST_COMMON) $(SOURCES) $(HEADERS) $(TEXINFOS) $(EXTRA_DIST)

TAR = gtar
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


#tests: $(TESTSPY)
#	-@(PYTHONPATH="..:../.libs:$(srcdir)/.." ; export PYTHONPATH; \
#	   for test in $(TESTSPY) ; do echo "-- $$test" ; $(PYTHON) $(srcdir)/$$test ; done)
tests:

clean:
	rm -f *.pyc core

install-data-local:
	$(mkinstalldirs) $(DESTDIR)$(EXAMPLE_DIR)
	-(for test in $(TESTSPY) $(XMLS) $(EXTRAS); \
	  do /usr/bin/install -c -m 0644 $$test $(DESTDIR)$(EXAMPLE_DIR) ; done)

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
