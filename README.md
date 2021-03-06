## Ivis-bot
*Do more than just text from discord* <br>
A confession bot with a few additions to improve experience over discord.

### General Information
```
- Language:     python3
- Trigger :     /
```
### Confession
Ivis will post confessions DMed to it in the <i>confesstion channel</i> anonymously.<br>
DM syntax: `/confess {message}`
<br><br>
Confession channel is the channel where Ivis will post all confessions. Only **admins** can set/modfy this channel.<br>
command: `/setconfess {channel}`

### Other Commands
- `/help` <br>show help embed with all commands and aliases <br>
![help command](https://raw.githubusercontent.com/LexxFade/Ivis-Bot/main/screenshots/help.png)

- `/youtube {query}` <br>search **query** on YouTube and return vid link <br>
![youtube](https://raw.githubusercontent.com/LexxFade/Ivis-Bot/main/screenshots/yt.png)

- `/aur {package}` <br>search for **package** on Arch User Repository and return **git-clone** links <br>
![arch user repo](https://raw.githubusercontent.com/LexxFade/Ivis-Bot/main/screenshots/aur.png)

- `/covid {country} (state)` <br>get covid stats for the given location. If no **state** if specified then stats for whole country is given. <br>
API used: [ M-Media-Group - Covid-19-API ](https://github.com/M-Media-Group/Covid-19-API) <br>
![covid details](https://raw.githubusercontent.com/LexxFade/Ivis-Bot/main/screenshots/covid.png)

- `/ping` <br>check ping <br>
![ping](https://raw.githubusercontent.com/LexxFade/Ivis-Bot/main/screenshots/ping.png)

### Welcome Message
Ivis also greets new members by pinging them and informing them about rules and roles channel (if any). These channels and the channel to post greetings can be configured by editing the [main file](https://github.com/LexxFade/Ivis-Bot/blob/main/ivis).<br>
```py
ivis
-------------------------------
# add welcome channel's id here
17. welcome_channel_id = "" 
.
.
.

# edit this line. either add channel id like <#channel-dl> or just write its name (case sensitive).
42. embed.add_field(name="°", value=f"Greetings {member}!\nCheck out #rules and #roles to get started.\n**✧**", inline=False)
```

### Extend
Ivis can be extended in either of the following ways:
1) add commands in [request.py](https://github.com/LexxFade/Ivis-Bot/blob/main/request.py)
2) write a new file and import it with [request](https://github.com/LexxFade/Ivis-Bot/blob/main/request.py) in [ivis](https://github.com/LexxFade/Ivis-Bot/blob/main/ivis)<br>
```py 
1. #!/usr/bin/env python
2. import discord, request #{add your filename here}
3. from discord.ext import commands
```
3) create corgs
