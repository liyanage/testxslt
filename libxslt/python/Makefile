# Makefile.in generated automatically by automake 1.4-p6 from Makefile.am

# Copyright (C) 1994, 1995-8, 1999, 2001 Free Software Foundation, Inc.
# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.

# Makefile for libxml2 python library


SHELL = /bin/sh

srcdir = .
top_srcdir = ..

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

top_builddir = ..

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

AUTOMAKE_OPTIONS = 1.4 foreign

SUBDIRS = . tests

INCLUDES = \
	-I$(PYTHON_INCLUDES) \
	 $(LIBXML_CFLAGS) \
	-I$(top_srcdir)


DOCS_DIR = $(datadir)/doc/libxslt-python-$(LIBXSLT_VERSION)
# libxsltclass.txt is generated
DOCS = TODO

EXTRA_DIST = \
	libxslt.c		\
	types.c			\
	generator.py		\
	libxml_wrap.h		\
	libxslt_wrap.h		\
	libxsl.py		\
	libxslt-python-api.xml	\
	$(DOCS)


libxsltmod_la_LDFLAGS = -module -avoid-version -L$(top_builddir)/libxslt/.libs \
                        -L$(top_builddir)/libexslt/.libs


#mylibs = #\
#	$(top_builddir)/libxslt/libxslt.la \
#	$(top_builddir)/libexslt/libexslt.la

#pythondir = #$(libdir)/python${PYTHON_VERSION}/site-packages
#python_LTLIBRARIES = #libxsltmod.la

#libxsltmod_la_SOURCES = #libxslt.c types.c libxslt-py.c
#libxsltmod_la_LIBADD = #$(mylibs) 

#GENERATE = #generator.py
#API_DESC = #$(top_srcdir)/doc/libxslt-api.xml $(srcdir)/libxslt-python-api.xml
#GENERATED = #$(srcdir)/libxsltclass.py \
#           $(srcdir)/libxslt-export.c \
#	   $(srcdir)/libxslt-py.c \
#	   $(srcdir)/libxslt-py.h
mkinstalldirs = $(SHELL) $(top_srcdir)/mkinstalldirs
CONFIG_HEADER = ../config.h
CONFIG_CLEAN_FILES = 
LTLIBRARIES =  $(python_LTLIBRARIES)


DEFS = -DHAVE_CONFIG_H -I. -I$(srcdir) -I..
LIBS = 
#libxsltmod_la_DEPENDENCIES =  \
#$(top_builddir)/libxslt/libxslt.la \
#$(top_builddir)/libexslt/libexslt.la
#libxsltmod_la_OBJECTS =  libxslt.lo types.lo \
#libxslt-py.lo
COMPILE = $(CC) $(DEFS) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS)
LTCOMPILE = $(LIBTOOL) --mode=compile $(CC) $(DEFS) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS)
CCLD = $(CC)
LINK = $(LIBTOOL) --mode=link $(CCLD) $(AM_CFLAGS) $(CFLAGS) $(LDFLAGS) -o $@
DIST_COMMON =  Makefile.am Makefile.in TODO


DISTFILES = $(DIST_COMMON) $(SOURCES) $(HEADERS) $(TEXINFOS) $(EXTRA_DIST)

TAR = gtar
GZIP_ENV = --best
SOURCES = $(libxsltmod_la_SOURCES)
OBJECTS = $(libxsltmod_la_OBJECTS)

all: all-redirect
.SUFFIXES:
.SUFFIXES: .S .c .lo .o .obj .s
$(srcdir)/Makefile.in: # Makefile.am $(top_srcdir)/configure.in $(ACLOCAL_M4) 
	cd $(top_srcdir) && $(AUTOMAKE) --foreign --include-deps python/Makefile

Makefile: $(srcdir)/Makefile.in  $(top_builddir)/config.status
	cd $(top_builddir) \
	  && CONFIG_FILES=$(subdir)/$@ CONFIG_HEADERS= $(SHELL) ./config.status


mostlyclean-pythonLTLIBRARIES:

clean-pythonLTLIBRARIES:
	-test -z "$(python_LTLIBRARIES)" || rm -f $(python_LTLIBRARIES)

distclean-pythonLTLIBRARIES:

maintainer-clean-pythonLTLIBRARIES:

install-pythonLTLIBRARIES: $(python_LTLIBRARIES)
	@$(NORMAL_INSTALL)
	$(mkinstalldirs) $(DESTDIR)$(pythondir)
	@list='$(python_LTLIBRARIES)'; for p in $$list; do \
	  if test -f $$p; then \
	    echo "$(LIBTOOL)  --mode=install $(INSTALL) $$p $(DESTDIR)$(pythondir)/$$p"; \
	    $(LIBTOOL)  --mode=install $(INSTALL) $$p $(DESTDIR)$(pythondir)/$$p; \
	  else :; fi; \
	done

uninstall-pythonLTLIBRARIES:
	@$(NORMAL_UNINSTALL)
	list='$(python_LTLIBRARIES)'; for p in $$list; do \
	  $(LIBTOOL)  --mode=uninstall rm -f $(DESTDIR)$(pythondir)/$$p; \
	done

.c.o:
	$(COMPILE) -c $<

# FIXME: We should only use cygpath when building on Windows,
# and only if it is available.
.c.obj:
	$(COMPILE) -c `cygpath -w $<`

.s.o:
	$(COMPILE) -c $<

.S.o:
	$(COMPILE) -c $<

mostlyclean-compile:
	-rm -f *.o core *.core
	-rm -f *.$(OBJEXT)

clean-compile:

distclean-compile:
	-rm -f *.tab.c

maintainer-clean-compile:

.c.lo:
	$(LIBTOOL) --mode=compile $(COMPILE) -c $<

.s.lo:
	$(LIBTOOL) --mode=compile $(COMPILE) -c $<

.S.lo:
	$(LIBTOOL) --mode=compile $(COMPILE) -c $<

mostlyclean-libtool:
	-rm -f *.lo

clean-libtool:
	-rm -rf .libs _libs

distclean-libtool:

maintainer-clean-libtool:

libxsltmod.la: $(libxsltmod_la_OBJECTS) $(libxsltmod_la_DEPENDENCIES)
	$(LINK) -rpath $(pythondir) $(libxsltmod_la_LDFLAGS) $(libxsltmod_la_OBJECTS) $(libxsltmod_la_LIBADD) $(LIBS)

# This directory's subdirectories are mostly independent; you can cd
# into them and run `make' without going through this Makefile.
# To change the values of `make' variables: instead of editing Makefiles,
# (1) if the variable is set in `config.status', edit `config.status'
#     (which will cause the Makefiles to be regenerated when you run `make');
# (2) otherwise, pass the desired values on the `make' command line.



all-recursive install-data-recursive install-exec-recursive \
installdirs-recursive install-recursive uninstall-recursive  \
check-recursive installcheck-recursive info-recursive dvi-recursive:
	@set fnord $(MAKEFLAGS); amf=$$2; \
	dot_seen=no; \
	target=`echo $@ | sed s/-recursive//`; \
	list='$(SUBDIRS)'; for subdir in $$list; do \
	  echo "Making $$target in $$subdir"; \
	  if test "$$subdir" = "."; then \
	    dot_seen=yes; \
	    local_target="$$target-am"; \
	  else \
	    local_target="$$target"; \
	  fi; \
	  (cd $$subdir && $(MAKE) $(AM_MAKEFLAGS) $$local_target) \
	   || case "$$amf" in *=*) exit 1;; *k*) fail=yes;; *) exit 1;; esac; \
	done; \
	if test "$$dot_seen" = "no"; then \
	  $(MAKE) $(AM_MAKEFLAGS) "$$target-am" || exit 1; \
	fi; test -z "$$fail"

mostlyclean-recursive clean-recursive distclean-recursive \
maintainer-clean-recursive:
	@set fnord $(MAKEFLAGS); amf=$$2; \
	dot_seen=no; \
	rev=''; list='$(SUBDIRS)'; for subdir in $$list; do \
	  rev="$$subdir $$rev"; \
	  test "$$subdir" != "." || dot_seen=yes; \
	done; \
	test "$$dot_seen" = "no" && rev=". $$rev"; \
	target=`echo $@ | sed s/-recursive//`; \
	for subdir in $$rev; do \
	  echo "Making $$target in $$subdir"; \
	  if test "$$subdir" = "."; then \
	    local_target="$$target-am"; \
	  else \
	    local_target="$$target"; \
	  fi; \
	  (cd $$subdir && $(MAKE) $(AM_MAKEFLAGS) $$local_target) \
	   || case "$$amf" in *=*) exit 1;; *k*) fail=yes;; *) exit 1;; esac; \
	done && test -z "$$fail"
tags-recursive:
	list='$(SUBDIRS)'; for subdir in $$list; do \
	  test "$$subdir" = . || (cd $$subdir && $(MAKE) $(AM_MAKEFLAGS) tags); \
	done

tags: TAGS

ID: $(HEADERS) $(SOURCES) $(LISP)
	list='$(SOURCES) $(HEADERS)'; \
	unique=`for i in $$list; do echo $$i; done | \
	  awk '    { files[$$0] = 1; } \
	       END { for (i in files) print i; }'`; \
	here=`pwd` && cd $(srcdir) \
	  && mkid -f$$here/ID $$unique $(LISP)

TAGS: tags-recursive $(HEADERS) $(SOURCES)  $(TAGS_DEPENDENCIES) $(LISP)
	tags=; \
	here=`pwd`; \
	list='$(SUBDIRS)'; for subdir in $$list; do \
   if test "$$subdir" = .; then :; else \
	    test -f $$subdir/TAGS && tags="$$tags -i $$here/$$subdir/TAGS"; \
   fi; \
	done; \
	list='$(SOURCES) $(HEADERS)'; \
	unique=`for i in $$list; do echo $$i; done | \
	  awk '    { files[$$0] = 1; } \
	       END { for (i in files) print i; }'`; \
	test -z "$(ETAGS_ARGS)$$unique$(LISP)$$tags" \
	  || (cd $(srcdir) && etags $(ETAGS_ARGS) $$tags  $$unique $(LISP) -o $$here/TAGS)

mostlyclean-tags:

clean-tags:

distclean-tags:
	-rm -f TAGS ID

maintainer-clean-tags:

distdir = $(top_builddir)/$(PACKAGE)-$(VERSION)/$(subdir)

subdir = python

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
	for subdir in $(SUBDIRS); do \
	  if test "$$subdir" = .; then :; else \
	    test -d $(distdir)/$$subdir \
	    || mkdir $(distdir)/$$subdir \
	    || exit 1; \
	    chmod 777 $(distdir)/$$subdir; \
	    (cd $$subdir && $(MAKE) $(AM_MAKEFLAGS) top_distdir=../$(top_distdir) distdir=../$(distdir)/$$subdir distdir) \
	      || exit 1; \
	  fi; \
	done
libxslt-py.lo libxslt-py.o : libxslt-py.c ../libxslt/xsltconfig.h \
	libxslt_wrap.h libxml_wrap.h ../libxslt/xslt.h \
	../libxslt/xsltInternals.h ../libxslt/numbersInternals.h \
	../libxslt/xsltutils.h ../libxslt/attributes.h \
	../libxslt/documents.h ../libxslt/extensions.h \
	../libxslt/extra.h ../libxslt/functions.h ../libxslt/imports.h \
	../libxslt/keys.h ../libxslt/namespaces.h ../libxslt/pattern.h \
	../libxslt/preproc.h ../libxslt/templates.h \
	../libxslt/transform.h ../libxslt/variables.h libxslt-py.h
libxslt.lo libxslt.o : libxslt.c libxslt_wrap.h libxml_wrap.h \
	../libxslt/xslt.h ../libxslt/xsltInternals.h \
	../libxslt/numbersInternals.h ../libxslt/xsltutils.h \
	../libxslt/xsltconfig.h ../libxslt/attributes.h \
	../libxslt/documents.h ../libxslt/extensions.h \
	../libxslt/extra.h ../libxslt/functions.h ../libxslt/imports.h \
	../libxslt/keys.h ../libxslt/namespaces.h ../libxslt/pattern.h \
	../libxslt/preproc.h ../libxslt/templates.h \
	../libxslt/transform.h ../libxslt/variables.h libxslt-py.h \
	libxslt-export.c
types.lo types.o : types.c libxml_wrap.h

info-am:
info: info-recursive
dvi-am:
dvi: dvi-recursive
check-am: all-am
check: check-recursive
installcheck-am:
installcheck: installcheck-recursive
install-exec-am:
install-exec: install-exec-recursive

install-data-am: install-pythonLTLIBRARIES install-data-local
install-data: install-data-recursive

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am
install: install-recursive
uninstall-am: uninstall-pythonLTLIBRARIES
uninstall: uninstall-recursive
all-am: Makefile $(LTLIBRARIES) all-local
all-redirect: all-recursive
install-strip:
	$(MAKE) $(AM_MAKEFLAGS) AM_INSTALL_PROGRAM_FLAGS=-s install
installdirs: installdirs-recursive
installdirs-am:
	$(mkinstalldirs)  $(DESTDIR)$(pythondir)


mostlyclean-generic:

clean-generic:

distclean-generic:
	-rm -f Makefile $(CONFIG_CLEAN_FILES)
	-rm -f config.cache config.log stamp-h stamp-h[0-9]*

maintainer-clean-generic:
mostlyclean-am:  mostlyclean-pythonLTLIBRARIES mostlyclean-compile \
		mostlyclean-libtool mostlyclean-tags \
		mostlyclean-generic

mostlyclean: mostlyclean-recursive

clean-am:  clean-pythonLTLIBRARIES clean-compile clean-libtool \
		clean-tags clean-generic mostlyclean-am

clean: clean-recursive

distclean-am:  distclean-pythonLTLIBRARIES distclean-compile \
		distclean-libtool distclean-tags distclean-generic \
		clean-am
	-rm -f libtool

distclean: distclean-recursive

maintainer-clean-am:  maintainer-clean-pythonLTLIBRARIES \
		maintainer-clean-compile maintainer-clean-libtool \
		maintainer-clean-tags maintainer-clean-generic \
		distclean-am
	@echo "This command is intended for maintainers to use;"
	@echo "it deletes files that may require special tools to rebuild."

maintainer-clean: maintainer-clean-recursive

.PHONY: mostlyclean-pythonLTLIBRARIES distclean-pythonLTLIBRARIES \
clean-pythonLTLIBRARIES maintainer-clean-pythonLTLIBRARIES \
uninstall-pythonLTLIBRARIES install-pythonLTLIBRARIES \
mostlyclean-compile distclean-compile clean-compile \
maintainer-clean-compile mostlyclean-libtool distclean-libtool \
clean-libtool maintainer-clean-libtool install-data-recursive \
uninstall-data-recursive install-exec-recursive \
uninstall-exec-recursive installdirs-recursive uninstalldirs-recursive \
all-recursive check-recursive installcheck-recursive info-recursive \
dvi-recursive mostlyclean-recursive distclean-recursive clean-recursive \
maintainer-clean-recursive tags tags-recursive mostlyclean-tags \
distclean-tags clean-tags maintainer-clean-tags distdir info-am info \
dvi-am dvi check check-am installcheck-am installcheck install-exec-am \
install-exec install-data-local install-data-am install-data install-am \
install uninstall-am uninstall all-local all-redirect all-am all \
installdirs-am installdirs mostlyclean-generic distclean-generic \
clean-generic maintainer-clean-generic clean mostlyclean distclean \
maintainer-clean


#all-local: libxslt.py

#libxslt.py: $(srcdir)/libxsl.py $(srcdir)/libxsltclass.py
#	cat $(srcdir)/libxsl.py $(srcdir)/libxsltclass.py > libxslt.py

#install-data-local:
#	$(mkinstalldirs) $(DESTDIR)$(libdir)/python${PYTHON_VERSION}/site-packages
#	/usr/bin/install -c -m 0644 libxslt.py $(DESTDIR)$(libdir)/python${PYTHON_VERSION}/site-packages
#	$(mkinstalldirs) $(DESTDIR)$(DOCS_DIR)
#	@(for doc in $(DOCS) ; \
#	   do /usr/bin/install -c -m 0644 $$doc $(DESTDIR)$(DOCS_DIR) ; done)

#$(GENERATED): gen_prog

#gen_prog:  $(srcdir)/$(GENERATE) $(API_DESC)
#	cd $(srcdir) && $(PYTHON) $(GENERATE)
#	touch gen_prog

#$(libxsltmod_la_OBJECTS): $(GENERATED)

all: 
tests test: all
	cd tests && $(MAKE) tests

clean:
	rm -f $(GENERATED) *.o libxslt.so *.pyc libxslt.py gen_prog

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
