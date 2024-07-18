import src

if __name__ == "__main__":
    print(f"{src.configInfo.name} (wersja {src.configInfo.version})")
    app = src.GUI()
    app.mainloop()
