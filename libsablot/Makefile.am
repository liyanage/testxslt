SUBDIRS = src doc utils
EXTRA_DIST = Makefile.nt INSTALL_WIN RELEASE README_JS

dist-hook:
	if test ! -d $(distdir)/autocfg; then mkdir $(distdir)/autocfg; fi
	@cp autocfg/config.h.in $(distdir)/autocfg
	@cp -R tools $(distdir)
