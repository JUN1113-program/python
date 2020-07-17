import tkinter as tk
import requests as req

root = tk.Tk()
root.title("")
root.geometry("200x100")
icon = './favicon.ico'
root.iconbitmap(default=icon)

def print_input_word():
    label["text"] = input_box.get()


def get_address():
    url = "https://zipcloud.ibsnet.co.jp/api/search"
    zipcode = input_box.get()
    response = req.get(url + "?zipcode=" + zipcode)
    print(response.text)
    response_json = response.json()["results"][0]
    print(response_json)
    zip_label["text"] = response_json["address1"] + response_json["address2"] + response_json["address3"]


label = tk.Label(root, text="郵便番号を入力してね")
label.pack(anchor='center', expand=1)

input_box = tk.Entry(root)
input_box.pack(anchor='center', expand=1)


button = tk.Button(root, text="検索", command=get_address)
button.pack(anchor='center', expand=1)

zip_label = tk.Label(root, text="")
zip_label.pack(anchor='center', expand=1)

root.mainloop()
