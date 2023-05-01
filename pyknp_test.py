from pyknp import KNP

knp = KNP()
result = knp.parse("霞ヶ浦で泳いでいる少女を見た。")

for tag in result.tag_list():
    for word in tag.mrph_list():
        ne_anotation = word.fstring
        if "固有キー" in ne_anotation:
            print(word.genkei)