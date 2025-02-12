#!/usr/bin/python3
"""
Renames Steam screenshots based on the game name and collects into a 
common output path. Must be run from within the Steam screenshot folder
or an external folder containing the "uncompressed copies" of 
the screenshots. Uncompressed screenshots will be renamed in place by
default.
"""
import pdb
import os.path
import shutil
from argparse import ArgumentParser

from SteamDB import SteamDB, safefilename

def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('-o', dest='outpath',
                       default='Steam Screenshots',
                       help='Output path. If not specified, will output from '
                       'the nominal gallery folder to '
                        'a subdirectory called "Steam Screenshots". '
                        'Uncompressed screenshots will be copied to this '
                        'folder if specified; otherwise they will be '
                        'renamed in place.')

    parser.add_argument('profileid', 
                       help='Steam profile ID. If your Steam profile URL is '
                       '"http://steamcommunity.com/profiles/12345/", then the ID would be '
                       '12345.')
                       
    args = parser.parse_args()
    
    steam = SteamDB(args.profileid)
    
    
    if os.path.join('760', 'remote') in os.path.abspath('.'):
        # Script is run within the Steam screenshot folder and is copying
        # jpeg screenshots.
        if not os.path.exists(args.outpath):
            os.makedirs(args.outpath)
        
        for (root, dirs, files) in os.walk('.'):
            if os.path.basename(root) == 'screenshots':
                appid = os.path.basename(os.path.normpath(os.path.join(root, '..')))
                
                try:
                    appname = safefilename(steam.db[int(appid)]['name'])
                except Exception:
                    appname = appid
                    print('Unable to identify app {}. Using app number.'.format(appid))
                for filename in files:
                    shutil.copy2(os.path.join(root, filename),
                        os.path.join(args.outpath, appname + ' ' + filename))
    else:
        # Script is run within an external folder and is renaming png screenshots
        for screenshot in os.listdir('.'):
            (filename, ext) = os.path.splitext(screenshot)
            if ext.lower() == '.png':
                try:
                    (appid, date, number) = filename.split('_')
                    if str.isnumeric(appid) and str.isnumeric(number):
                        appname = safefilename(steam.db[int(appid)]['name'])
                        outname = "{name}_{date}_{number}{ext}".format(
                            name=appname, date=date, number=number, ext=ext)
                        if args.outpath == 'Steam Screenshots':
                            # Custom path was not specified. Rename in place
                            os.rename(screenshot, outname)
                        else:
                            # Custom path specified. Copy to this path
                            shutil.copy2(screenshot,
                                os.path.join(args.outpath, outname))
                        
                    else:
                        raise Exception('Unexpected naming convention.')
                    
                except Exception:
                    print('Unable to identify {}; skipping file.'.format(screenshot))
                

if __name__ == '__main__':
    main()
