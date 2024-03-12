																					      
# Do Anything You Want in this bot...
import sqlite3, telebot, random
ftext = ""
token ="7149334849:AAFucSKmjUrhj2KuabrXAsWtuOexI7eD0RA"
bot =telebot.TeleBot(token)



def search_all(id):
   cn =sqlite3.connect('iran_data(PRISM).sqlite')
   cr= cn.cursor()
   info=id.text.split(" ")[1]
   #       try:
   daddy = cr.execute("""SELECT * FROM niggers WHERE id = {} OR phone = {} OR username = {}""".format(info,info,info)).fetchone()
   print(daddy)	
   hmmmm = """niggger info\\nid: {}\\nphone: +{}\\nusername: @{}\\nby @o1hmmm""".format(daddy[0],daddy[1],daddy[2])
   bot.send_message(id.chat.id, text=hmmmm)
    #      except:
#      bot.send_message(id.chat.id, text="{} not found".format(info))
def random_search(id):
   cn =sqlite3.connect('iran_data(PRISM).sqlite')
   cr= cn.cursor()
   rowid =random.randint(0, 50000)
   text =cr.execute("SELECT * FROM niggers WHERE rowid = {}".format(rowid)).fetchone()
   text="""nigger info
id: {}
phone: +{}
username: @{}""".format(text[0], text[1], text[2])
   bot.send_message(id, text=text)
@bot.message_handler(commands=["start"])
def hi(message):
   bot.send_message(message.chat.id, text="hello user")
@bot.message_handler(commands=["rand"])
def rand_search(message):
   id = message.chat.id
   random_search(id)
@bot.message_handler(commands=["search"])
def hmmm(message):
   search_all(message)



print("go PRISM")
bot.polling(True, timeout=60)

																		
