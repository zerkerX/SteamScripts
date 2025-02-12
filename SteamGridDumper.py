#!/usr/bin/python3

import os.path
from urllib.request import urlopen
from urllib.error import HTTPError
from argparse import ArgumentParser

from SteamDB import SteamDB, safefilename

def grabimage(remotepath, localpath):
    if os.path.exists(localpath):
        print('Skipping {}; file already exists.'.format(localpath))
    else:
        with urlopen(remotepath) as stream:
            with open(localpath, 'wb') as outfile:
                outfile.write(stream.read())
        print('Wrote {}.'.format(localpath))
        


def main():
    parser = ArgumentParser(description='Downloads Steam Grid View images.')
    parser.add_argument('-o', dest='outpath',
                       default='Steam Grid View Images',
                       help='Output path. If not specified, will output to '
                        'a subdirectory called "Steam Grid View Images"')
    parser.add_argument('profileid', 
                       help='Steam profile ID. If your Steam profile URL is '
                       '"http://steamcommunity.com/profiles/12345/", then the ID would be '
                       '12345.')

    args = parser.parse_args()
    
    try:
        steam = SteamDB(args.profileid)
        
        if not os.path.exists(args.outpath):
            os.mkdir(args.outpath)
        
        for app in steam.db.values():
            remotepath = "http://cdn.akamai.steamstatic.com/steam/apps/{}/header.jpg".format(
                app['appid'])
            localpath = os.path.join(args.outpath, safefilename(app['name']) + '.jpg')
            try:
                grabimage(remotepath, localpath)
            except HTTPError:
                print('Unable to download header.jpg for {}'.format(app['name']))
    except Exception as problem:
        print('Unable to download images: {}'.format(problem))

if __name__ == '__main__':
    main()
