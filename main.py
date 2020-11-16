from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()

def getStock():
    try:
        Symbol = TkStock.get()
        response = requests.get("https://money.cnn.com/quote/quote.html?symb={}".format(Symbol))
        soup = BeautifulSoup(response.text, 'html.parser')
        stock = soup.find(class_="wsod_last").contents[0].get_text()
        Label(root, text="The Stock Price for {} is ${}.".format(Symbol, stock)).pack()
    except Exception as e:
        ErrorLabel = Label(root, text="An Error has occured.").pack()
        print(e)

TkStock = Entry(root, width=20)
TkStock.pack()
TkStock.insert(0, "Stock Symbol")

TkButton = Button(root, text="Get Price", command=getStock)
TkButton.pack()

root.mainloop()