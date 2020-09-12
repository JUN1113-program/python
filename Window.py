import tkinter as tk


class Window:
    root = tk.Tk()

    def __init__(self):
        self.root.title("")
        self.root.geometry("200x100")

    # 画面を開く
    # 注) 画面を閉じるまでこのコマンド移行は実行されない
    def open(self) -> None:
        print("画面をOpen")
        self.root.mainloop()

    # 画面のタイトルを設定する
    def set_title(self, title: str) -> None:
        print("titleの変更:" + title)
        self.root.title(title)

    # 画面のファビコンを設定する
    def set_icon(self, file_path: str) -> None:
        print("iconの変更:" + file_path)
        self.root.iconbitmap(default=file_path)

    # 画面幅を設定する
    def set_window_size(self, width: str, height: str) -> None:
        print("画面幅の変更:" + "幅:" + width + " 縦:" + height)
        self.root.geometry(width + "x" + height)
