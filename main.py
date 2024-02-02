from SQLAuth.datatypes import CopyableObject, License

data = {
    "key": "real"
}
l = License(data)
k = l.copy()