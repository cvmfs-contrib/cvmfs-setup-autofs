#!/usr/bin/make -f

# This make file takes care of installing files

all: # nothing to build

# default install target is debian because that's the easist way to
#   set up the 'rules' file.
install:
	mkdir -p $(DESTDIR)/etc/auto.master.d
	install -D -m 0644 cvmfs.autofs $(DESTDIR)/etc/auto.master.d
