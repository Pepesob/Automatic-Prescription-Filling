from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import json
import os


class Browser:

    def __init__(self):
        self.login = ""
        self.password = ""

        self.current_person_num = "0-23-000000000-0"

        self.diff_receiver_name = ""
        self.diff_receiver_surrname = ""
        self.diff_receiver_pesel = ""
        with open(os.path.join(os.path.dirname(__file__), "resources", "data.json")) as f:
            dict_data = json.load(f)
            self.login = dict_data["login"]
            self.password = dict_data["password"]


        # if self.login == "" or self.password == "": # why did I even add this here?
        #     return

        # inicjalizacja
        self.path = 'resources\\chromedriver.exe'
        self.chrome_service = Service(ChromeDriverManager().install())
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.chrome_service.creation_flags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)
        self.driver.get("https://ezwm.nfz.gov.pl/ap-zz/user/zz/welcome@default")

        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "FFFRAXownfz")))
        # select = self.driver.find_element(By.ID, "FFFRAXownfz")
        # all_options = select.find_elements(By.TAG_NAME, "option")
        # for option in all_options:
        #     if option.get_attribute("value") == "ael_szb8eOEsC5mPBpiesg--":
        #         option.click()
        #         break
        #
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "FFFRAXlogin")))
        # login = self.driver.find_element(By.NAME, "FFFRAXlogin")
        # login.send_keys(self.login)
        #
        # haslo = self.driver.find_element(By.NAME, "FFFRAXpasw")
        # haslo.send_keys(self.password)
        #
        # accept = self.driver.find_element(By.NAME, "sub1")
        # accept.click()

        # --------------------
        # self.target_under_limit = {"P.072.00.D":"798736","P.071.00.B":"798732","P.072.01.D":"798740"} old codes
        self.target_under_limit = {'O.01.01.01.B': '1903', 'O.01.02.00.D': '1895', 'O.01.02.01.D': '2632765', 'O.01.01.00.B': '1891'}
        # self.szajna_all = {"P.072.00.D":"661935","P.074.00.D1":"1909208","P.074.00.D":"1909164","P.071.00.B":"661893",
        #                    "P.073.00.B1":"1909233","P.073.00.B":"1909186","P.072.01.D":"661956","P.074.01.D1":"1909198",
        #                    "P.074.01.D":"1909153"} old codes
        self.szajna_all = {"O.01.01.01.B1":"2313", "O.01.02.00.D1":"2302", "O.01.02.00.D2":"2344",
                           "O.01.02.01.D2":"2336", "O.01.02.01.D1":"2632052", "O.01.01.00.B1":"2324",
                           "O.01.01.01.B2":"2371", "O.01.01.01.B":"1946", "O.01.02.00.D":"1920",
                           "O.01.02.01.D":"2632068", "O.01.01.00.B":"1907"}

        self.glass_codes = {'O.01.02.00.D3': '2808927', 'O.01.01.01.B3': '2808963', 'O.01.01.00.B3': '2808934',
                            'O.01.02.01.D.PR': '2632338', 'O.01.01.01.B.PR': '2632574', 'O.01.02.00.D.PR': '2632098',
                            'O.03.01': '2632030', 'O.01.01.00.B.PR': '2632279', 'O.01.02.01.D2.PR': '2632325',
                            'O.01.01.00.B2.PR': '2631965', 'O.01.02.00.D2.PR': '2632457', 'O.01.01.01.B': '2632405',
                            'O.01.02.01.D': '2632765', 'O.01.01.00.B2': '2632660', 'O.01.02.00.D1': '2632536',
                            'O.01.01.01.B1': '2632629', 'O.01.02.01.D1': '2632052', 'O.01.02.00.D': '2632079',
                            'O.01.01.01.B2': '2632809', 'O.01.02.01.D2': '2632459', 'O.01.01.01.B2.PR': '2632187',
                            'O.01.01.00.B1': '2632497', 'O.01.02.00.D2': '2632586', 'O.01.01.00.B': '2632108'}


    def select_on_begining(self):
        # if "https://ezwm.nfz.gov.pl/ap-zz/user/zz/pobrzlec" not in self.driver.current_url: # jeżeli jest na złej stronie
        #     raise ZeroDivisionError()

        self.current_person_num = self.driver.find_element(By.NAME, "nr_zlec").get_attribute("value")

        first_select = self.driver.find_element(By.ID, "select2-nrUmowyMiejSwd-container")
        first_select.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "select2-nrUmowyMiejSwd-results")))
        first_select_table = self.driver.find_element(By.ID, "select2-nrUmowyMiejSwd-results")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "select2-results__option--highlighted")))
        first_select_table.find_element(By.CLASS_NAME, "select2-results__option--highlighted").click()


        second_select = self.driver.find_element(By.ID, "select2-podstawaUbezpieczenia-container")
        second_select.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "select2-podstawaUbezpieczenia-results")))
        second_select_table = self.driver.find_element(By.ID, "select2-podstawaUbezpieczenia-results")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "select2-results__option--highlighted")))
        second_select_table.find_element(By.CLASS_NAME, "select2-results__option--highlighted").click()

        accept_prescription = self.driver.find_element(By.CLASS_NAME, "btn-edit")
        accept_prescription.click()

    def click_next_on_prescription(self):
        button_save = self.driver.find_element(By.CLASS_NAME, "btn-edit")
        button_save.click()

    def home_screen_after_adding_prescription(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Odśwież listę']")))

        for i in range(5):
            time.sleep(1)
            self.driver.refresh()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@value='Odśwież listę']")))
                realise = self.driver.find_element(By.XPATH, "//a[contains(text(),'realizuj')]")
            except:
                pass
            else:
                break

        realise = self.driver.find_element(By.XPATH, "//a[contains(text(),'realizuj')]")
        self.driver.get(realise.get_attribute("href"))

    def go_to_printing_view(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Odśwież listę']")))

        for i in range(5):
            time.sleep(1)
            self.driver.refresh()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "data")))
            first_row = self.driver.find_element(By.CLASS_NAME, "data")
            try:
                table = first_row.find_element(By.XPATH, "//td[contains(text(),'{0}')]".format(self.current_person_num))
                drop_down = first_row.find_element(By.CLASS_NAME, "dropdown-content")
                all_pages = drop_down.find_element(By.XPATH, "//a[contains(text(),'III i IV część')]")
            except:
                pass
            else:
                break

        first_row = self.driver.find_element(By.CLASS_NAME, "data")
        first_row.find_element(By.XPATH, "//*[contains(text(),'{0}')]".format(self.current_person_num))
        drop_down = first_row.find_element(By.CLASS_NAME, "dropdown-content")
        all_pages = drop_down.find_element(By.XPATH, "//a[contains(text(),'III i IV część')]")
        self.driver.get(all_pages.get_attribute("href"))

        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.NAME, "BUTX_NEXT")))
        button_next = self.driver.find_element(By.NAME, "BUTX_NEXT")
        button_next.click()

    def write_prescription(self):
        # if "https://ezwm.nfz.gov.pl/ap-zz/user/zz/wydanewyrmed" not in self.driver.current_url: # jeżeli jest na złej stronie
        #     raise ZeroDivisionError()

        tabelka = self.driver.find_element(By.CLASS_NAME, "tabnumber")
        dane_o_szklach = tabelka.find_elements(By.TAG_NAME, "tr")
        glasses_to_write = []

        for i, oko in enumerate(dane_o_szklach[1:]):
            oko = oko.find_elements(By.TAG_NAME, "td")
            kod_szkla = oko[1].accessible_name
            glasses_to_write.append((i,kod_szkla))

        for i, code in glasses_to_write:
            print(code)
            try:
                self.wpisz_szklo(i, code)
            except:
                print("Wystąpił błąd z {0} szkłem. Wypełnij sam {0} tabelkę".format(i + 1))

        self.wpisz_osobe_wydaj()


    def wpisz_osobe_wydaj(self):
        imie = self.driver.find_element(By.NAME, "imie")
        imie.send_keys(Keys.BACK_SPACE)
        imie.send_keys("Agnieszka")
        nazwisko = self.driver.find_element(By.NAME, "nazwisko")
        nazwisko.send_keys(Keys.BACK_SPACE)
        nazwisko.send_keys("Sobczyńska")

    def wpisz_szklo(self,szklo_z_kolei, kod_szkla_):
        numery_szkiel = self.glass_codes

        numery_tabelek = ["170", "480", "790", "1100"]

        if kod_szkla_ not in numery_szkiel:
            print("Szkło {0} nie w normie. Wypełnij {0} tabelę".format(szklo_z_kolei+1))
            return

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "select2-kodPrzedmDic{0}-container".format(szklo_z_kolei)))
        )
        wybor = self.driver.find_element(By.ID, "select2-kodPrzedmDic{0}-container".format(szklo_z_kolei))
        wybor.click()

        try:
            opcje_wyrob = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "select2-results__option--highlighted"))
            )
        except:
            raise NoSuchElementException()

        #opcje_wyrob = driver.find_element(By.ID, "select2-kodPrzedmDic{0}-results".format(szklo_z_kolei))
        opcje_wyrob.click()

        self.driver.find_element(By.ID, "select2-kodProdhanDic{0}-container".format(numery_tabelek[szklo_z_kolei])).click()
        try:
            wybor_produkt = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field"))
            )
        except:
            raise NoSuchElementException()

        wybor_produkt.send_keys(numery_szkiel[kod_szkla_])

        count = 0

        # to jest w miare dobre; muszę zawsze podświetlone zmieniać dlatego while
        while count < 2:
            try:
                count += 0.02
                podswietlone = self.driver.find_element(By.CLASS_NAME, "select2-results__option--highlighted")
            except:
                continue
            try:
                if podswietlone.find_element(By.CLASS_NAME,"label-info").text == str(numery_szkiel[kod_szkla_]):
                    break
            except:
                pass
            time.sleep(0.02)
            count += 0.02
        podswietlone.click()

        time.sleep(0.1)
        self.driver.find_elements(By.NAME, "lbWydSztuk")[szklo_z_kolei].send_keys("1")

    def accept_patient_data(self):
        button = self.driver.find_element(By.XPATH, "//*[contains(text(),'{0}')]".format("potwierdzam zgodność danych pacjenta"))
        button.click()

    def write_diff_person(self):
        diff_person = self.driver.find_element(By.XPATH, "//a[contains(text(),'inna osoba')]")
        diff_person.click()

        receiver_content = self.driver.find_element(By.ID,"odbiorOsoba")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "idOsoby")))

        diff_person_pesel = self.driver.find_element(By.ID, "idOsoby")
        diff_person_pesel.click()
        diff_person_pesel.send_keys(self.diff_receiver_pesel)

        diff_person_name = receiver_content.find_elements(By.NAME, "imie")[1]
        diff_person_name.click()
        diff_person_name.send_keys(self.diff_receiver_name)

        diff_person_surname = receiver_content.find_elements(By.NAME, "nazwisko")[1]
        diff_person_surname.click()
        diff_person_surname.send_keys(self.diff_receiver_surrname)

        self.diff_receiver_pesel = ""
        self.diff_receiver_name = ""
        self.diff_receiver_surrname = ""

