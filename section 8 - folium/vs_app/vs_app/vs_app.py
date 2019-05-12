import json

f = open('world.json', 'r', encoding='utf-8-sig')
world = json.load(f)
f.close()

print(type(world))
