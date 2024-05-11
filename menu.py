from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from main import start

app = QApplication([])

window = QWidget()
window.resize(200, 100)

play_btn = QPushButton("PLAY")
shop_btn = QPushButton("SHOP")
shop_btn = QPushButton("SHOP")
gg_lbl = QLineEdit("")
skin_1 = QLabel()
buy_skin_1_btn = QPushButton("BUY SKIN EMMM")

skin_1_img = QPixmap("rocket.png")
skin_1_img = skin_1_img.scaledToWidth(64)
skin_1.setPixmap(skin_1_img)

main_line = QVBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
h5 = QHBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3.addWidget(gg_lbl)
h4.addWidget(skin_1)
h5.addWidget(buy_skin_1_btn)
h1.addWidget(play_btn)
h2.addWidget(shop_btn)
main_line.addLayout(h3)
main_line.addLayout(h4)
main_line.addLayout(h5)
main_line.addLayout(h1)
main_line.addLayout(h2)
settings = {}



def read_data():
    global settings
    try:
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    except:
        settings = {
            "skin": "rocket.png",
            "money": 0
        }


def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)

read_data()
def buy_skin_1():
    if settings["money"] >= 7:
        settings["money"] -= 7
        settings["skin"] = "asteroid.png"
        write_data()
    else:
        print("грошей не хватає!!!!")


buy_skin_1_btn.clicked.connect(buy_skin_1)
play_btn.clicked.connect(start)
window.setLayout(main_line)
window.show()
app.exec()