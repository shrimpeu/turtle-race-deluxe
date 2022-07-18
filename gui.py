import tkinter as tk
import turtle
import random

from tkinter import messagebox

from config import *
from helpers import *


class App(tk.Tk):
    """
    The main root of the app interface. The class that controls the interface/pages.

    Attributes:
        self.root (tk.Frame): instance of main frame
        self.frames (dict): dictionary of frames that the root will control to navigate through pages
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default=APP_LOGO)

        self.root = tk.Frame(self)
        self.root.pack(side="top", fill="both", expand=True)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.geometry("804x606")

        self.frames = {}

        for F in {StartPage, SignInPage, SignUpPage}:
            frame = F(self.root, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_main_page(self, email=None):
        frame = MainPage(self.root, self, email)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class StartPage(tk.Frame):
    """
    The class that displays the start page of the app

    Args:
        parent (tk.Frame): the root interface that will controll this frame class
        controller (tk.Tk): the App class
    
    Attributes:
        logo (tk.PhotoImage): imports the app logo GIF file from assets folder
        lb_logo (tk.Label): places the logo in frame as label widget
        lb_title (tk.Label): places the title of the app as label widget
        btn_signup (tk.Button): button widget to navigate SignUpPage frame
        btn_signin (tk.Button): button widget to navigate SignInPage frame
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=120, pady=20, bg=BG_1)

        self.logo = tk.PhotoImage(file="assets/logo.gif")
        self.lb_logo = tk.Label(self, image=self.logo, bg=BG_1)
        self.lb_logo.pack(padx=100, pady=(30, 10))

        self.lb_title = tk.Label(self, text=TITLE, font=SUBTITLE_FONT, fg=TITLE_FG, bg=BG_1)
        self.lb_title.pack(padx=100, pady=30)

        self.btn_signup = tk.Button(self, text="Sign up", font=NORMAL_FONT, fg=BUTTON_FG, bg=BUTTON_BG, command=lambda: controller.show_frame(SignUpPage),)
        self.btn_signup.pack(padx=40, pady=5, fill="both")

        self.btn_signin = tk.Button(self, text="Sign In", font=NORMAL_FONT, fg=BUTTON_FG, bg=BUTTON_BG, command=lambda: controller.show_frame(SignInPage),)
        self.btn_signin.pack(padx=40, pady=5, fill="both")


class SignUpPage(tk.Frame):
    """
    The class that displays the sign up page of the App.

    Args:
        parent (tk.Frame): the root interface that will controll this frame class
        controller (tk.Tk): the App class
    
    Attributes:
        entry_firstname (tk.Entry): entry widget that receives the first name of the user.
        entry_lastname (tk.Entry): entry widget that receives the last name of the user.
        entry_email (tk.Entry): entry widget that receives the email of the user.
        entry_passwd (tk.Entry): entry widget that receives the password created by the user.
        entry_repasswd (tk.Entry): entry widget that receives the re-typed password created by the user.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=100, pady=120, bg=BG_1)

        #----- Label widgets -----#
        lb_title = tk.Label(self, text="Sign up", width=20, height=1, font=SUBTITLE_FONT, bg=BG_1, fg=TITLE_FG, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        lb_firstname = tk.Label(self, text="First name:", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_firstname.grid(column=0, row=1, pady=(0, 10), padx=(0, 5))

        lb_lastname = tk.Label(self, text="Last name:", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_lastname.grid(column=0, row=2, pady=(0, 10), padx=(0, 5))

        lb_email = tk.Label(self, text="Email:", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_email.grid(column=0, row=3, pady=(0, 10), padx=(0, 5))

        lb_passwd = tk.Label(self, text="Create password:", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_passwd.grid(column=0, row=4, pady=(20, 10), padx=(0, 5))

        lb_repasswd = tk.Label(self, text="Re-type password:", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_repasswd.grid(column=0, row=5, pady=(0, 10), padx=(0, 5))

        #----- Entry widgets -----#
        self.entry_firstname = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=ENTRY_FG, bg=ENTRY_BG, font=NORMAL_FONT, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_firstname.grid(column=1, row=1, columnspan=2, pady=(0, 10))

        self.entry_lastname = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=ENTRY_FG, bg=ENTRY_BG, font=NORMAL_FONT, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_lastname.grid(column=1, row=2, columnspan=2, pady=(0, 10))

        self.entry_email = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=ENTRY_FG, bg=ENTRY_BG, font=NORMAL_FONT, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_email.grid(column=1, row=3, columnspan=2, pady=(0, 10))

        self.entry_passwd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=ENTRY_FG, bg=ENTRY_BG, font=NORMAL_FONT, show="*", highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_passwd.grid(column=1, row=4, columnspan=2, pady=(20, 10))

        self.entry_repasswd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=ENTRY_FG, bg=ENTRY_BG, font=NORMAL_FONT, show="*", highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_repasswd.grid(column=1, row=5, columnspan=2, pady=(0, 10))

        #----- Create button widgets -----#
        btn_create_account = tk.Button(self, text="Create Account", font=NORMAL_FONT, fg=BUTTON_FG, bg=BUTTON_BG, command=lambda: controller.show_frame(StartPage) if self.valid_credentials() else None,)
        btn_create_account.grid(column=1, row=6, columnspan=2, pady=(10, 0), sticky="NESW")

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=BUTTON_FG, bg=BUTTON_BG, command=lambda: controller.show_frame(StartPage),)
        btn_cancel.grid(column=0, row=6, pady=(10, 0), padx=(0, 5), sticky="NESW")

    def valid_credentials(self) -> bool:
        """Check all user inputs if they are valid and stores them in user_data if True"""
        entries = (self.entry_firstname, self.entry_lastname, self.entry_email,
                   self.entry_passwd, self.entry_repasswd)

        if self.input_not_empty():
            input_firstname = self.entry_firstname.get()
            input_lastname = self.entry_lastname.get()
            input_email = self.entry_email.get().encode("utf-8")
            input_passwd = self.entry_passwd.get()
            input_rpasswd = self.entry_repasswd.get()

            if email_taken(input_email):
                messagebox.showwarning(title="Invalid Credentials", message="Email already in use.")
                return False
            else:
                input_email = hash_str(input_email)
                if input_passwd == input_rpasswd:
                    add_new_account(input_email, input_firstname, input_lastname, input_passwd)
                    for e in entries:
                        e.delete(0, tk.END)
                    return True
                else:
                    messagebox.showwarning(title="Invalid Input", message="Password do not match.")
            return False
        else:
            messagebox.showwarning(title="Invalid Credentials", message="Empty input!")

    def input_not_empty(self) -> bool:
        """Checks all the entries if they are empty."""
        entries = (self.entry_firstname.get(), self.entry_lastname.get(), self.entry_email.get(),
                   self.entry_passwd.get(), self.entry_repasswd.get())

        for e in entries:
            if len(e) == 0:
                return False
        return True


class SignInPage(tk.Frame):
    """
    The class that displays the sign in page of the App.

    Args:
        parent (tk.Frame): the root interface that will controll this frame class
        controller (tk.Tk): the App class
    
    Attributes:
        entry_email (tk.Entry): entry widget that receives the email of the user.
        entry_passwd (tk.Entry): entry widget that receives the password created by the user.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=100, pady=100, bg=BG_1)

        #----- Label widgets -----#
        lb_title = tk.Label(self, text="Sign in", width=20, height=2, font=SUBTITLE_FONT, bg=BG_1, fg=TITLE_FG, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        lb_email = tk.Label(self, text="Email: ", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_email.grid(column=0, row=1, pady=(0, 10), padx=(0, 5))

        lb_passwd = tk.Label(self, text="Password: ", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_passwd.grid(column=0, row=2, pady=(0, 10), padx=(0, 5))

        #----- Entry widgets -----#
        self.entry_email = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=ENTRY_FG, bg=ENTRY_BG, font=NORMAL_FONT, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_email.grid(column=1, row=1, columnspan=2, pady=(0, 10))

        self.entry_passwd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=ENTRY_FG, bg=ENTRY_BG, font=NORMAL_FONT, show="*", highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_passwd.grid(column=1, row=2, columnspan=2, pady=(0, 10))

        #----- Button widgets -----#
        btn_signin = tk.Button(self, text="Sign in", font=NORMAL_FONT, fg=BUTTON_FG, bg=BUTTON_BG, command=lambda: controller.show_main_page(self.entry_email.get()) if self.valid_credentials() else None,)
        btn_signin.grid(column=1, row=3, columnspan=2, pady=(10, 0), sticky="NESW")

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=BUTTON_FG, bg=BUTTON_BG, command=lambda: controller.show_frame(StartPage),)
        btn_cancel.grid(column=0, row=3, pady=(10, 0), padx=(0, 5), sticky="NESW")

    def valid_credentials(self) -> bool:
        """Checks the entered email and password are correct by looking at user_data JSON file"""
        input_email = self.entry_email.get().encode("utf-8")
        input_passwd = self.entry_passwd.get().encode("utf-8")

        if email_taken(input_email):
            input_email = get_existing_email(input_email)
            email_passwd = EXISTING_ACCOUNTS[input_email]["pword"].encode("utf-8")
            if bcrypt.checkpw(input_passwd, email_passwd):
                return True
            else:
                messagebox.showwarning(title="Invalid Credentials", message="Invalid password.")
        else:
            messagebox.showwarning(title="Invalid Credentials", message="Email is not yet registered. Try signing up first.")


class MainPage(tk.Frame):
    def __init__(self, parent, controller, email):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1)

        # Get info from email that has been logged in
        for e in EXISTING_ACCOUNTS:
            if bcrypt.checkpw(email.encode("utf-8"), e.encode("utf-8")):
                f_name = EXISTING_ACCOUNTS[e]["first_name"]
                l_name = EXISTING_ACCOUNTS[e]["last_name"]
                self.balance = EXISTING_ACCOUNTS[e]["balance"]
                self.email = e

        # Set canvas for turtle section
        self.canvas = tk.Canvas(self, width=760, height=400, bg="black")
        self.canvas.grid(column=0, row=0, columnspan=8, pady=(0, 20))

        self.turtle_section = turtle.TurtleScreen(self.canvas)
        self.turtle_section.bgpic("assets/turtle_bg.gif")

        # Initialize turtles
        self.rturtle = turtle.RawTurtle(self.turtle_section)
        self.gturtle = turtle.RawTurtle(self.turtle_section)
        self.bturtle = turtle.RawTurtle(self.turtle_section)
        self.yturtle = turtle.RawTurtle(self.turtle_section)
        self.oturtle = turtle.RawTurtle(self.turtle_section)

        self.turtles = [[self.rturtle, "red", "R"], [self.gturtle, "green", "G"], [self.bturtle, "blue", "B"],
                        [self.yturtle, "yellow", "Y"], [self.oturtle, "orange", "O"]]
        self.turtle_ypos = [50, 0, -50, -100, -150]

        # Set turtles in their position
        self.set_turtles()

        #----- Labels - Account info -----#
        self.total_bet = 0
        self.total_bet_str = tk.StringVar()
        self.total_bet_str.set(f"Total Bet: {self.total_bet}")

        lb_total_bet = tk.Label(self, textvariable=self.total_bet_str, height=1, font=NORMAL_FONT, anchor="w", relief=tk.SUNKEN, fg=TITLE_FG, bg=BUTTON_BG)
        lb_total_bet.grid(column=6, row=1, padx=(5, 0), pady=(0, 5), sticky="NESW")

        self.balance_str = tk.StringVar()
        self.balance_str.set(f"Balance: Php {self.balance}")

        lb_user_balance = tk.Label(self, textvariable=self.balance_str, height=1, font=NORMAL_FONT, anchor="center", relief=tk.SUNKEN, fg=TITLE_FG, bg=BUTTON_BG)
        lb_user_balance.grid(column=6, row=2, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW")

        lb_user_name = tk.Label(self, text=f"Name: {f_name[:30]}. {l_name[:1]}.", height=1, font=NORMAL_FONT, anchor="w", relief=tk.SUNKEN, fg=TITLE_FG, bg=BUTTON_BG)
        lb_user_name.grid(column=7, row=1, padx=(5, 0), pady=(0, 5), sticky="NESW")

        #----- 1st Column -----#
        lb_RO = tk.Label(self, text=" R-O ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_RO.grid(column=0, row=1, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_GO = tk.Label(self, text=" G-O ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_GO.grid(column=0, row=2, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_BO = tk.Label(self, text=" B-O ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_BO.grid(column=0, row=3, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_YO = tk.Label(self, text=" Y-O ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_YO.grid(column=0, row=4, padx=(0, 5), sticky="NESW")

        #----- 2nd column -----#
        self.input_bet_RO = tk.IntVar()
        self.input_bet_RO.set(0)

        self.input_bet_GO = tk.IntVar()
        self.input_bet_GO.set(0)

        self.input_bet_BO = tk.IntVar()
        self.input_bet_BO.set(0)

        self.input_bet_YO = tk.IntVar()
        self.input_bet_YO.set(0)

        entry_bet_RO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RO,)
        entry_bet_RO.grid(column=1, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_GO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GO,)
        entry_bet_GO.grid(column=1, row=2, pady=(0, 5), sticky="NESW")

        entry_bet_BO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_BO,)
        entry_bet_BO.grid(column=1, row=3, pady=(0, 5), sticky="NESW")

        entry_bet_YO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_YO,)
        entry_bet_YO.grid(column=1, row=4, sticky="NESW")

        #----- 3rd Column -----#
        lb_RY = tk.Label(self, text=" R-Y ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_RY.grid(column=2, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_GY = tk.Label(self, text=" G-Y ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_GY.grid(column=2, row=2, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_BY = tk.Label(self, text=" B-Y ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_BY.grid(column=2, row=3, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_GB = tk.Label(self, text=" G-B ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_GB.grid(column=2, row=4, padx=(5, 5), sticky="NESW")

        #----- 4th column -----#
        self.input_bet_RY = tk.IntVar()
        self.input_bet_RY.set(0)

        self.input_bet_GY = tk.IntVar()
        self.input_bet_GY.set(0)

        self.input_bet_BY = tk.IntVar()
        self.input_bet_BY.set(0)

        self.input_bet_GB = tk.IntVar()
        self.input_bet_GB.set(0)

        entry_bet_RY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RY,)
        entry_bet_RY.grid(column=3, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_GY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GY,)
        entry_bet_GY.grid(column=3, row=2, pady=(0, 5), sticky="NESW")

        entry_bet_BY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_BY,)
        entry_bet_BY.grid(column=3, row=3, pady=(0, 5), sticky="NESW")

        entry_bet_GB = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GB,)
        entry_bet_GB.grid(column=3, row=4, sticky="NESW")

        #----- 5th Column -----#
        lb_RB = tk.Label(self, text=" R-B ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_RB.grid(column=4, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_RG = tk.Label(self, text=" R-G ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG)
        lb_RG.grid(column=4, row=2, padx=(5, 5), pady=(0, 5), sticky="NESW")

        #----- 6th column -----#
        self.input_bet_RB = tk.IntVar()
        self.input_bet_RB.set(0)

        self.input_bet_RG = tk.IntVar()
        self.input_bet_RG.set(0)

        entry_bet_RB = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RB,)
        entry_bet_RB.grid(column=5, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_RG = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RG,)
        entry_bet_RG.grid(column=5, row=2, pady=(0, 5), sticky="NESW")

        #----- USER INPUT LIST -----#
        self.all_bets = [
            self.input_bet_RO, self.input_bet_GO, self.input_bet_BO, self.input_bet_YO,
            self.input_bet_RY, self.input_bet_GY, self.input_bet_BY, self.input_bet_GB,
            self.input_bet_RB, self.input_bet_RG]

        #----- Buttons -----#

        # Game start button
        btn_start = tk.Button(self, text="Start Game", font=NORMAL_FONT, command=self.start_race, height=1, fg=TITLE_FG, bg="white")
        btn_start.grid(column=4, row=3, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW",)
        # Reset bet button
        btn_reset_bet = tk.Button(self, text="Reset Bet", font=NORMAL_FONT, command=self.reset_bet, height=1, fg=TITLE_FG, bg="white")
        btn_reset_bet.grid(column=4, row=4, columnspan=2, padx=(5, 0), sticky="NESW")
        # Deposite Button
        btn_deposit = tk.Button(self, text="Deposit", font=NORMAL_FONT, command=self.show_DepositPage, height=1, fg=TITLE_FG, bg="white")
        btn_deposit.grid(column=6, row=3, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW",)
        # Withdraw Button
        btn_withdraw = tk.Button(self, text="Withdraw", font=NORMAL_FONT, command=self.show_WithdrawPage, height=1, fg=TITLE_FG, bg="white")
        btn_withdraw.grid(column=7, row=4, padx=(5, 0), sticky="NESW")
        # Log out Button
        btn_logout = tk.Button(self, text="Log out", font=NORMAL_FONT, command=lambda: controller.show_frame(StartPage), height=1, fg="red", bg="white")
        btn_logout.grid(column=6, row=4, padx=(5, 0), sticky="NESW")

    def set_turtles(self) -> None:
        for t in self.turtles:
            self.turtle_section.addshape(f"assets/t_{t[1]}.gif")
            t[0].shape(f"assets/t_{t[1]}.gif")
            t[0].shapesize(2)
            t[0].pencolor(t[1])
            t[0].penup()
            t[0].goto(x=-300, y=self.turtle_ypos[self.turtles.index(t)])
            t[0].pendown()

    def start_race(self) -> None:
        self.compute_bets()
        turtles = self.turtles

        if self.total_bet != 0:
            winners = "-"
            while len(winners) != 3:
                for t in turtles:
                    if t[0].xcor() >= 278:
                        if len(winners) == 2:
                            winners = winners + t[2]
                        else:
                            winners = t[2] + winners
                        turtles.remove(t)
                    else:
                        t[0].forward(random.randint(1, 5))
                
            messagebox.showinfo(title="Game Result", message=f"WINNERS: {winners}")

    def compute_bets(self) -> int:
        for bet in self.all_bets:
            bet = bet.get()
            if bet == "":
                bet = 0
            self.total_bet += bet

        if self.total_bet > self.balance:
            messagebox.showwarning(title="Invalid Input", message="Insufficient balance.")
            self.total_bet = 0
            return None
        elif self.total_bet == 0:
            messagebox.showwarning(title="Invalid Input", message="Hey, bet something!")
            self.total_bet = 0
            return None
        else:
            self.total_bet_str.set(f"Total Bet: Php {self.total_bet}")
            self.reset_bet()

    def show_DepositPage(self):
        deposit_page = DepositPage(self.email,  self.balance_str)
        deposit_page.title("Deposit thru Paypal")
        deposit_page.resizable(width=False, height=False)
        deposit_page.mainloop()

    def show_WithdrawPage(self):
        withdraw_page = WithdrawPage(self.email, self.balance_str)
        withdraw_page.title("Withdraw")
        withdraw_page.resizable(width=False, height=False)
        withdraw_page.mainloop()

    def reset_bet(self):
        for bet in self.all_bets:
            bet.set(0)


class DepositPage(tk.Toplevel):
    def __init__(self, email, balance_str, *args, **kwargs):
        tk.Toplevel.__init__(self, bg=BG_1 ,*args, **kwargs)

        self.email = email
        self.balance_str = balance_str

        self.logo = tk.PhotoImage(file="assets/paypal.gif")
        self.lb_logo = tk.Label(self, image=self.logo, bg=BG_1)
        self.lb_logo.pack(padx=20, pady=30)

        lb_title = tk.Label(self, text="Deposit", font=SUBTITLE_FONT, anchor="center", fg=TITLE_FG, bg=BG_1)
        lb_title.pack(padx=20, pady=10)

        lb_amount = tk.Label(self, text="Amount (min: Php 100)", font=NORMAL_FONT, anchor="center", bg=BG_1)
        lb_amount.pack(padx=20, pady=(0, 5))

        self.entry_amount = tk.Entry(self, width=30, font=NORMAL_FONT, borderwidth=2, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_amount.pack(padx=20)

        lb_signinp_title = tk.Label(self, text="Sign in to Paypal", font=NORMAL_FONT, anchor="center", fg=TITLE_FG , bg=BG_1)
        lb_signinp_title.pack(padx=20, pady=(30, 5))

        lb_paypal_email = tk.Label(self, text="Email", font=NORMAL_FONT, anchor="w", bg=BG_1)
        lb_paypal_email.pack(padx=20, pady=(5, 5))

        self.entry_paypal_email = tk.Entry(self, width=30, font=NORMAL_FONT, borderwidth=2, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_paypal_email.pack(padx=20, pady=(0, 10))

        lb_paypal_pw = tk.Label(self, text="Password", font=NORMAL_FONT, anchor="w", bg=BG_1)
        lb_paypal_pw.pack(padx=20, pady=(0, 5))

        self.entry_paypal_pw = tk.Entry(self, width=30, font=NORMAL_FONT, borderwidth=2, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL, show="*")
        self.entry_paypal_pw.pack(padx=20, pady=(0, 20))

        btn_confirm = tk.Button(self, text="Confirm", font=NORMAL_FONT, command=self.confirm_deposit, fg=TITLE_FG, bg="white")
        btn_confirm.pack(padx=20, pady=(0, 20), fill="both")


    def confirm_deposit(self):
        balance = curr_balance(self.email)
        entries = (self.entry_paypal_email.get(), self.entry_paypal_pw.get())
        entry_amount = int(self.entry_amount.get())
        if valid_amount(self, "deposit", entry_amount, balance) and \
            input_not_empty(self, entries):
            balance += entry_amount
            update_balance(self.email, balance)
            self.balance_str.set(f"Balance: Php {balance}")
            self.destroy()


class WithdrawPage(tk.Toplevel):
    def __init__(self, email, balance_str, *args, **kwargs):
        tk.Toplevel.__init__(self, bg=BG_1,*args, **kwargs)

        self.email = email
        self.balance_str = balance_str

        self.logo = tk.PhotoImage(file="assets/paypal.gif")
        self.lb_logo = tk.Label(self, image=self.logo, bg=BG_1)
        self.lb_logo.pack(padx=20, pady=30)

        lb_title = tk.Label(self, text="Withdraw", font=SUBTITLE_FONT, anchor="center", fg=TITLE_FG, bg=BG_1)
        lb_title.pack(padx=20, pady=10)

        lb_amount = tk.Label(self, text="Amount (min: Php 300)", font=NORMAL_FONT, anchor="center", bg=BG_1)
        lb_amount.pack(padx=20, pady=(0, 5))

        self.entry_amount = tk.Entry(self, width=30, font=NORMAL_FONT, borderwidth=2, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_amount.pack(padx=20)

        lb_signinp_title = tk.Label(self, text="Sign in to Paypal", font=NORMAL_FONT, anchor="center", fg=TITLE_FG , bg=BG_1)
        lb_signinp_title.pack(padx=20, pady=(30, 5))

        lb_paypal_email = tk.Label(self, text="Email", font=NORMAL_FONT, anchor="w", bg=BG_1)
        lb_paypal_email.pack(padx=20, pady=(5, 5))

        self.entry_paypal_email = tk.Entry(self, width=30, font=NORMAL_FONT, borderwidth=2, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL)
        self.entry_paypal_email.pack(padx=20, pady=(0, 10))

        lb_paypal_pw = tk.Label(self, text="Password", font=NORMAL_FONT, anchor="w", bg=BG_1)
        lb_paypal_pw.pack(padx=20, pady=(0, 5))

        self.entry_paypal_pw = tk.Entry(self, width=30, font=NORMAL_FONT, borderwidth=2, highlightthickness=2, highlightcolor=BORDER_FILL, highlightbackground=BORDER_FILL, show="*")
        self.entry_paypal_pw.pack(padx=20, pady=(0, 20))

        btn_confirm = tk.Button(self, text="Confirm", font=NORMAL_FONT, command=self.confirm_withdraw, fg=TITLE_FG, bg="white")
        btn_confirm.pack(padx=20, pady=(0, 20), fill="both")
    
    def confirm_withdraw(self):
        balance = curr_balance(self.email)
        entries = (self.entry_paypal_email.get(), self.entry_paypal_pw.get())
        entry_amount = int(self.entry_amount.get())
        if valid_amount(self, "withdraw", entry_amount, balance) and \
            input_not_empty(self, entries):
            balance -= entry_amount
            update_balance(self.email, balance)
            self.balance_str.set(f"Balance: Php {balance}")
            self.destroy()
