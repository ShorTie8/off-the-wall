# SmoothWall Build system.
#
# (c) SmoothWall Ltd 2005
#
# This code is distributed under the terms of the GPL v2.

include ../Makefile.conf

PACKAGE = eciadsl-usermode
VERSION = 0.12

BASE_URL = http://eciadsl.flashtux.org/download/

ifeq ($(mARCH),$(mTUPLE))
PATCH_FILE1 = pusb-linux.c.patch
else
PATCH_FILE1 = pusb-linux.c-2.patch
endif

include ../Makefile.rules
