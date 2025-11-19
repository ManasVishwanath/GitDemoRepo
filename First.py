class TestCapture:
    def __init__(self):
        self.capture = {}

    def put(self,key,value):
        self.capture[key] = value
    def get(self,key):
        return self.capture[key]