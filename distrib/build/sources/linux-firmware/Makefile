# SmoothWall Build system.
#
# (c) SmoothWall Ltd 2005
#
# This code is distributed under the terms of the GPL v2.

include ../Makefile.conf

PACKAGE = linux-firmware
VERSION = 20170228

EXTENSION = .tar.gz

export pkgName = $(PACKAGE)
export gitURL = git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
export gitCommitID = 5abb924a730b5ecca489dfc2ebbdfc90af6ec62d
export gitBranch = $(VERSION)

PREPARE = yes
$(DIR)/:
	true

COMPILE = yes
compile:
	true

INSTALL = yes
install: download
	rm -rf $(PKG_ROOT)
	mkdir -p $(PKG_ROOT)/lib/firmware
	tar xvf $(DOWNLOADS_DIR)/$(TARBALL)$(EXTENSION)
	cd $(PACKAGE)-$(VERSION); cp -avr . $(PKG_ROOT)/lib/firmware
	chown -R root:root $(PKG_ROOT)/lib/firmware/*
	find $(PKG_ROOT)/lib/firmware -type f -exec chmod 444 {} \;
	find $(PKG_ROOT)/lib/firmware -type d -exec chmod 555 {} \;

include ../Makefile.rules
