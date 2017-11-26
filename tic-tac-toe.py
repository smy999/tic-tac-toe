from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"
            
      if list[0]["text"] == list[1]["text"] == list[2]["text"] != "     ":
            w_msg(player)
      if list[3]["text"] == list[4]["text"] == list[5]["text"] != "     ":
            w_msg(player)
      if list[6]["text"] == list[7]["text"] == list[8]["text"] != "     ":
            w_msg(player)
      if list[0]["text"] == list[3]["text"] == list[6]["text"] != "     ":
            w_msg(player)
      if list[1]["text"] == list[4]["text"] == list[7]["text"] != "     ":
            w_msg(player)
      if list[2]["text"] == list[5]["text"] == list[8]["text"] != "     ":
            w_msg(player)
      if list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
            w_msg(player)
      if list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
            w_msg(player)
            
def w_msg(player):
      if player=="O":
            m=Message(window, text="O is winner")
            m.grid(row=3, column=0)
      if player=="X":
            m=Message(window, text="X is winner")
            m.grid(row=3, column=0)

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


