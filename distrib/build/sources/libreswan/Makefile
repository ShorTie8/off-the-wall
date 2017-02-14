# SmoothWall Build system.
#
# (c) SmoothWall Ltd 2005
#
# This code is distributed under the terms of the GPL v2.

include ../Makefile
include ../Makefile.conf
include ../Makefile.versions

PACKAGE = $(FREESWAN_TYPE)
VERSION = $(FREESWAN_VER)

BASE_URL = https://download.libreswan.org

TARBALL = $(FREESWAN_TYPE)-$(VERSION)

PATCH_FILE1 = makefile.patch
PATCH_FILE2 = ikev1_xauth.c.patch

KNL_SRC = $(SOURCES_DIR)/linux$(KERNEL_TYPE)/linux
MOD_DEST = /lib/modules/$(K_RAW_VERSION)$(KERNEL_TYPE)/kernel/net/ipsec

unpack: $(DIR)/
	@true

CONFIGURE = yes
COMPILE = yes
INSTALL = yes

configure: patch
	cp makefile.inc.local $(DIR)/Makefile.inc.local

CFLAGS:=$(CFLAGS) -fno-strict-aliasing
compile: configure
	$(MAKE) $(JOBS) -C $(COMPILE_DIR) V=1 KERNELSRC=$(KNL_SRC) WERROR_CFLAGS="" base
	$(MAKE) $(JOBS) -C $(COMPILE_DIR) V=1 KERNELSRC=$(KNL_SRC) WERROR_CFLAGS="" module

install: compile
	mkdir -p $(PKG_ROOT)${PKG_DIR}
	tput smso;echo "INSTALL";tput rmso;sleep 1
	$(MAKE) -C $(COMPILE_DIR) DESTDIR=$(PKG_ROOT) KERNELSRC=$(KNL_SRC) install-base
	$(MAKE) -C $(COMPILE_DIR) DESTDIR=$(PKG_ROOT) KERNELSRC=$(KNL_SRC) minstall
	rm -rf $(PKG_ROOT)$(PKG_DIR)/rc* $(PKG_ROOT)$(PKG_DIR)/etc/ipsec.conf $(PKG_ROOT)/var

include ../Makefile.rules
