#!/bin/sh
INDIR=$(dirname $0)
OUTDIR=$(realpath $INDIR/man)
BINDIR=$(realpath $INDIR/bin)
LIBDIR=$(realpath $INDIR/lib/python)

# Hacky means to satisfy the library dependency temporarily
cp "$LIBDIR/SteamDB.py" "$BINDIR"

mkdir -p $OUTDIR
help2man $BINDIR/steamgriddumper -n "Downloads Steam Grid View images" -m "Steam Image Scripts" -s 1 -N --version-string="1.0" > $OUTDIR/steamgriddumper.1
help2man $BINDIR/steamlibrarydumper -n "Downloads Steam Library images" -m "Steam Image Scripts" -s 1 -N --version-string="1.0" > $OUTDIR/steamlibrarydumper.1
help2man $BINDIR/steamlibraryherodumper -n "Downloads Steam Library Hero images" -m "Steam Image Scripts" -s 1 -N --version-string="1.0" > $OUTDIR/steamlibraryherodumper.1
help2man $BINDIR/steamlogodumper -n "Downloads Steam Logo images" -m "Steam Image Scripts" -s 1 -N --version-string="1.0" > $OUTDIR/steamlogodumper.1
help2man $BINDIR/steamlogotextdumper -n "Downloads Steam Logo images" -m "Steam Image Scripts" -s 1 -N --version-string="1.0" > $OUTDIR/steamlogotextdumper.1
help2man $BINDIR/steamscreenshotrenamer -n "Renames Steam screenshots based on the game name and collects into a common output path" -m "Steam Image Scripts" -s 1 -N --version-string="1.0" > $OUTDIR/steamscreenshotrenamer.1

# Cleanup hack
rm "$BINDIR/SteamDB.py"
