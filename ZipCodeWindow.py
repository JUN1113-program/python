from Window import Window
import requests as req
import tkinter as tk


class ZipCodeWindow(Window):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self.root, text="郵便番号を入力してね")
        self.label.pack(anchor='center', expand=1)

        self.input_box = tk.Entry(self.root)
        self.input_box.pack(anchor='center', expand=1)

        self.button = tk.Button(self.root, text="検索", command=self.get_address)
        self.button.pack(anchor='center', expand=1)

        self.zip_label = tk.Label(self.root, text="")
        self.zip_label.pack(anchor='center', expand=1)

    def print_input_word(self) -> None:
        self.label["text"] = self.input_box.get()

    def get_address(self) -> None:
        url = "https://zipcloud.ibsnet.co.jp/api/search"
        zipcode = self.input_box.get()
        response = req.get(url + "?zipcode=" + zipcode)
        print(response.text)
        response_json = response.json()["results"][0]
        print(response_json)
        self.zip_label["text"] = response_json["address1"] + response_json["address2"] + response_json["address3"]
