#!/usr/bin/make -f

all: #no code to build

install:
	mkdir -p $(DESTDIR)/usr/share/cvmfs-setup-autofs 
	install -D -m 0644 cvmfs.autofs $(DESTDIR)/usr/share/cvmfs-setup-autofs 
