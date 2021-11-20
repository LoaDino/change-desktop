import win32api, win32con, win32gui
from time import sleep

base = "C:\\Users\\2\\Desktop\\change_desktop\\desktops\\" #у меня это лежало на раб.столе просто

Red = 0
Blue = 0
Green = 0

colors = { "R": "red", "G": "green", "B": "blue"} #соответсвтие между говно-кодерным языком и нормальным


def comparison(R:int, G:int, B:int): #находим какого цвета больше всего - это и будет цвет обоев
    M = max(R,G,B) 

    if M == R:
        return "R"
    elif M == B:
        return "B"
    elif M == G:
        return "G"


def setWallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE) #получаем ключ, по которому будем находить путь к обоям
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0") 
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0") # для изменен6ия обоев (не вникал, честно)
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2) #изменяем обои на нужные

def pixel_color_at(x, y):
    hdc = win32gui.GetWindowDC(win32gui.GetDesktopWindow()) #получаем весь экран
    c = int(win32gui.GetPixel(hdc, x, y)) # получаем пиксель по координатам с экрана
    # (r, g, b)
    return (c & 0xff), ((c >> 8) & 0xff), ((c >> 16) & 0xff) #возвращаем кортеж из R, G, B



input("put the cursor on the indicator") #ждем, пока наведем курсор на место, где проверка цвета
indicator = win32gui.GetCursorPos() #получаем позицию курсора

COLOR = ""

while True:
    RGB = pixel_color_at(indicator[0], indicator[1])

    indicator_color = comparison(RGB[0],RGB[1],RGB[2])

    if indicator_color != COLOR: #если цвет изменился, меняем нынешний цвет и меняем обои
        COLOR = indicator_color

        setWallpaper(base+f"{colors[COLOR]}.jpg")

    sleep(0.2) #пауза, чтобы не жрать много памяти и цп (мелочь, а приятно)