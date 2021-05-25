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

    def on_button_press(self, event):
        """
        The method for when the left mouse button is pressed and a selection
        should be started.
        Parameters:
            event: Bound to <ButonPress-1>.
        """

        # save mouse drag start position
        self.startX = self.screenCanvas.canvasx(event.x)
        self.startY = self.screenCanvas.canvasy(event.y)

        self.rect = self.screenCanvas.create_rectangle(
            self.x, self.y, 1, 1, outline='#dbf3ff', width=2)

    def exitScreenshotMode(self):
        """ Method to exit the selecting mode. """
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        root.deiconify()

    def exit_application(self):
        """ Method to end the application. """
        root.quit()


root = Tk()
app = Application(root)
