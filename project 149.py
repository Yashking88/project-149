from tkinter import *
import random

root=Tk()
root.title("Random Word Generator")
root.geometry("400x400")
root.config(bg = "cyan1")

generatedWord = Label(root, font="Roboto")
def generatorFunc():
    
   alpha_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
   random_no1 = random.randint(1,26)
   random_no2 = random.randint(1,26)
   random_no3 = random.randint(1,26)
   random_no4 = random.randint(1,26)
   random_no5 = random.randint(1,26)

   random_alpha1 = alpha_list[random_no1]
   random_alpha2 = alpha_list[random_no2]
   random_alpha3 = alpha_list[random_no3]
   random_alpha4 = alpha_list[random_no4]
   random_alpha5 = alpha_list[random_no5]
   generatedWord["text"]=str(random_alpha1) + str(random_alpha2) + str(random_alpha3) + str(random_alpha4) + str(random_alpha5)

callGenerator = Button(root, text="Generate Random Letters", bg="red", font="stgotic", command=generatorFunc)
callGenerator.place(relx=0.5, rely=0.2, anchor=CENTER)

generatedWord.place(relx=0.5, rely=0.4, anchor=CENTER)
root.mainloop()