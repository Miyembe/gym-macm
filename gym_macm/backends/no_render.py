from ..cm_framework import (FrameworkBase, Keys)
# from ..settings import fwSettings

class NoRender(FrameworkBase):
    def __init__(self,settings):
        super(NoRender, self).__init__()
        self.settings = settings
        if settings.onlyInit:  # testing mode doesn't initialize Pyglet
            return

        self.renderer = None

    def run(self):
        pass

    def quit(self):
        self.world.contactListener = None
        self.world.destructionListener = None
        pass

    def Keyboard(self, key):
        """
        Callback indicating 'key' has been pressed down.
        """
        pass

    def KeyboardUp(self, key):
        """
        Callback indicating 'key' has been released.
        See Keyboard() for key information
        """
        pass