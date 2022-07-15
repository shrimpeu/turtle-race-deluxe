import tkinter as tk
import turtle

from tkinter import messagebox

from config import *
from helpers import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.root = tk.Frame(self)
        self.root.pack(side="top", fill="both", expand=True)

        # 0 = minimum
        # Weight = priority
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in {StartPage, SignInPage, SignUpPage}:
            frame = F(self.root, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):  # cont = controller
        frame = self.frames[cont]
        frame.tkraise()

    def show_main_page(self, email=None):
        frame = MainPage(self.root, self, email)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1)

        lb_title = tk.Label(self, text=TITLE, font=LARGE_FONT, fg=FG_1, bg=BG_1)
        lb_title.pack(padx=20, pady=20)

        btn_signup = tk.Button(self, text="Sign up", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(SignUpPage),)
        btn_signup.pack(padx=40, pady=5, fill="both")

        btn_signin = tk.Button(self, text="Sign In", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(SignInPage),)
        btn_signin.pack(padx=40, pady=5, fill="both")


class SignUpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1, relief=tk.SUNKEN)

        #----- Label widgets -----#
        lb_title = tk.Label(self, text="Sign up", width=20, height=1, font=LARGE_FONT, bg=BG_1, fg=FG_1, anchor="center",)
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
        self.entry_firstname = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT,)
        self.entry_firstname.grid(column=1, row=1, columnspan=2, pady=(0, 10))

        self.entry_lastname = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT,)
        self.entry_lastname.grid(column=1, row=2, columnspan=2, pady=(0, 10))

        self.entry_email = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT,)
        self.entry_email.grid(column=1, row=3, columnspan=2, pady=(0, 10))

        self.entry_passwd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT, show="*",)
        self.entry_passwd.grid(column=1, row=4, columnspan=2, pady=(20, 10))

        self.entry_repasswd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT, show="*",)
        self.entry_repasswd.grid(column=1, row=5, columnspan=2, pady=(0, 10))

        self.entries = (self.entry_firstname.get(), self.entry_lastname.get(), self.entry_email.get(),
                   self.entry_passwd.get(), self.entry_repasswd.get())

        #----- Create button widgets -----#
        btn_create_account = tk.Button(self, text="Create Account", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(StartPage) if self.valid_credentials() else None,)
        btn_create_account.grid(column=1, row=6, columnspan=2, pady=(10, 0), sticky="NESW")

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(StartPage),)
        btn_cancel.grid(column=0, row=6, pady=(10, 0), padx=(0, 5), sticky="NESW")

    def valid_credentials(self) -> bool:
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
                    input_passwd = hash_str(input_passwd.encode("utf-8"))

                    EXISTING_ACCOUNTS[input_email] = {
                            "first_name": input_firstname,
                            "last_name": input_lastname,
                            "pword": input_passwd,
                            "balance": 0
                            }
                    write_json(EXISTING_ACCOUNTS)

                    for e in entries:
                        e.delete(0, tk.END)

                    messagebox.showinfo(title="Account Created", message="Account successfully created!")    
                    return True
                else:
                    messagebox.showwarning(title="Invalid Input", message="Password do not match.")
            return False
        else:
            messagebox.showwarning(title="Invalid Credentials", message="Empty input!")

    def input_not_empty(self) -> bool:
        entries = (self.entry_firstname.get(), self.entry_lastname.get(), self.entry_email.get(),
                   self.entry_passwd.get(), self.entry_repasswd.get())

        for e in entries:
            if len(e) == 0:
                return False
        return True


class SignInPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1, relief=tk.SUNKEN)

        self.email = tk.StringVar()

        #----- Label widgets -----#
        lb_title = tk.Label(self, text="Sign in", width=20, height=1, font=LARGE_FONT, bg=BG_1, fg=FG_1, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        lb_email = tk.Label(self, text="Email: ", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_email.grid(column=0, row=1, pady=(0, 10), padx=(0, 5))

        lb_passwd = tk.Label(self, text="Password: ", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_passwd.grid(column=0, row=2, pady=(0, 10), padx=(0, 5))

        #----- Entry widgets -----#
        self.entry_email = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT, textvariable=self.email)
        self.entry_email.grid(column=1, row=1, columnspan=2, pady=(0, 10))

        self.entry_passwd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT, show="*",)
        self.entry_passwd.grid(column=1, row=2, columnspan=2, pady=(0, 10))

        #----- Button widgets -----#
        btn_signin = tk.Button(self, text="Sign in", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_main_page(self.email.get()) if self.valid_credentials() else None,)
        btn_signin.grid(column=1, row=3, columnspan=2, pady=(10, 0), sticky="NESW")

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(StartPage),)
        btn_cancel.grid(column=0, row=3, pady=(10, 0), padx=(0, 5), sticky="NESW")

    def valid_credentials(self) -> bool:
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
        tk.Frame.__init__(self, parent, padx=20, pady=20)

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

        turtle_section = turtle.TurtleScreen(self.canvas)
        turtle_section.bgcolor("black")

        # Initialize turtles
        self.rturtle = turtle.RawTurtle(turtle_section)
        self.gturtle = turtle.RawTurtle(turtle_section)
        self.bturtle = turtle.RawTurtle(turtle_section)
        self.yturtle = turtle.RawTurtle(turtle_section)
        self.oturtle = turtle.RawTurtle(turtle_section)

        self.turtles = [[self.rturtle, "red", "R"], [self.gturtle, "green", "G"], [self.bturtle, "blue", "B"],
                        [self.yturtle, "yellow", "Y"], [self.oturtle, "orange", "O"]]
        self.turtle_ypos = [50, 0, -50, -100, -150]

        # Set turtles in their position
        self.set_turtles()

        #----- Labels - Account info -----#
        self.total_bet = 0
        self.total_bet_str = tk.StringVar()
        self.total_bet_str.set(f"Total Bet: {self.total_bet}")

        lb_total_bet = tk.Label(self, textvariable=self.total_bet_str, heigh=1, font=NORMAL_FONT, anchor="w")
        lb_total_bet.grid(column=6, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")

        self.balance_str = tk.StringVar()
        self.balance_str.set(f"Balance: {self.balance}")

        lb_user_balance = tk.Label(self, textvariable=self.balance_str, heigh=1, font=NORMAL_FONT, anchor="w",)
        lb_user_balance.grid(column=6, row=2, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_user_name = tk.Label(self, text=f"Name: {f_name[:30]}. {l_name[:1]}.", heigh=1, font=NORMAL_FONT, anchor="w",)
        lb_user_name.grid(column=7, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")

        #----- 1st Column -----#
        lb_RO = tk.Label(self, text=" R-O ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_RO.grid(column=0, row=1, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_GO = tk.Label(self, text=" G-O ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_GO.grid(column=0, row=2, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_BO = tk.Label(self, text=" B-O ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_BO.grid(column=0, row=3, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_YO = tk.Label(self, text=" Y-O ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
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

        entry_bet_RO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RO)
        entry_bet_RO.grid(column=1, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_GO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GO)
        entry_bet_GO.grid(column=1, row=2, pady=(0, 5), sticky="NESW")

        entry_bet_BO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_BO)
        entry_bet_BO.grid(column=1, row=3, pady=(0, 5), sticky="NESW")

        entry_bet_YO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_YO)
        entry_bet_YO.grid(column=1, row=4, sticky="NESW")

        #----- 3rd Column -----#
        lb_RY = tk.Label(self, text=" R-Y ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_RY.grid(column=2, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_GY = tk.Label(self, text=" G-Y ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_GY.grid(column=2, row=2, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_BY = tk.Label(self, text=" B-Y ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_BY.grid(column=2, row=3, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_GB = tk.Label(self, text=" G-B ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
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

        entry_bet_RY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RY)
        entry_bet_RY.grid(column=3, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_GY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GY)
        entry_bet_GY.grid(column=3, row=2, pady=(0, 5), sticky="NESW")

        entry_bet_BY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_BY)
        entry_bet_BY.grid(column=3, row=3, pady=(0, 5), sticky="NESW")

        entry_bet_GB = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GB)
        entry_bet_GB.grid(column=3, row=4, sticky="NESW")

        #----- 5th Column -----#
        lb_RB = tk.Label(self, text=" R-B ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_RB.grid(column=4, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_RG = tk.Label(self, text=" R-G ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_RG.grid(column=4, row=2, padx=(5, 5), pady=(0, 5), sticky="NESW")

        #----- 6th column -----#
        self.input_bet_RB = tk.IntVar()
        self.input_bet_RB.set(0)

        self.input_bet_RG = tk.IntVar()
        self.input_bet_RG.set(0)

        entry_bet_RB = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RB)
        entry_bet_RB.grid(column=5, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_RG = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RG)
        entry_bet_RG.grid(column=5, row=2, pady=(0, 5), sticky="NESW")

        #----- USER INPUT LIST -----#
        self.all_bets = [
            self.input_bet_RO, self.input_bet_GO, self.input_bet_BO, self.input_bet_YO,
            self.input_bet_RY, self.input_bet_GY, self.input_bet_BY, self.input_bet_GB,
            self.input_bet_RB, self.input_bet_RG]

        #----- Buttons -----#

        # Game start button
        btn_start = tk.Button(self, text="Start Game", font=NORMAL_FONT, command=self.compute_bets,)
        btn_start.grid(column=4, row=3, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW",)
        # Reset bet button
        btn_reset_bet = tk.Button(self, text="Reset Bet", font=NORMAL_FONT, command=self.reset_bet,)
        btn_reset_bet.grid(column=4, row=4, columnspan=2, padx=(5, 0), sticky="NESW")
        # Deposite Button
        btn_deposit = tk.Button(self, text="Deposit", font=NORMAL_FONT, command=self.show_DepositPage,)
        btn_deposit.grid(column=6, row=3, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW",)
        # Withdraw Button
        btn_withdraw = tk.Button(self, text="Withdraw", font=NORMAL_FONT, command=lambda: controller.show_frame(StartPage),)
        btn_withdraw.grid(column=7, row=4, padx=(5, 0), sticky="NESW")
        # Log out Button
        btn_logout = tk.Button(self, text="Log out", font=NORMAL_FONT, command=lambda: controller.show_frame(StartPage),)
        btn_logout.grid(column=6, row=4, padx=(5, 0), sticky="NESW")

    def set_turtles(self):
        for t in self.turtles:
            t[0].shape("turtle")
            t[0].shapesize(2)
            t[0].color(t[1])
            t[0].penup()
            t[0].goto(x=-300, y=self.turtle_ypos[self.turtles.index(t)])
            t[0].pendown()

    def compute_bets(self) -> int:
        for bet in self.all_bets:
            bet = bet.get()
            self.total_bet += bet

        if self.total_bet > self.balance:
            messagebox.showwarning(title="Invalid Input", message="Insufficient balance.")
            self.total_bet = 0
            return None
        else:
            self.total_bet_str.set(f"Total Bet: {self.total_bet}")
            self.reset_bet()


    def show_DepositPage(self):
        deposit_page = DepositPage(self.email, self.balance, self.balance_str)
        deposit_page.title("Deposit thru Paypal")
        deposit_page.resizable(width=False, height=False)
        deposit_page.mainloop()

    def reset_bet(self):
        for bet in self.all_bets:
            bet.set(0)


class DepositPage(tk.Toplevel):
    def __init__(self, email, balance, balance_str, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        self.email = email
        self.balance = balance
        self.balance_str = balance_str

        lb_title = tk.Label(self, text="Deposit (Paypal)", font=LARGE_FONT, anchor="center")
        lb_title.grid(column=0, row=0, columnspan=3, padx=20, pady=20, sticky="nesw")

        lb_amount = tk.Label(self, text="Amount (min: Php 100)", font=NORMAL_FONT, anchor="center")
        lb_amount.grid(column=0, row=1, columnspan=3, padx=20, pady=(20, 10), sticky="nesw")

        self.entry_amount = tk.Entry(self, width=30, font=NORMAL_FONT, borderwidth=2,)
        self.entry_amount.grid(column=0, row=2, padx=20, pady=(0, 20), sticky="NESW",)

        btn_signup = tk.Button(self, text="Confirm Payment", font=NORMAL_FONT, command=self.confirm_payment)
        btn_signup.grid(column=0, row=3, columnspan=3, padx=20, pady=(10, 20), sticky="nesw")

    def confirm_payment(self):
        entry_amount = int(self.entry_amount.get())
        if entry_amount >= 100:
            self.balance += entry_amount
            update_balance(self.email, self.balance)
            self.balance_str.set(f"Balance: Php {self.balance}")
            self.destroy()
        else:
            messagebox.showwarning(title="Invalid Input", message="Amount is below the minimum payment required.")
            self.lift()