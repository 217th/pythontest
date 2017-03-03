rels = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for (offset, rel) in enumerate(reversed(rels)):
    if rels.index(rel) > 0:
        for relPrev in rels[0: rels.index(rel)]:
            print(offset, rel, relPrev)
            if (relPrev-rel > 1):
                rels.pop(rels.index(rel))
                break

print(rels)