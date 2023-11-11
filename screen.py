from abstract import *


class Monitor (Screen):
    def release_component(self):
        print("монитор")


class Projector (Screen):
    def release_component(self):
        print("проектор")
