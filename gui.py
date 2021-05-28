from tkinter import *
import pyautogui


class Application():
    """
    This is a class for the GUI for screen snipping text.

    Attributes:
        master (Tk()): Required to start the tkinter GUI.
    """

    def __init__(self, master) -> None:

        self.master = master
        self.master.geometry("350x300+500+300")

        # nav bar frame
        self.nav_bar = Frame(self.master, height=20, width=50)
        self.nav_bar.rowconfigure(0, minsize=50, weight=1)
        self.master.columnconfigure([0, 1, 2], minsize=50, weight=1)
        self.nav_bar.pack(side=TOP)

        # textbox frame
        self.textframe = Frame(self.master, height=600, width=500)
        self.textframe.pack()

        # button snip
        self.btn_snip = Button(self.nav_bar, text="Snip",
                               command=self.select_ROI)
        self.btn_snip.grid(row=0, column=0, sticky="nsew")

        # button translate from
        self.curr_lang_from = StringVar(master)
        self.curr_lang_from.set("en")
        self.btn_translate_from = OptionMenu(
            self.nav_bar, self.curr_lang_from, "en")
        self.btn_translate_from.grid(row=0, column=1, sticky="nsew")

        # button translate to
        self.curr_lang_to = StringVar(master)
        self.curr_lang_to.set("cn")
        self.btn_translate_to = OptionMenu(
            self.nav_bar, self.curr_lang_to, "en", "jp")
        self.btn_translate_to.grid(row=0, column=2, sticky="nsew")

        # textbox
        self.textbox = Text(self.textframe)
        placeholder = "中文"
        self.textbox.insert(END, placeholder)
        self.textbox.pack()

        # roi canvas ( screen selectable )
        self.ROI_window = Toplevel()
        self.ROI_window.attributes("-alpha", .8)
        self.ROI_frame = Frame(self.ROI_window, background="#8698b0")
        self.ROI_frame.pack(fill=BOTH, expand=YES)
        self.ROI_window.withdraw()

    def select_ROI(self):

        print("selectROI clicked")

        self.roi_canvas.attributes('-fullscreen', True)
        self.roi_canvas.attributes('-alpha', .2)
        self.roi_canvas.attributes("-topmost", True)
        # self.roi_canvas.lift()
        self.master.withdraw()  # hide master
        self.roi_canvas.deiconify()  # show roi_canvas

        # bind buttons
        self.roi_canvas.bind("<buttonPress-1>", self.on_left_click)
        self.roi_canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.roi_canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

    def on_left_click(self):
        print("left mouse button clicked ")

    def on_mouse_drag(self):
        print("mouse dragging")

    def on_mouse_release(self):
        print("Mouse released")
        self.roi_canvas.withdraw()
        self.master.deconify()

    def snip(self, left, top, width, height):
        """
        The method to take a screenshot given an area.
        Parameters:
            left (int): The left position.
            top (int): The top position.
            width (int): The width.
            height (int): The height.
        """
        im = pyautogui.screenshot(region=(left, top, width, height))
        im.save(".capture.png")

    def exitScreenshotMode(self):
        """ Method to exit the selecting mode. """
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        self.master.deiconify()

    def exit_application(self):
        """ Method to end the application. """
        self.master.quit()


def main():
    root = Tk()
    app = Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
