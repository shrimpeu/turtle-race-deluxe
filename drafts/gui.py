import tkinter as tk
import turtle

from config import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        root = tk.Frame(self)
        root.pack(side="top", fill="both", expand=True)

        # 0 = minimum
        # Weight = priority
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        pages = (
            StartPage,
            SignUpPage,
            SignInPage,
            MainPage,
            DepositPage,
            GCashDepositPage,
            PaymayaDepositPage,
            PaypalDepositPage,
            WithdrawPage,
        )

        self.frames = {}

        for F in pages:
            frame = F(root, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):  # cont = controller
        frame = self.frames[cont]
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
        entry_firstname = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT,)
        entry_firstname.grid(column=1, row=1, columnspan=2, pady=(0, 10))

        entry_lastname = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT,)
        entry_lastname.grid(column=1, row=2, columnspan=2, pady=(0, 10))

        entry_email = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT,)
        entry_email.grid(column=1, row=3, columnspan=2, pady=(0, 10))

        entry_passwd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT, show="*",)
        entry_passwd.grid(column=1, row=4, columnspan=2, pady=(20, 10))

        entry_repasswd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT, show="*",)
        entry_repasswd.grid(column=1, row=5, columnspan=2, pady=(0, 10))

        #----- Create button widgets -----#
        btn_create_account = tk.Button(self, text="Create Account", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(MainPage),)
        btn_create_account.grid(column=1, row=6, columnspan=2, pady=(10, 0), sticky="NESW")

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(StartPage),)
        btn_cancel.grid(column=0, row=6, pady=(10, 0), padx=(0, 5), sticky="NESW")


class SignInPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1, relief=tk.SUNKEN)

        #----- Label widgets -----#
        lb_title = tk.Label(self, text="Sign in", width=20, height=1, font=LARGE_FONT, bg=BG_1, fg=FG_1, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        lb_email = tk.Label(self, text="Email: ", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_email.grid(column=0, row=1, pady=(0, 10), padx=(0, 5))

        lb_passwd = tk.Label(self, text="Password: ", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_passwd.grid(column=0, row=2, pady=(0, 10), padx=(0, 5))

        #----- Entry widgets -----#
        entry_email = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT,)
        entry_email.grid(column=1, row=1, columnspan=2, pady=(0, 10))

        entry_passwd = tk.Entry(self, width=30, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT, show="*",)
        entry_passwd.grid(column=1, row=2, columnspan=2, pady=(0, 10))

        #----- Button widgets -----#
        btn_signin = tk.Button(self, text="Sign in", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(MainPage),)
        btn_signin.grid(column=1, row=3, columnspan=2, pady=(10, 0), sticky="NESW")

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(StartPage),)
        btn_cancel.grid(column=0, row=3, pady=(10, 0), padx=(0, 5), sticky="NESW")


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20)

        canvas = tk.Canvas(self, width=760, height=300)
        canvas.grid(column=0, row=0, columnspan=8, pady=(0, 20))

        draw = turtle.RawTurtle(canvas)

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
        entry_bet_RO = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_RO.grid(column=1, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_GO = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_GO.grid(column=1, row=2, pady=(0, 5), sticky="NESW")

        entry_bet_BO = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_BO.grid(column=1, row=3, pady=(0, 5), sticky="NESW")

        entry_bet_YO = tk.Entry(self, width=5, font=NORMAL_FONT)
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
        entry_bet_RY = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_RY.grid(column=3, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_GY = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_GY.grid(column=3, row=2, pady=(0, 5), sticky="NESW")

        entry_bet_BY = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_BY.grid(column=3, row=3, pady=(0, 5), sticky="NESW")

        entry_bet_GB = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_GB.grid(column=3, row=4, sticky="NESW")

        #----- 5th Column -----#
        lb_RB = tk.Label(self, text=" R-B ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_RB.grid(column=4, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_RG = tk.Label(self, text=" R-G ", height=1, font=NORMAL_FONT, relief=tk.RAISED)
        lb_RG.grid(column=4, row=2, padx=(5, 5), pady=(0, 5), sticky="NESW")

        # 6th column
        entry_bet_RB = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_RB.grid(column=5, row=1, pady=(0, 5), sticky="NESW")

        entry_bet_RG = tk.Entry(self, width=5, font=NORMAL_FONT)
        entry_bet_RG.grid(column=5, row=2, pady=(0, 5), sticky="NESW")

        #----- Buttons -----#

        # Game start button
        btn_start = tk.Button(self, text="Start Game", font=NORMAL_FONT)
        btn_start.grid(column=4, row=3, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW",)
        # Reset bet button
        btn_reset_bet = tk.Button(self, text="Reset Bet", font=NORMAL_FONT)
        btn_reset_bet.grid(column=4, row=4, columnspan=2, padx=(5, 0), sticky="NESW")
        # Deposite Button
        btn_deposit = tk.Button(self, text="Deposit", font=NORMAL_FONT, command=lambda: controller.show_frame(DepositPage),)
        btn_deposit.grid(column=6, row=3, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW",)
        # Withdraw Button
        btn_withdraw = tk.Button(self, text="Withdraw", font=NORMAL_FONT, command=lambda: controller.show_frame(WithdrawPage))
        btn_withdraw.grid(column=7, row=4, padx=(5, 0), sticky="NESW")
        # Log out Button
        btn_logout = tk.Button(self, text="Log out", font=NORMAL_FONT, command=lambda: controller.show_frame(StartPage),)
        btn_logout.grid(column=6, row=4, padx=(5, 0), sticky="NESW")

        #----- Labels - Account info -----#
        lb_total_bet = tk.Label(self, text="Total bet: 12345", heigh=1, font=NORMAL_FONT, anchor="w")
        lb_total_bet.grid(column=6, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_user_balance = tk.Label(self, text="Balance: Php 12345", heigh=1, font=NORMAL_FONT, anchor="w",)
        lb_user_balance.grid(column=6, row=2, padx=(5, 5), pady=(0, 5), sticky="NESW")

        lb_user_name = tk.Label(self, text="Name: Juan Dela Cruz", heigh=1, font=NORMAL_FONT, anchor="w",)
        lb_user_name.grid(column=7, row=1, padx=(5, 5), pady=(0, 5), sticky="NESW")


class DepositPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1, relief=tk.SUNKEN)

        payment_option = ["GCash", "Paymaya", "Paypal"]

        #----- Title -----#
        lb_title = tk.Label(self, text="Deposit", width=20, height=1, font=LARGE_FONT, bg=BG_1, fg=FG_1, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=2, pady=(0, 20), padx=(10, 10))

        #----- Amount input section -----#
        lb_amount = tk.Label(self, text="Amount (min. Php 100)", height=1, font=NORMAL_FONT, fg=FG_1, bg=BG_1, anchor="center")
        lb_amount.grid(column=0, row=1, columnspan=2, pady=(0, 10), padx=(10, 10))

        entry_amount = tk.Entry(self, width=10, borderwidth=2, relief=tk.GROOVE, fg=FG_1, bg=BG_2, font=NORMAL_FONT,)
        entry_amount.grid(column=0, row=2, columnspan=2, pady=(0, 20), padx=(10, 10), sticky="NESW")

        #----- Payment method section -----#
        lb_payment_opt = tk.Label(self, text="Payment Method", height=1, font=NORMAL_FONT, fg=FG_1, bg=BG_1, anchor="center")
        lb_payment_opt.grid(column=0, row=3, columnspan=2, pady=(0, 5), padx=(10, 10))

        btn_gcash = tk.Button(self, text="GCash", font=NORMAL_FONT, fg=FG_1, bg=BG_1, command=lambda: controller.show_frame(GCashDepositPage))
        btn_gcash.grid(column=0, row=4, columnspan=2, pady=(5, 5), padx=(10, 10), sticky="NESW")

        btn_paymaya = tk.Button(self, text="Paymaya", font=NORMAL_FONT, fg=FG_1, bg=BG_1, command=lambda: controller.show_frame(PaymayaDepositPage))
        btn_paymaya.grid(column=0, row=5, columnspan=2, pady=(5, 5), padx=(10, 10), sticky="NESW")

        btn_paypal = tk.Button(self, text="Paypal", font=NORMAL_FONT, fg=FG_1, bg=BG_1, command=lambda: controller.show_frame(PaypalDepositPage))
        btn_paypal.grid(column=0, row=6, columnspan=2, pady=(5, 5), padx=(10, 10), sticky="NESW")

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(MainPage))
        btn_cancel.grid(column=0, row=7, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="NESW")


class GCashDepositPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1, relief=tk.SUNKEN)

        lb_title = tk.Label(self, text="Pay with GCash", width=20, height=1, font=LARGE_FONT, bg=BG_1, fg=FG_1, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(DepositPage))
        btn_cancel.grid(column=0, row=1, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="NESW")


class PaypalDepositPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1, relief=tk.SUNKEN)

        lb_title = tk.Label(self, text="Pay with Paypal", width=20, height=1, font=LARGE_FONT, bg=BG_1, fg=FG_1, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(DepositPage))
        btn_cancel.grid(column=0, row=1, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="NESW")


class PaymayaDepositPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1, relief=tk.SUNKEN)

        lb_title = tk.Label(self, text="Pay with Paymaya", width=20, height=1, font=LARGE_FONT, bg=BG_1, fg=FG_1, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(DepositPage))
        btn_cancel.grid(column=0, row=1, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="NESW")


class WithdrawPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1, relief=tk.SUNKEN)

        lb_title = tk.Label(self, text="Withdraw", width=20, height=1, font=LARGE_FONT, bg=BG_1, fg=FG_1, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=FG_1, bg=BG_2, command=lambda: controller.show_frame(DepositPage))
        btn_cancel.grid(column=0, row=1, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="NESW")
