"""Minesweeper version 0.2.2 made by Ryan Callahan"""

from tkinter import *
from tkinter import ttk
import random

root = Tk()

class Minesweeper:
    pass


class MinesweeperButton(Button):
    def __init__(self, **args):
        super().__init__(**args)
        self.minestate = None


class Minebutton:

    def __init__ (self, root):
        self.button_dict = dict()
        mines = 25
        self.mlist = []
        self.mines = []

        for x in range(0, 10):
            for y in range(0,10):
                self.mlist.append([x, y])

        for x in range(0, 10):
            for y in range(0, 10):
                self.button_dict[f"{x}, {y}"] = MinesweeperButton(text="", height=1, width=2)
                self.button_dict[f"{x}, {y}"].bind("<ButtonRelease-1>", self.minesweeperclick)
                self.button_dict[f"{x}, {y}"].bind("<ButtonRelease-3>", self.flag)
                self.button_dict[f"{x}, {y}"].grid(column=x, row=y)

        for x in range(0, mines):
            self.minegenerate()

    def minegenerate(self):
        x, y = random.choice(self.mlist)
        self.mines.append(self.button_dict[f"{x}, {y}"])
        self.button_dict[f"{x}, {y}"].unbind("<ButtonRelease-1>")
        self.button_dict[f"{x}, {y}"].bind("<ButtonRelease-1>", self.boom)
        self.mlist.remove([x, y])

    def boom(self, event):
        for button in self.button_dict.values():
            button.update()
            root.update()
            button_geo, button_x, button_y = button.winfo_geometry().split("+")
            button_length, button_height = button_geo.split("x")
            root_x, root_y = root.winfo_rootx(), root.winfo_rooty()
            x = int(event.x_root) - int(root_x)
            y = int(event.y_root) - int(root_y)
            if x in range(int(button_x), (int(button_x) + int(button_length)))\
                    and y in range(int(button_y), (int(button_y) + int(button_height))):
                button.config(state="disabled", text="mine")
                root.update()
                root.destroy()
                break

    def flag(self, event):
        for button in self.button_dict.values():
            button.update()
            root.update()
            button_geo, button_x, button_y = button.winfo_geometry().split("+")
            button_length, button_height = button_geo.split("x")
            root_x, root_y = root.winfo_rootx(), root.winfo_rooty()
            x = int(event.x_root) - int(root_x)
            y = int(event.y_root) - int(root_y)
            if x in range(int(button_x), (int(button_x) + int(button_length)))\
                    and y in range(int(button_y), (int(button_y) + int(button_height))):
                button.config(state="disabled", text="flag")
                button.unbind("<ButtonRelease-1>")
                button.unbind("<ButtonRelease-3>")
                button.bind("<ButtonRelease-3>", self.unflag)


    def unflag(self, event):
        for button in self.button_dict.values():
            button.update()
            root.update()
            button_geo, button_x, button_y = button.winfo_geometry().split("+")
            button_length, button_height = button_geo.split("x")
            root_x, root_y = root.winfo_rootx(), root.winfo_rooty()
            x = int(event.x_root) - int(root_x)
            y = int(event.y_root) - int(root_y)
            if x in range(int(button_x), (int(button_x) + int(button_length)))\
                    and y in range(int(button_y), (int(button_y) + int(button_height))):
                button.config(state="disabled", text="")
                button.unbind("<ButtonRelease-3>")
                button.bind("<ButtonRelease-1>", self.minesweeperclick)
                button.bind("<ButtonRelease-3>", self.flag)


    def minesweeperclick(self, event):
        for button in self.button_dict.values():
            button.update()
            root.update()
            button_geo, button_x, button_y = button.winfo_geometry().split("+")
            button_length, button_height = button_geo.split("x")
            root_x, root_y = root.winfo_rootx(), root.winfo_rooty()
            #print(button_geo)
            x = int(event.x_root) - int(root_x)
            y = int(event.y_root) - int(root_y)
            if x in range(int(button_x), (int(button_x) + int(button_length)))\
                    and y in range(int(button_y), (int(button_y) + int(button_height))):
                button.config(state="disabled")
                button.unbind("<ButtonRelease-3>")
                self.numbertest(button)

    def numbertest(self, button):
        adjacentmines = 0
        for list in self.button_dict.items():
            if button in list:
                x, y = list[0].split(", ")
                try:
                    if self.button_dict[f"{str(int(x)-1)}, {str(int(y)+1)}"] in self.mines:
                        adjacentmines += 1
                except KeyError:
                    pass
                try:
                    if self.button_dict[f"{str(int(x)-1)}, {y}"] in self.mines:
                        adjacentmines += 1
                except KeyError:
                    pass
                try:
                    if self.button_dict[f"{str(int(x)-1)}, {str(int(y)-1)}"] in self.mines:
                        adjacentmines += 1
                except KeyError:
                    pass
                try:
                    if self.button_dict[f"{x}, {str(int(y)-1)}"] in self.mines:
                        adjacentmines += 1
                except KeyError:
                    pass
                try:
                    if self.button_dict[f"{x}, {str(int(y)+1)}"] in self.mines:
                        adjacentmines += 1
                except KeyError:
                    pass
                try:
                    if self.button_dict[f"{str(int(x)+1)}, {str(int(y)+1)}"] in self.mines:
                        adjacentmines += 1
                except KeyError:
                    pass
                try:
                    if self.button_dict[f"{str(int(x)+1)}, {y}"] in self.mines:
                        adjacentmines += 1
                except KeyError:
                    pass
                try:
                    if self.button_dict[f"{str(int(x)+1)}, {str(int(y)-1)}"] in self.mines:
                        adjacentmines += 1
                except KeyError:
                    pass
                button.config(text=adjacentmines)


    def minetest(self, button):
        button.config(text="click")


Minebutton(root)
root.mainloop()