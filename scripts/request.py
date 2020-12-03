#!/usr/bin/env python
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from re import sub
from random import randint

about = "Hey I'm Ivis! :v:"
confessions = """DM me your confessions and I'll post em anonymously in the confession channel.
Until n unless you show our DM history to anyone else, no one would ever find out who made what confession ;)"""

commands = """
**/help**
- Get this help menu
- __Aliases__: `/about` `/info`

**/youtube {query}**
- Search for YouTube videos right from discord!
- __Aliases__: `/yt {query}` `/vid {query}`

**/motivate**
- Feeling low? try this command to find some motivation :heart:
- __Aliases__: `motivation`

**/aur {package}**
- Gaha Arch Linux is **the** elite OS
- Use this command to find packages on AUR with its `git-clone`
- __Aliases__: `/arch {package}` `/git-clone {package}`

**/ping**
- Pretty self-explanatory command, I guess?"""

def help(requirement):
    if requirement == "about":
        return about
    elif requirement == "confessions":
        return confessions
    elif requirement == "commands":
        return commands

def youtube(query):
    query = sub(r'\W+', '%20', query)
    ddg_link = r"https://duckduckgo.com/html?q=" + "\"youtube.com/watch?v=\"%20" + query
    ddg_data = uReq(ddg_link).read()
    ddg_soup = soup(ddg_data, 'html.parser')

    youtube_link = str(ddg_soup.findAll('a', {'class':'result__url'}, limit=1))
    start_index = youtube_link.find("www.youtube.com/watch?v=")
    return (youtube_link[start_index:-24])

def motivation():
    gif_list = [] #todo add gifs here
    return gif_list[randint(0, (len(gif_list)-1))]

def aur(query):
    pass
