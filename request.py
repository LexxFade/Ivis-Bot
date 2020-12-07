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
- __Aliases__: `/listen {message}` | `/confession {message}`

**/youtube {query}**
- Search for YouTube videos right from discord!
- __Aliases__: `/yt {query}` | `/vid {query}`

**/motivate**
- Feeling low? try this command to get motivation :heart:
- __Alias__: `/motivation`

**/aur {package}**
- Find packages on AUR with its `git-clone`
- __Aliases__: `/arch {package}` | `/git-clone {package}`

**/ping**
- Pretty self-explanatory command, I guess?

**/help**
- Get this help menu
- __Aliases__: `/about` | `/info`'''

def char_manage(text, new_char):
    return sub(r'\W+', new_char, text)

def youtube(query):
    query = char_manage(query, "%20")
    ddg_link = r"https://duckduckgo.com/html?q=" + "\"youtube.com/watch?v=\"%20" + query
    ddg_data = uReq(ddg_link).read()
    ddg_soup = soup(ddg_data, 'html.parser')

    youtube_link = str(ddg_soup.findAll('a', {'class':'result__url'}, limit=1))
    start_index = youtube_link.find("www.youtube.com/watch?v=")
    return (youtube_link[start_index:-24])

def motivation():
    gif_list = [] #todo add gifs here
    return gif_list[random.randint(0, ((len(gif_list))-1))]

def aur(package_name):
    package = char_manage(package_name, "-")
    package_link = f"https://aur.archlinux.org/packages/?O=0&SeB=n&K={package}&outdated=&SB=p&SO=d&PP=50&do_Search=Go"
    return_list = [package_link]
    aur_data = uReq(package_link).read()
    aur_soup = soup(aur_data, 'html.parser')

    try:
        index = 1
        for title in aur_soup.find("tbody").findAll("a"):
            index += 1
            if (index % 2 == 0) and (index < 12):
                return_list.append([title.text, "", -1])
        
        out_index = 0
        in_index = 0
        for other_details in aur_soup.tbody.find_all('td'):
            out_index += 1
            if (out_index + 1) % 6 == 0:
                return_list[(in_index) + 1][2] = other_details.text
                in_index += 1

            elif ((out_index + 1) % 3 == 0):
                return_list[(in_index) + 1][1] = other_details.text
            
            if return_list[-1][2] != -1:
                break
                
    except AttributeError:
        return_list.append(0)

    return return_list

def channel_id():
    pass

def random_id():
    length = random.randint(10, 15)
    letters_and_digits = string.ascii_letters + string.digits
    random_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return random_str

def random_color():
    return random.randint(0, 0xffffff)
