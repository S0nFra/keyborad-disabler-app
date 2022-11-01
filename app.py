import keyboard
from PIL import Image
from pystray import Icon, Menu, MenuItem
from plyer import notification as npa

class App:

    def __init__(self, icon_path=''):
        try:
            self._icon_on = Image.open(icon_path + "kon.png")
            self._icon_off = Image.open(icon_path + "koff.png")
        except FileNotFoundError:
            print("Files not found in",icon_path)
            npa.notify("Error",
                message=f"Files not found in {icon_path}",
                timeout = 5)
            exit()

        self._state = True
        self._menu = Menu(
            MenuItem("Clean keyboard",
                action=self._on_click,
                checked= lambda item: not self._state,
                visible= not Icon.HAS_DEFAULT_ACTION,
                default=True),
            MenuItem("Close",
                action= lambda : self.stop())
            )
        self._icon = Icon("App", self._icon_on, menu=self._menu)

    def _on_click(self):
        if self._state:
            for i in range(150):
                keyboard.block_key(i)            
            self._icon.icon = self._icon_off
            self._state = False
        else:
            keyboard.unhook_all()
            self._icon.icon = self._icon_on
            self._state = True

    def run(self):
        self._icon.run()
    
    def stop(self):
        self._icon.stop()

if __name__ == "__main__":
    App().run()