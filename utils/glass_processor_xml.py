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


# write_to_file(tree1)

glasses_array = [
{'id-prod-handl': '2632098', 'kod-prod-handl': '2284', 'kod-srodka': 'O.01.02.00.D.PR', 'nazwa-handl': 'SZKŁO OKULAROWE', 'nazwa-prod': 'JZO', 'model': 'NIE DOTYCZY', 'indyw-zamow': 'N', 'cena-brutto': '25.00'},

{'id-prod-handl': '2632030', 'kod-prod-handl': '1535', 'kod-srodka': 'O.03.01', 'nazwa-handl': 'SOCZEWKA KONTAKTOWA MIĘKKA', 'nazwa-prod': 'CIBA VISION', 'model': 'NIE DOTYCZY', 'indyw-zamow': 'N', 'cena-brutto': '150.00'},

{'id-prod-handl': '2632279', 'kod-prod-handl': '2282', 'kod-srodka': 'O.01.01.00.B.PR', 'nazwa-handl': 'SZKŁO OKULAROWE', 'nazwa-prod': 'JZO', 'model': 'NIE DOTYCZY', 'indyw-zamow': 'N', 'cena-brutto': '25.00'},

{'id-prod-handl': '2632325', 'kod-prod-handl': '2356', 'kod-srodka': 'O.01.02.01.D2.PR', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'OPTIPLAST 1,5', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2631965', 'kod-prod-handl': '2377', 'kod-srodka': 'O.01.01.00.B2.PR', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'OPTIPLAST 1,6', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632457', 'kod-prod-handl': '2357', 'kod-srodka': 'O.01.02.00.D2.PR', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'OPTIPLAST 1,5', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632405', 'kod-prod-handl': '1903', 'kod-srodka': 'O.01.01.01.B', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'TARGET', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '25.00'},

{'id-prod-handl': '2632765', 'kod-prod-handl': '1899', 'kod-srodka': 'O.01.02.01.D', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'TARGET', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '25.00'},

{'id-prod-handl': '2632660', 'kod-prod-handl': '2375', 'kod-srodka': 'O.01.01.00.B2', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'RAKO', 'model': 'CR 1,56 A', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632536', 'kod-prod-handl': '2302', 'kod-srodka': 'O.01.02.00.D1', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632629', 'kod-prod-handl': '2313', 'kod-srodka': 'O.01.01.01.B1', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632052', 'kod-prod-handl': '2291', 'kod-srodka': 'O.01.02.01.D1', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632079', 'kod-prod-handl': '1895', 'kod-srodka': 'O.01.02.00.D', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'TARGET', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '25.00'},

{'id-prod-handl': '2632809', 'kod-prod-handl': '2371', 'kod-srodka': 'O.01.01.01.B2', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'CR 1,5', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632459', 'kod-prod-handl': '2334', 'kod-srodka': 'O.01.02.01.D2', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'CR 1,5', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632187', 'kod-prod-handl': '2376', 'kod-srodka': 'O.01.01.01.B2.PR', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'SZAJNA', 'model': 'OPTIPLAST 1,5', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632497', 'kod-prod-handl': '2328', 'kod-srodka': 'O.01.01.00.B1', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'RAKO', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632586', 'kod-prod-handl': '2347', 'kod-srodka': 'O.01.02.00.D2', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'RAKO', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

{'id-prod-handl': '2632586', 'kod-prod-handl': '2347', 'kod-srodka': 'O.01.02.00.D2', 'nazwa-handl': 'SOCZEWKA OKULAROWA', 'nazwa-prod': 'RAKO', 'model': 'CR', 'indyw-zamow': 'N', 'cena-brutto': '100.00'},

]

glasses_array_only_codes = {entry["kod-srodka"]: entry["id-prod-handl"] for entry in glasses_array}

print(glasses_array_only_codes)