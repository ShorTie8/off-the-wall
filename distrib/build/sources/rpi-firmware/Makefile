# SmoothWall Build system.
#
# (c) SmoothWall Ltd 2005
#
# This code is distributed under the terms of the GPL v2.
#
# Okie Dokie, For the Raspberry`s, This is how you do it.
# You start off by picking your firmware comment to set kernel version.
# https://github.com/raspberrypi/firmware/commits/master
# The kernel version is imbeded into the non-changleable firmware.
# Because of openswan, we will pick the latest 3.x.y version.
# 4.4.y for libswan, which is in swe3.2-alef
# So out github commit for 3.18.16 is on Jun 17, 2015, hmmm.....
# https://github.com/raspberrypi/firmware/commit/fc6c9896d26e9fb2cca9c024804f13938ee99311
# But rpi3 was released Feb 29, 2016, which is kernel version 4.1.y
# So the latest 4.1.y is on Apr 11, 2016, @popcornmix, kernel: bump to 4.1.21 Apr 6, 2016
# https://github.com/raspberrypi/firmware/commit/a32be142b2c0c84f10bf495fd530570fe3c83c7b
# Which I think will work with openswan, or so I hope so rpi3 will work.
# Can't have a land Before Time .. :/~
# Now we move onto the kernel source
# Goto https://github.com/raspberrypi/linux and pick your branch from firmware 4.1.y
# https://github.com/raspberrypi/linux/tree/rpi-4.1.y and pick the latest commit, I guess
# https://github.com/raspberrypi/linux/commit/ff45bc0e8917c77461b2901e2743e6339bb70413

include ../Makefile.conf
include ../Makefile.versions

PACKAGE = rpi-firmware

ifeq ($(mTUPLE),rpi2)
VERSION = 8b9d7b8c9cf371e1e3341bec3fd83c530e432a33
else ifeq ($(mTUPLE),rpi3)
VERSION = a32be142b2c0c84f10bf495fd530570fe3c83c7b
else
echo "unsupport firmware for Rapberry pi"
exit 76
endif

BASE_URL = https://github.com/raspberrypi/firmware/archive/$(VERSION)/$(PACKAGE)-$(VERSION).tar.gz

INSTALL = yes

install: download
	tar xf $(DOWNLOADS_DIR)/$(PACKAGE)-$(VERSION).tar.gz
	mv firmware-$(VERSION) $(PACKAGE)-$(VERSION)
	mkdir -p $(PKG_ROOT)

	mkdir -vp $(PKG_ROOT)/boot
	#cp -avR $(DIR)/boot/* $(PKG_ROOT)/boot
	install -m 0644 $(DIR)/boot/LICENCE.broadcom $(PKG_ROOT)/boot/LICENCE.broadcom
	install -m 0644 $(DIR)/boot/bootcode.bin $(PKG_ROOT)/boot/bootcode.bin
	install -m 0644 $(DIR)/boot/fixup_cd.dat $(PKG_ROOT)/boot/fixup_cd.dat
	install -m 0644 $(DIR)/boot/fixup.dat $(PKG_ROOT)/boot/fixup.dat
	install -m 0644 $(DIR)/boot/fixup_db.dat $(PKG_ROOT)/boot/fixup_db.dat
	install -m 0644 $(DIR)/boot/fixup_x.dat $(PKG_ROOT)/boot/fixup_x.dat
	install -m 0644 $(DIR)/boot/start_cd.elf $(PKG_ROOT)/boot/start_cd.elf
	install -m 0644 $(DIR)/boot/start_db.elf $(PKG_ROOT)/boot/start_db.elf
	install -m 0644 $(DIR)/boot/start.elf $(PKG_ROOT)/boot/start.elf
	install -m 0644 $(DIR)/boot/start_x.elf $(PKG_ROOT)/boot/start_x.elf


	mkdir -vp $(PKG_ROOT)/opt
	cp -avR $(DIR)/opt/* $(PKG_ROOT)/opt

	#mkdir -vp $(PKG_ROOT)/lib/modules
	#cp -avR $(DIR)/modules/* $(PKG_ROOT)/lib/modules

	install -m 0644 cmdline.txt $(PKG_ROOT)/boot/cmdline.txt
	install -m 0644 config.txt $(PKG_ROOT)/boot/config.txt
	sed -i $(PKG_ROOT)/boot/config.txt -e "s/UNAME/$(KERNEL_VER)/"


include ../Makefile.rules
