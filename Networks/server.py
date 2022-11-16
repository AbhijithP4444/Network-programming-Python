import socket
from tkinter import *

def send(listbox,entry):
    message=entry.get()
    listbox.insert('end',"Server:"+message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))
def recieve(listbox):
    message_from_client = client.recv(1000)
    listbox.insert('end',"Client:"+message_from_client.decode("utf-8"))

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
root.title("Server")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.bind((HOST_NAME,PORT))
s.listen(4)


client,address=s.accept()
# print("client is connected and has the address", address)
# while True:
#     message_to_client=input("server:")
#     client.send(bytes(message_to_client, "utf-8"))
root.mainloop()


