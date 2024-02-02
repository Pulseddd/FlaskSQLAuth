class CopyableObject():
    def __init__(self, object_name: str) -> None:
        self.obj_name = object_name
        self.copy = lambda: objects[self.obj_name](self.data)
    
class License(CopyableObject):
    def __init__(self, data: dict) -> None:
        self.key = data["key"]
        self.data = data
        super().__init__("license")


objects = {
    "license": License
}
