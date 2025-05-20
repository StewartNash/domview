from xml.etree import ElementTree


class IndexedTree(ElementTree):
    def __init__(self, position=[0]):
        super.__init__(self)
        self.position = position
