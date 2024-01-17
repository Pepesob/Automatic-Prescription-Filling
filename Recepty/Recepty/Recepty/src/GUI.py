import _tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading as th
from .Browser import Browser
import json
from .ConfigInfo import configInfo


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.browser:Browser = None
        self.title(f'{configInfo.name} {configInfo.version}')

        try:
            self.iconbitmap(r"src\resources\prescription_icon.ico")
        except _tkinter.TclError:
            print("\033[91m!!! Icon error !!!\033[00m")

        self.label = tk.Label(self, text='Recepty')

        self.manage_program = ttk.Label(self, text="Zarządzanie programem")
        self.manage_program.grid(row=0,column=0,padx=5,pady=2)
        self.manage_program1 = ttk.Label(self, text="Wypełnianie recept")
        self.manage_program1.grid(row=0, column=1, padx=5, pady=2)

        # buttons
        self.button_start = tk.Button(self, text='Rozpocznij działanie programu')
        self.button_start['command'] = self.start_program
        self.button_start.grid(row=1,column=0,padx=5,pady=2)

        self.button_fill_adv = tk.Button(self, text='Wypełnij całą receptę z tym samym odbiorcą')
        self.button_fill_adv['command'] = self.fill_prescription_same_receiver
        self.button_fill_adv['state'] = 'disabled'
        self.button_fill_adv.grid(row=2,column=1,padx=5,pady=2)

        self.button_fill = tk.Button(self, text='Wypełnij tylo formularz recepty')
        self.button_fill['command'] = self.fill_prescription
        self.button_fill['state'] = 'disabled'
        self.button_fill.grid(row=1, column=1, padx=5, pady=2)

        self.button_fill_diff = tk.Button(self, text="Wypełnij całą receptę z innym odbiorcą")
        self.button_fill_diff["command"] = self.take_diff_person_and_fill_presc
        self.button_fill_diff['state'] = 'disabled'
        self.button_fill_diff.grid(row=3, column=1, padx=5, pady=2)

        self.button_password_change = tk.Button(self, text='Zmień hasło')
        self.button_password_change['command'] = self.password_change_popup_window
        self.button_password_change.grid(row=2,column=0,padx=5,pady=2)

        self.button_quit = tk.Button(self, text='Zamknij program')
        self.button_quit['command'] = self.end_program
        self.button_quit.grid(row=3,column=0,padx=5,pady=2)

        # --------------------------------------------------------------------
        """
        self.button_temp = tk.Button(self, text='Wypełnij pierwsze okno')
        self.button_temp['command'] = self.temp
        self.button_temp.grid(row=0,column=2,padx=5,pady=2)

        self.button_temp2 = tk.Button(self, text='Domowe okno po wypisaniu recepty')
        self.button_temp2['command'] = self.temp2
        self.button_temp2.grid(row=1,column=2,padx=5,pady=2)

        self.button_temp3 = tk.Button(self, text='Domowe okno po dodaniu do realizacji')
        self.button_temp3['command'] = self.temp3
        self.button_temp3.grid(row=2,column=2,padx=5,pady=2)

        self.button_temp4 = tk.Button(self, text='Wypisz inne imie i nazwisko')
        self.button_temp4['command'] = self.temp4
        self.button_temp4.grid(row=3,column=2,padx=5,pady=2)
        """

    def disable_fill_buttons(self):
        self.button_fill_diff['state'] = 'disabled'
        self.button_fill['state'] = 'disabled'
        self.button_fill_adv['state'] = 'disabled'

    def enable_fill_buttons(self):
        self.button_fill_diff['state'] = 'active'
        self.button_fill['state'] = 'active'
        self.button_fill_adv['state'] = 'active'

    def temp(self):
        self.browser.select_on_begining()

    def temp2(self):
        self.browser.go_to_printing_view()

    def temp3(self):
        self.browser.home_screen_after_adding_prescription()

    def temp4(self):
        self.browser.diff_receiver_name = "Ania"
        self.browser.diff_receiver_surrname = "Kowalska"
        self.browser.diff_receiver_pesel = "12345678901"
        self.browser.write_diff_person()

    def fill_prescription(self):
        if self.browser is None:
            return


        def func2():
            self.disable_fill_buttons()

            try:
                self.browser.write_prescription()
                self.browser.accept_patient_data()
            except ZeroDivisionError: # jeśli driver nie jest na odpowieniej stronie
                print("\033[91m!!! Błąd w wypełnianiu recepty !!!\033[00m")
                messagebox.showinfo("Błąd", "Nieodpowiednia strona dla tej funkcji!")
                self.enable_fill_buttons()
                return
            except:
                print("\033[91m!!! Błąd w wypełnianiu recepty !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd przy wypełnianiu recepty!")
                self.enable_fill_buttons()
                return

            self.enable_fill_buttons()

        th.Thread(target=func2).start()


    def take_diff_person_and_fill_presc(self):
        def func():
            inp_name: str = input_name.get()
            inp_surname: str = input_surname.get()
            inp_pesel: str = input_pesel.get()

            if not inp_name.isalpha() and len(inp_name) == 0:
                print("\033[91m!!! Błąd w formacie imienia !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd w formacie imienia!")
                popup.destroy()
                return

            if not inp_surname.isalpha() and len(inp_surname) == 0:
                print("\033[91m!!! Błąd w formacie nazwiska !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd w formacie nazwiska!")
                popup.destroy()
                return

            if not inp_pesel.isnumeric() and len(inp_pesel) != 11:
                print("\033[91m!!! Błąd w formacie PESEL !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd w formacie PESEL!")
                popup.destroy()
                return

            self.browser.diff_receiver_name = inp_name
            self.browser.diff_receiver_surrname = inp_surname
            self.browser.diff_receiver_pesel = inp_pesel

            popup.destroy()
            self.fill_prescription_diff_receiver()

        popup = tk.Toplevel(self)
        popup.title("Wpisz dane innego odbiorcy")
        popup.minsize(250, 0)

        imie = ttk.Label(popup, text="Imie:")
        input_name = tk.Entry(popup)
        nazwisko = ttk.Label(popup, text="Nazwisko:")
        input_surname = tk.Entry(popup)
        pesel = ttk.Label(popup, text="PESEL:")
        input_pesel = tk.Entry(popup)

        imie.pack()
        input_name.pack()
        nazwisko.pack()
        input_surname.pack()
        pesel.pack()
        input_pesel.pack()

        input_button = tk.Button(popup, text='Akceptuj')
        input_button['command'] = func
        input_button.pack()

        popup.pack_slaves()


    def fill_prescription_diff_receiver(self):
        if self.browser is None:
            return

        def fuc():
            self.disable_fill_buttons()

            try:
                self.browser.select_on_begining()
            except ZeroDivisionError:
                print("\033[91m!!! Nieodpowiednia strona dla tej funkcji !!!\033[00m")
                messagebox.showinfo("Błąd", "Nieodpowiednia strona dla tej funkcji!")
                self.enable_fill_buttons()
                return
            except:
                print("\033[91m!!! Błąd na początku !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd na początku wypełniania!")
                self.enable_fill_buttons()
                return

            try:
                self.browser.home_screen_after_adding_prescription()
            except:
                print("\033[91m!!! Błąd z przejściem do okna recepty !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd z przejściem do okna recepty!")
                self.enable_fill_buttons()
                return

            try:
                self.browser.write_prescription()
                self.browser.write_diff_person()
                self.browser.click_next_on_prescription()
            except:
                print("\033[91m!!! Błąd w wypełnianiu recepty !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd w wypełnianiu recepty!")
                self.enable_fill_buttons()
                return

            try:
                self.browser.go_to_printing_view()
            except:
                print("\033[91m!!! Błąd przy przejściu do generowania pliku !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd przy przejściu do okna generowania pliku!")
                self.enable_fill_buttons()
                return
            
            self.enable_fill_buttons()

        th.Thread(target=fuc).start()


    def fill_prescription_same_receiver(self):
        if self.browser is None:
            return

        def fuc():
            self.disable_fill_buttons()

            try:
                self.browser.select_on_begining()
            except ZeroDivisionError:
                print("\033[91m!!! Nieodpowiednia strona dla tej funkcji !!!\033[00m")
                messagebox.showinfo("Błąd", "Nieodpowiednia strona dla tej funkcji!")
                self.enable_fill_buttons()
                return
            except:
                print("\033[91m!!! Błąd na początku !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd na początku wypełniania!")
                self.enable_fill_buttons()
                return

            try:
                self.browser.home_screen_after_adding_prescription()
            except:
                print("\033[91m!!! Błąd z przejściem do okna recepty !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd z przejściem do okna recepty!")
                self.enable_fill_buttons()
                return

            try:
                self.browser.write_prescription()
                self.browser.accept_patient_data()
                self.browser.click_next_on_prescription()
            except:
                print("\033[91m!!! Błąd w wypełnianiu recepty !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd w wypełnianiu recepty!")
                self.enable_fill_buttons()
                return

            try:
                self.browser.go_to_printing_view()
            except:
                print("\033[91m!!! Błąd przy przejściu do generowania pliku !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd przy przejściu do okna generowania pliku!")
                self.enable_fill_buttons()
                return

            self.enable_fill_buttons()

        th.Thread(target=fuc).start()

    def start_program(self):

        if self.browser is None:

            try:
                self.browser = Browser()

            except:
                print("\033[91m!!! Błąd przy uruchamianiu przeglądarki  !!!\033[00m")
                messagebox.showinfo("Błąd", "Błąd przy uruchamianiu przeglądarki!")
            self.button_start.config(text="Wyłącz przeglądarkę")
            self.enable_fill_buttons()
        else:
            try:
                self.browser.driver.quit()
            finally:
                self.browser = None
                self.button_start.config(text="Rozpocznij działanie programu")
                self.disable_fill_buttons()


    def end_program(self):
        if self.browser is not None:
            try:
                self.browser.driver.quit()
            finally:
                pass
        self.destroy()
        quit()

    def password_change_popup_window(self):
        def func():
            new_password = input_password.get()
            with open("src/resources/data.json","r") as f:
                json_data = json.load(f)
            json_data["password"] = new_password
            with open("src/resources/data.json","w") as f:
                json.dump(json_data,f,indent=1)
            popup.destroy()

        popup = tk.Toplevel(self)
        popup.title("Zmiana hasła")
        popup.geometry("300x50")

        input_password = tk.Entry(popup)
        input_password.pack()

        input_button = tk.Button(popup, text='Akceptuj')
        input_button['command'] = func
        input_button.pack()


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
