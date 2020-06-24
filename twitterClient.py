#
# COSC2671 Social Media and Network Analytics
# @author Jeffrey Chan, 2019
#

import sys
import tweepy as tw


def twitterAuth():
    """
        Setup Twitter API authentication.
        Replace keys and secrets with your own.

        @returns: tweepy.OAuthHandler object
    """

    try:
        consumerKey = "R9AYvMRr90aEiNcmyo0LTsNwo"
        consumerSecret = "ZScA2zTY7WDHVzwuaHiMwj6TaUKkj9MX30BGzt6ynLXlENFDL6"
        accessToken = "2317262508-Gc9TTR5LWxuKhg8n26bPWgqbA0naim1Knbd5Aa6"
        accessSecret = "RvxoFzWlbAreZsReV5PmbZqplkF2qePoTR7L5LOSI5jwP"
    except KeyError:
        sys.stderr.write("Key or secret token are invalid.\n")
        sys.exit(1)

    auth = tw.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)

    return auth



def twitterClient():
    """
        Setup Twitter API client.

        @returns: tweepy.API object
    """

    auth = twitterAuth()
    client = tw.API(auth,wait_on_rate_limit=True)

    return client
