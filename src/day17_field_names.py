layer = iface.activeLayer()

features = layer.getFeatures()
print(features)
ids = []
for feature in features:
    id = feature.id()
    ids.append(id)
    break
    
    
print(ids)

f = next(features)
fields = f.fields()

for field in fields:
    print(field.name())
    
field_names = [field.name for field in fields]
print(field_names)