from abstract import *

class HomePC(PC):
    def release_computer(self, component: Screen):
        print("Создан домашний компьютер и к нему подключено устройство под названием ", end="")
        component.release_component()


class OfficePC(PC):
    def release_computer(self, component: Screen):
        print("Создан домашний компьютер и к нему подключено устройство под названием ", end="")
        component.release_component()
