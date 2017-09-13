# -*- coding: utf-8 -*-
from discord import *
import asyncio
import config
import random

class Bot(Client):
    """ Classe Bot extend de discord.client
    """
    def __init__(self):
        """Constructeur par defaut
        """
        self.__listChannelCree = {}
        self.__channelLog = None
        self.__roleAdmin= None
        super().__init__()

    def lancer(self):
        """Lance le Bot sur le serveur
        Return True
        """
        self.run(config.apiBot)
        return True

    async def on_ready(self):
        """Fonction quand le Bot est connecté
        initialise les attributs de la classe
        """
        print('Connecté en tant que')
        print(self.user.name)
        print(self.user.id)
        print('------')      
      
        for s in self.servers:
            self.serveur = s
            self.__roleAdmin = s.role_hierarchy[0]
            
        
        self.__channelLog=utils.find(lambda m: m.name == 'logbot', self.serveur.channels)
        if self.__channelLog == None:
            everyone = PermissionOverwrite(read_messages=False)
            self.__channelLog = await self.create_channel(self.serveur, 'logbot', (self.serveur.default_role, everyone), type=ChannelType.text)

    async def cree_channel(self):
        """ Crée un channel Vocal a partir de la liste de mot de `nomsChannel.py`
        Return Channel
        """
        nomChannel = random.choice(config.nomsChannel)
        while nomChannel.lower() in  self.__listChannelCree.keys() :
              nomChannel = nomChannel+str(random.randint(0,9))
        channel = await self.create_channel(self.serveur, nomChannel, type=ChannelType.voice)
        self.__listChannelCree[nomChannel.lower()]=channel
        return channel

    async def suppr_channel(self, nom):
        """ Supprime le channel Vocal crée par le bot a partir de son nom
        Parameters : nom : nom du channel
        """
        nom = nom.lower()
        channel = self.__listChannelCree[nom]
        if channel is not None:
            del self.__listChannelCree[nom]
            await self.delete_channel(channel)
            return True
        return False

    async def on_message(self,message):
        """Lit les messages saisie sur le serveur
        """
        try:
            if message.author == self.user:
                return
            if message.content.startswith("!move"):
                param = message.content.split(" ")
                if len(param)!=2:
                    msg = '{0.author.mention}, commande incorrect ```!move <channel-name>```'.format(message)
                    await self.send_message(message.channel, msg)
                    return
                if message.author.voice.voice_channel == None:
                    msg = '{0.author.mention}, veuillez vous connectez à un channel vocale'.format(message)
                    await self.send_message(message.channel, msg)
                    return
                nomChannel = param[1].lower()
                if nomChannel in self.__listChannelCree.keys():
                    channel = self.__listChannelCree[nomChannel]
                    await self.move_member(message.author, channel)
                    return
            #Commande Admin        
                    
            print(message.author.top_role.name)
            
            print(self.__roleAdmin.name)
            if message.author.top_role != self.__roleAdmin:
                return
            if message.content.startswith('!create'):
                param = message.content.split(" ")
                if len(param)==2:
                    channel = await self.create_channel(self.serveur, param[1], type=ChannelType.voice)
                else:
                    channel = await self.cree_channel()
                await self.__logMes("Channel "+channel.name+" crée")

            elif message.content.startswith('!deleteAll'):
                await self.__supprAllChannel()
            elif message.content.startswith('!delete'):
                param = message.content.split(" ")
                if len(param)==2:
                    channel = await self.suppr_channel(param[1])
                    await self.__logMes("Channel "+param[1]+" suppr")
                else:
                    await self.__supprMyChannel()
            elif message.content.startswith('!moveChannelTop'):
                channel = self.__listChannelCree[message.content.split(" ")[1].lower()]
                if channel.position != 1:
                    await self.move_channel(channel, 1)
        except Exception as e:
            await self.__logMes("**Exception** : \n```sh\n"+str(e)+"```")



    async def __supprMyChannel(self):
        """Supprime tout les channels Vocales crée par le BOT
        """
        channelAsuppr = []
        for nom, c in self.__listChannelCree.items():
            channelAsuppr.append(c)
        for cS in channelAsuppr:
            del self.__listChannelCree[cS.name.lower()]
            await self.delete_channel(cS)
        await self.__logMes("Channels  suppr")
        return

    async def __supprAllChannel(self):
        """Supprime tout les channels Vocales sauf le channel "General"
        """
        channelAsuppr = []
        for c in self.serveur.channels:            
            print(c.name)
            if c.name.lower() != "general" and c.type == ChannelType.voice:
                channelAsuppr.append(c)
        for cS in channelAsuppr:
            await self.delete_channel(cS)
        await self.__logMes("Channels  suppr")
        return

    async def __logMes(self, message):
        """
        Envoie un message dans le channel de log du Bot
        """
        await self.send_message(self.__channelLog, message)




if __name__ == "__main__":
    bot = Bot()
    bot.lancer()
