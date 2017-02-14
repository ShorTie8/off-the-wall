# SmoothWall Build system.
#
# (c) SmoothWall Ltd 2005
#
# This code is distributed under the terms of the GPL v2.

include ../Makefile.conf

PACKAGE = qemu
VERSION = 2.7.0

BASE_URL = http://wiki.qemu-project.org/download
EXTENSION = .tar.bz2

# Verbose build
export V=1

ifeq ($(mTUPLE),$(filter $(mTUPLE),rpi2 rpi3 ODROID-XU3))
CONFIG_OPTS =
else
CONFIG_OPTS = --target-list=i386-softmmu
endif

include ../Makefile.rules

