from factory import *


def main():
    h_factory = HomeComputerFactory()
    hpc = h_factory.create_computer()
    hscreen = h_factory.create_screen()

    hpc.release_computer(hscreen)

    o_factory = OfficeComputerFactory()
    opc = o_factory.create_computer()
    oscreen = o_factory.create_screen()

    opc.release_computer(oscreen)


if __name__ == "__main__":
    main()
