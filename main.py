from gui import App


def main():
    """The main function of the program"""
    app = App()

    app.title("Turtle Race")
    app.resizable(width=False, height=False)

    app.mainloop()


if __name__ == "__main__":
    main()
