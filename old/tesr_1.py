drinks={
    'martini': {'vodka','vermouth'},
    'black russian': {'vodka','kahlua'},
    'white russian': {'cream','vodka','kahlua'},
    'manhattan': {'rye','vermouth','bitters'},
    'screwtriver': {'orange juice','vodka'}
    }
print(drinks.items())
for a,b in drinks.items():
    if 'vodka' in b:
        print(a)
