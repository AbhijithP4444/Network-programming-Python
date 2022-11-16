import socket
from tkinter import *
def send(listbox,entry):
    message=entry.get()
    listbox.insert('end',"Client:"+message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))

def recieve(listbox):
    message_from_server = s.recv(1000)
    listbox.insert('end',"Server:"+message_from_server.decode("utf-8"))

root=Tk()
root.geometry('250x300')
entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
button=Button(root,text="send",command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)
rbutton=Button(root,text="recieve",command=lambda :recieve(listbox))
rbutton.pack(side=BOTTOM)
root.title("Client")


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.connect((HOST_NAME,PORT))

# while True:
#     msg=s.recv(1000)
#     print("server:"+msg.decode('utf-8'))
#     message_to_server=input("client:")
#     s.send(bytes(message_to_server,"utf-8"))
root.mainloop()