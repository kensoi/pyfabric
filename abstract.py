from abc import ABCMeta, abstractmethod

class Screen (metaclass=ABCMeta):
    @abstractmethod
    def release_component(self):
        pass

class PC (metaclass=ABCMeta):
    @abstractmethod
    def release_computer(self, component: Screen):
        pass

class ComputerFactory (metaclass=ABCMeta):
    @abstractmethod
    def create_computer(self)->PC:
        pass
    
    @abstractmethod
    def create_screen(self) -> Screen:
        pass