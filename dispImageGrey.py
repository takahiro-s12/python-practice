#ウィンドウを表示するモジュール
import tkinter as tk
#ファイルダイアログを使うモジュール
import tkinter.filedialog as fd
#画像を扱うモジュール
import PIL.Image
#tkinterで作った画面上に画像を表示させるモジュール
import PIL.ImageTk

#画像ファイルを表示する関数
def dispPhoto(path):
    #画像を読み込む
    newImage= PIL.Image.open(path).convert("L").resize((300,300))
    #画像をラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

#ファイルダイアログを開くための関数
def openFile():
    #ファイルダイアログを開いて選択したファイルを取得する
    fpath = fd.askopenfilename()
    #ファイル名があるかの判断
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()
tk.mainloop()
