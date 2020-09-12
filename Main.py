from ZipCodeWindow import ZipCodeWindow

# windowのインスタンスを作成
zip_window = ZipCodeWindow()

# 画面の情報を設定
zip_window.set_title("test")
zip_window.set_icon("./favicon.ico")
zip_window.set_window_size("300", "200")

# 画面を開く
zip_window.open()
