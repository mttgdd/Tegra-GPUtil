class GPU:
    def __init__(self, id=0, is_tegra=False):
        self.id = id
        self.is_tegra = is_tegra

    def setup(self):
        if not self.is_tegra:
            self.dev = GPUtil.getGPUs()[self.id]
        else:
            self.dev = jtop()
            self.dev.start()

    def memoryUsed(self):
        return self.dev.ram['use'] if self.is_tegra else self.dev.memoryUsed

    def load(self):
        return self.dev.gpu['val'] if self.is_tegra else self.dev.load

    def memoryTotal(self):
        return self.dev.ram['tot'] if self.is_tegra else self.dev.memoryTotal

    def uuid(self):
        return self.dev.board['hardware']['SERIAL_NUMBER'] if self.is_tegra else self.dev.uuid

    def name(self):
        return self.dev.board['info']['machine'] if self.is_tegra else self.dev.name

    def temperature(self):
        return self.dev.temperature['GPU'] if self.is_tegra else self.dev.temperature
