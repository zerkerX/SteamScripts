#!/bin/sh
DEST=${PREFIX=/usr/local}

./createman.sh

mkdir -p "$DEST/bin"
mkdir -p "$DEST/share/man/man1"
install -t "$DEST/bin" bin/*
install -t "$DEST/share/man/man1" man/*

PYDEST=$(./getpypath.py $DEST)
if [ $? -eq 0 ]; then
    mkdir -p "$PYDEST"
    install -t "$PYDEST" lib/python/*
else
    B=$(tput bold)
    NB=$(tput sgr0)
    echo "${B}NOTICE${NB}: Unable to find a python library path for specified "
    echo "prefix ${B}$DEST${NB}. Presently only ${B}pure_lib${NB} (usually in /usr/local)"
    echo "and ${B}USER_SITE${NB} (usually in /home/user/.local) are supported."
fi
