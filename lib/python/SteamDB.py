from urllib.request import urlopen
import html
import json
import os

def safefilename(rawname):
    """ Convenience method to create a file-system-safe version of a name.
    Useful for naming files based on game names.
    """
    return rawname.translate(str.maketrans('', '', '"\\/:\''))

class SteamDB:
    """ Class for storing a database of steam applications from a given
    profile.
    
    Public member
    db - a dictionary of steam applications in the profile. This is keyed
         by application ID. Each entry will contain the following fields
         per the current Steam site design:
         appid          - The application ID (integer)
         name           - The application name
         logo           - A URL to the application logo
         availStatLinks - A sub-dictionary of game statistics
         Other fields can be found for some games such as friendly_name,
         friendlyURL, hours, hours_forever, and last_played, but their
         presense is based on whether the applicable data is available
         for the game.
         If in doubt, refer to the Steam Profile page in a 'view source'
         format, or use the Python debugger to inspect extracted data.
    """
    def __init__(self, profileid_or_path):
        """ Initializes the Steam database information based on the provided
        profileid (or name), or a downloaded HTML profile games page
        """
        # Extract the Javascript game data table from the profile website. Interpret as JSON to load.
        if os.path.exists(profileid_or_path):
            with open(profileid_or_path, 'r') as profilefile:
                profile = profilefile.read()
        else:
            if str.isnumeric(profileid_or_path):
                url = "http://steamcommunity.com/profiles/{}/games?tab=all".format(profileid_or_path)
            else:
                url = "http://steamcommunity.com/id/{}/games?tab=all".format(profileid_or_path)
            with urlopen(url) as stream:
                profile = stream.read().decode('utf-8')
            
        if 'This profile is private' in profile:
            raise Exception('Cannot parse private profile.')
        dbtext = profile.partition('data-profile-gameslist="')[2].partition('"></template>')[0]
        dbtext = html.unescape(dbtext)
        rawdb = json.loads(dbtext)
        
        # Debug code. Uncomment (and add early Try statement) to get a saved
        # HTML file of the profile page upon error.
        #~ except Exception:
            #~ print('Writing debug.html file.')
            #~ with open('debug.html', 'w') as debugfile:
                #~ debugfile.write(profile)
            #~ raise
        
        # Convert the directly loaded database into a dictionary, keyed by app id.
        self.db = dict()
        for app in rawdb['rgGames']:
            self.db[app['appid']] = app
