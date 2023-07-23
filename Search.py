import wikipediaapi
from tkinter import *

def search_wikipedia():
    search_query = entry.get()
    lang = language.get()

    wiki_wiki = wikipediaapi.Wikipedia(language=lang)
    page_py = wiki_wiki.page(search_query)
    if page_py.exists():
        result_text.delete('1.0', END)
        result_text.insert(END, page_py.text)
    else:
        result_text.delete('1.0', END)
        result_text.insert(END, "Page not found.")

root = Tk()
root.title("Wikipedia Search")
root.geometry("500x500")

label = Label(root, text="Enter a search term:")
label.pack()

entry = Entry(root, width=40)
entry.pack()

language = StringVar()
language.set("en")  # اللغة الافتراضية هي الإنجليزية
language_radio = Radiobutton(root, text="English", variable=language, value="en")
language_radio.pack()
language_radio = Radiobutton(root, text="Arabic", variable=language, value="ar")
language_radio.pack()

search_button = Button(root, text="Search", command=search_wikipedia)
search_button.pack()

result_text = Text(root, width=60, height=20)
result_text.pack()

root.mainloop()
