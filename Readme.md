# Steam Image Scripts

Somewhat outdated scripts that attempt to download images from Steam using
your profile information. Unfortunately, Steam profile privacy makes this somewhat
impractical.

Maybe I can update these later to work with a manually downloaded page?

Overall dependencies to install these tools:

* `help2man` to generate manual pages
* a Python interpreter that can be run with `python3`

To install to `/usr/local`, simply run `install.sh` (likely with sudo).
This will also generate the manual pages.

To uninstall later, run `uninstall.sh`.

Run either with the `PREFIX` variable set to a value to install to an alternate
location. Example:

```shell
# PREFIX=/usr ./install.sh
```

or

```shell
$ PREFIX=/home/youruser/.local ./install.sh
```

**NOTE**: Python libraries attempt to detect a suitable Python include path
using the `getpypath.py` helper script. At present they will only install
into `/usr/local` (specifically *purelib*) or your home folder (*USER_SITE*).

Refer to manpages for details on any individual tool.
