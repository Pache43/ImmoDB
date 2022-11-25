class immo:

    def __init__(self, id, name, link, lastEdit, price, bundesland, ort, attributes):
        self.id = id
        self.name = name
        self.link = link
        self.lastEdit = lastEdit
        self.price = price
        self.bundesland = bundesland
        self.ort = ort
        self.attreibutes = attributes

    def toString(self):
        return "[" + self.id + "]: " + self.price + ", " + self.name