import xmlrpclib
from threading import Thread
import time
from Tkinter import *

class MyApp:
    def __init__(self, parent, server):
        self.last_message_id = -1
        self.myParent = parent   
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.userFlag = 1
        self.userName = None
        self.display = Text(self.myContainer1, bd=5, height=15, takefocus=0)
        self.display.pack(side=TOP)
        self.writer = Text(self.myContainer1,bd=5, height=5)
        self.writer.pack(side=TOP)
        self.writer.bind("<Return>", self.getText)
        
        a = "localhost"
        whserver = "http://"+a+":"+"8000"

        self.server = xmlrpclib.ServerProxy(whserver)
        self.displayText("Ingrese un Nombre de Usuario:\n") 
        
        
               
    def getText(self, event):
        ans = self.writer.get(1.0, "end-1c")
        self.writer.delete(1.0, END)
        self.writer.mark_set("insert", "1.0")
        if(self.userFlag):
            self.registerUser(ans)
        else:
            self.received(ans)
                       
       
    
    
    def displayText(self, text):
        self.display.configure(state = NORMAL)
        self.display.insert(INSERT, text)
        self.display.see(END)
        self.display.configure(state = DISABLED)
            
    def registerUser(self, user):
         
        if self.server.log(user):
            self.displayText("Usuario en uso\n")
        else:
            self.userFlag=0
            self.display.delete(0.0, END)
            self.userName = user
            self.refresh()
            

    def received(self, text):
        try:
            self.server.enviado(self.userName,text)
            
        except Exception, e:
            pass
        time.sleep(1)
    
    def refresh(self):
        try:
            msjs = self.server.recv(int(self.last_message_id)+1)
        except Exception:
            pass
        for m in msjs:
            if int(m['id']) > self.last_message_id:
                self.last_message_id = int(m['id'])
                self.displayText('%s dice: %s\n\n' % (m['usuario'], m['texto']))
        self.display.see(END)
        self.display.after(1, self.refresh)
  
        
    

a = "localhost"
whserver = "http://"+a+":"+"8000"
server = xmlrpclib.ServerProxy(whserver)
  
def listening():           
    root = Tk()
    root.wm_title("AlCaChat 0.1")
    myapp = MyApp(root, server)
    root.mainloop()
    try:
        server.logout(myapp.userName)
    except Exception, e:
        pass



def synch():
  while True:  
    if not listen.is_alive():
      break
    t1 = time.time()
    try:
      ts = server.sincronizar()
    except Exception : 
      continue
    ta =  ts + (time.time() - t1)
    time.sleep(1)

listen = Thread (target = listening)
listen.start()

synchro = Thread (target = synch)
synchro.start()

