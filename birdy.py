#!/usr/bin/python 

import tweepy
import json
import process

jsonPath = "./tokens.json"      #Location of json file with tokens/keys

def readtoken(type_name, attribute_name):
    """
    Gets and returns the designated value in json file
    :param type_name: Consumer or Access type
    :param attribute_name: Key or secret value
    :return: string to corresponding type and attribute (e.e., consumer_key)
    """
    #with open(jsonPath, 'r') as jsonFile:
    #    tokenData = json.load(jsonFile)
    #return tokenData[type_name][attribute_name]

def main():
    # Reads the keys and secrets from json file
    #consumer_key = readtoken("consumer", "key")
    #consumer_secret = readtoken("consumer", "secret")
    #access_token = readtoken("access", "key")
    #access_token_secret = readtoken("access", "secret")

    # Constructs OAuthentication
    #auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret, callback=None)
    #auth.set_access_token(access_token, access_token_secret)

    process.process.convert()

    #api = tweepy.API(auth)

    #print(api.get_user(167457765))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nDone!')
