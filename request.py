#!/usr/bin/env python
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from re import sub
import string, random

about = '''Hey I'm Ivis! :v:
With me you can do more than just texting on discord'''

confessions = '''DM me your confessions and I'll post em anonymously in the confession channel.
Until n unless you leak our chat, no one would ever find out who made what confession ;)'''

commands = '''
**/confess {message}**
- DM me this with your message and I will post your message in the confession channel anonymously.
- __Aliases__: `/listen {message}` `/confession {message}`

**/youtube {query}**
- Search for YouTube videos right from discord!
- __Aliases__: `/yt {query}` `/vid {query}`

**/motivate**
- Feeling low? try this command to get motivation :heart:
- __Alias__: `/motivation`

**/aur {package}**
- Find packages on AUR with its `git-clone`
- __Aliases__: `/arch {package}` `/git-clone {package}`

**/ping**
- Pretty self-explanatory command, I guess?

**/help**
- Get this help menu
- __Aliases__: `/about` `/info`'''

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
    return gif_list[random.randint(0, ((len(gif_list))-1))]

def aur(query):
    pass

def channel_id():
    pass

def random_id():
    length = random.randint(10, 15)
    letters_and_digits = string.ascii_letters + string.digits
    random_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return random_str

def random_color():
    return random.randint(0, 0xffffff)
