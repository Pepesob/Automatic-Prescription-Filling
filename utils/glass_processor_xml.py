import xml.etree.ElementTree as ET

tree1 = ET.parse("./030002638240001.xml")


# if True it means it is good
def check1(tree):
    root = tree.getroot()
    temp = root.find("slowniki").findall("pakiet-zaopatrz")
    t = [temp[i].iter("poz-pak-zaopatrz") for i in range(12)]

    for a in list(zip(*t)):
        for item in a[1:]:
            if a[0].attrib != item.attrib:
                return False
    return True


def price_limits(tree: ET.ElementTree):
    root = tree.getroot()

    codes = root.find("slowniki").findall("prod-zposp")

    prices = {}
    for item in codes:
        code = item.attrib["kod-srodka"]
        name = item.attrib["nazwa"]
        price = item.find("limit-okres").find("limit-ceny").attrib["wart-limit-ce"]

        prices[code] = {"nazwa": name, "limit-ceny": price}

    return prices


def glasses_grouped_by_code_only_szajna_and_target(tree: ET.ElementTree):
    root = tree.getroot()
    glasses = {}
    for item in root.find("slowniki").iter("produkt-handlowy"):
        glasses[item.attrib["id-prod-handl"]] = item.attrib

    for item in root.find("slowniki").findall("pakiet-zaopatrz")[1].iter("poz-pak-zaopatrz"):
        glasses[item.attrib["id-prod-handl"]]["cena-brutto"] = item.attrib["cena-brutto"]

    group_by_kod_srodka = {}
    for k,v in glasses.items():
        kod_srodka = v["kod-srodka"]
        if group_by_kod_srodka.get(kod_srodka) is None:
            group_by_kod_srodka[kod_srodka] = []
        group_by_kod_srodka[kod_srodka].append(v)

    return group_by_kod_srodka


def write_to_file(tree):
    limits = price_limits(tree)
    glasses_dict = glasses_grouped_by_code_only_szajna_and_target(tree)

    with open("glass_codes.txt", "w", encoding="utf-8") as f:
        for code, glasses in glasses_dict.items():
            f.write(f"Kod: {code};   Limit ceny: {limits[code]['limit-ceny']};    Typ: {limits[code]['nazwa']}\n")
            f.write("Dostępne szkła:\n")
            for glass in glasses:
                if not glass["cena-brutto"] == limits[code]['limit-ceny']:
                    continue
                f.write(f"{glass}\n")
            f.write("\n\n")


def print_entries(tree):
    limits = price_limits(tree)
    glasses_dict = glasses_grouped_by_code_only_szajna_and_target(tree)

    for code, glasses in glasses_dict.items():
        print(f"Kod: {code};   Limit ceny: {limits[code]['limit-ceny']};    Typ: {limits[code]['nazwa']}")
        print("Dostępne szkła:")
        for glass in glasses:
            print(glass)
        print("\n\n")


write_to_file(tree1)
