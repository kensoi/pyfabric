from abstract import *
from screen import *
from pc import *

class HomeComputerFactory(ComputerFactory):
    def create_computer(self) -> PC:
        return HomePC()
    
    def create_screen(self) -> Screen:
        return Monitor()
    

class OfficeComputerFactory(ComputerFactory):
    def create_computer(self) -> PC:
        return OfficePC()
    
    def create_screen(self) -> Screen:
        return Projector()