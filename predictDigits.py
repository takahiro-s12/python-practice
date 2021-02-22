import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.ANTIALIAS)
    #画像の濃淡を数字に変換
    numImage = numpy.asarray(grayImage, dtype = float)
    #実数を整数に切り捨てて変換 → 濃淡を0〜16に変更
    numImage = numpy.floor(16 - 16 * (numImage / 256))
    #配列を一次元化
    numImage = numImage.flatten()

    return numImage

def predictDigits(data):
    #学習用データの読込
    digits = sklearn.datasets.load_digits()
    #機械学習をする
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    #予測変換する
    n = clf.predict([data])
    print("予測=",n)

data = imageToData("2.png")
predictDigits(data)


"""
SVMとは
SVM(サポートベクターマシン)とはデータを分類して境界線を引くためのアルゴリズム
「教師あり学習」の手法を用いて正解データを「教師からの助言」として学習し、学習結果をもとに境界線を定めた「分類器」を作成する
その分類器を活用して、新しいデータ(未知のデータ)を入力した時に、そのデータがどちらに分類されるかを区別することができるようになる
"""
