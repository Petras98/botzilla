import socket, time
import threading
import sys
#from queue import Queue

""" bot_config class used to package information to give to bot so it can do its thing """
class bot_config:
    nick = ""

""" class for the actual bot """
class irc_bot:
    def __init__(self, server, port, channel, botconfig):
        self.server = server
        self.channel = channel
        self.port = port
        self.botconfig = botconfig

    def connect(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.server, self.port))

    def register(self):
        self.connection.send("USER {} {} {} : test bot lel\n\n".format(self.botconfig.nick, self.botconfig.nick, self.botconfig.nick))
        self.connection.send("NICK {}\n\n".format(self.botconfig.nick))
        self.connection.send("JOIN {}\n\n".format(self.channel))

    
    
    
    def say(self, message):
        self.connection.send("PRIVMSG {} :{}\n\n".format(self.channel, message))
        userInput = True
    

        while userInput: 
            time.sleep(0.1)
            
            try: 
                text = self.connection.recv(2040) 
                print text  
            except Exception: 
                pass

            if text.lower().find(":hi")!=-1: 
                self.connection.send("PRIVMSG {} :Im responding\r\n".format(self.channel)) 

            text=""

            
            if userInput == "exit":
                break
        
        userInput = raw_input("Type exit, to exit: ") 

if (__name__ == "__main__"):
    conf = bot_config
    conf.nick = "PetrasTestBotzillaBot"
    bot = irc_bot("irc.freenode.net", 6667, "#BotzillaBotTesting", conf)
    bot.connect()
    bot.register()
    
    threading1 = threading.Thread(target=bot.say("hi"))
    threading1.daemon = True
    threading1.start()

    while userInput
    userInput = raw_input("Enter exit")
    global userInput
    
    
    while(True):pass #should be replaced later with more productive loop

