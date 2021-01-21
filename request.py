#!/usr/bin/env python
from bs4 import BeautifulSoup as soup
import string, random, re, urllib.request, requests

#! ==
#! Backend for commands at main file.
#// install "Better Comments" extension to have color coded commments
#// for clearer code understanding.
#! ==

#?       ___          _                                                       
#?      / / |__   ___| |_ __    _ __ ___  ___ _ __   ___  _ __  ___  ___  ___ 
#?     / /| '_ \ / _ \ | '_ \  | '__/ _ \/ __| '_ \ / _ \| '_ \/ __|/ _ \/ __|
#?    / / | | | |  __/ | |_) | | | |  __/\__ \ |_) | (_) | | | \__ \  __/\__ \
#?   /_/  |_| |_|\___|_| .__/  |_|  \___||___/ .__/ \___/|_| |_|___/\___||___/
#?                     |_|                   |_|                              

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

#! ==
                                       
#?   __                  _   _                 
#?  / _|_   _ _ __   ___| |_(_) ___  _ __  ___ 
#? | |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#? |  _| |_| | | | | (__| |_| | (_) | | | \__ \
#? |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#?                                             

#! replaces space and other special characters from string with given character
def char_manage(text, new_char):
    modified = re.sub(r'\W+', new_char, text)
    modified = modified.replace(" ", "")
    return modified


#! searches query over youtube and get result link
def youtube(query):
    query = char_manage('-', query)
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}&persist_gl=1&gl=GB")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return(video_ids[0])


#! gets random motivation message
def motivation():
    #! https://github.com/surhud004/Foodish#readme
    gif_list = [] #todo add gifs here
    return gif_list[random.randint(0, ((len(gif_list))-1))]


#! searches for package name on <https://aur.archlinux.org/>
def aur(package_name):
    package = char_manage(package_name, "-")
    package_link = f"https://aur.archlinux.org/packages/?O=0&SeB=n&K={package}&outdated=&SB=p&SO=d&PP=50&do_Search=Go"
    return_list = [package_link]
    aur_data = urllib.request.urlopen(package_link).read()
    aur_soup = soup(aur_data, 'html.parser')

    #* try to find for package list
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
    #* no package from the given name exists
    except AttributeError:
        return_list.append(0) #// error code

    return return_list


#! returns random advice
def randomadvice():
    advice = requests.get("https://api.adviceslip.com/advice").json()
    return(advice['slip']['advice'])


#! gets covid stats for the given location from <https://github.com/M-Media-Group/Covid-19-API>
def covid(country, state):
    try:
        countryStats = requests.get(f"https://covid-api.mmediagroup.fr/v1/cases?country={country.capitalize()}").json
        stateStats = countryStats[state.capitalize()]
        return [stateStats['confirmed'], stateStats['recovered'], stateStats['deaths']]
    except: #* if given location doesn't exists
        return 0


#! generates random id for confession message
def random_id():
    length = random.randint(10, 15)
    letters_and_digits = string.ascii_letters + string.digits
    random_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return random_str


#! generates random color
def random_color():
    return random.randint(0, 0xffffff)

#! ==
