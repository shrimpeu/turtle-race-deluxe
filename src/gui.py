# Built-in modules
import tkinter as tk
import turtle
import random

# Specific methods from built-in modules
from tkinter import messagebox

# Custom modules
from src.config import *
from src.helpers import *


class App(tk.Tk):
    """
    The main root of the app interface. The class that controls the interface/pages.

    Attributes:
        root (tkinter.Frame): instance of main frame
        frames (dict): dictionary of frames that the root will control to navigate through pages
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default=APP_LOGO)

        self.root = tk.Frame(self)
        self.root.pack(side="top", fill="both", expand=True)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.geometry("970x617")

        self.frames = {}

        for F in {StartPage, SignInPage, SignUpPage}:
            frame = F(self.root, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        """Shows the selected frame by bringing/raising it forward"""
        frame = self.frames[cont]
        frame.tkraise()

    def show_main_page(self, email=None):
        """Shows the MainPage frame"""
        frame = MainPage(self.root, self, email)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class StartPage(tk.Frame):
    """
    The class that displays the start page of the app

    Args:
        parent (tkinter.Frame): the root interface that will control this frame class
        controller (tkinter.Tk): the App class
    
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
        parent (tkinter.Frame): the root interface that will control this frame class
        controller (tkinter.Tk): the App class
    
    Attributes:
        entry_firstname (tkinter.Entry): entry widget that receives the first name of the user.
        entry_lastname (tkinter.Entry): entry widget that receives the last name of the user.
        entry_email (tkinter.Entry): entry widget that receives the email of the user.
        entry_passwd (tkinter.Entry): entry widget that receives the password created by the user.
        entry_repasswd (tkinter.Entry): entry widget that receives the re-typed password created by the user.
        entry_boxes (list): list of all entry widgets
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=170, pady=150, bg=BG_1)

        #----- Label widgets -----#
        lb_title = tk.Label(self, text="Sign up", width=20, height=1, font=SUBTITLE_FONT, bg=BG_1, fg=TITLE_FG, anchor="center",)
        lb_title.grid(column=0, row=0, columnspan=3, pady=(0, 20), padx=(10, 10))

        lb_firstname = tk.Label(self, text="First name:", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_firstname.grid(column=0, row=1, pady=(0, 10), padx=(0, 5))

        lb_lastname = tk.Label(self, text="Last name:", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_lastname.grid(column=0, row=2, pady=(0, 10), padx=(0, 5))

        lb_email = tk.Label(self, text="Email:", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
        lb_email.grid(column=0, row=3, pady=(0, 10), padx=(0, 5))

        lb_passwd = tk.Label(self, text="Password (>8 chars.):", width=20, height=1, font=NORMAL_FONT, bg=BG_1, fg=FG_1, anchor="e",)
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

        self.entry_boxes = (self.entry_firstname, self.entry_lastname, self.entry_email,
                   self.entry_passwd, self.entry_repasswd)

        #----- Create button widgets -----#
        btn_create_account = tk.Button(self, text="Create Account", font=NORMAL_FONT, fg=BUTTON_FG, bg=BUTTON_BG, command=lambda: controller.show_frame(StartPage) if self.valid_credentials() else None,)
        btn_create_account.grid(column=1, row=6, columnspan=2, pady=(10, 0), sticky="NESW")

        btn_cancel = tk.Button(self, text="Cancel", font=NORMAL_FONT, fg=BUTTON_FG, bg=BUTTON_BG, command=lambda: controller.show_frame(StartPage),)
        btn_cancel.grid(column=0, row=6, pady=(10, 0), padx=(0, 5), sticky="NESW")

    def valid_credentials(self) -> bool:
        """Check all user inputs if they are valid and stores them in user_data if True"""
        entries = [self.entry_firstname.get(), self.entry_lastname.get(), self.entry_email.get(),
                   self.entry_passwd.get(), self.entry_repasswd.get()]

        if input_not_empty(self, entries) and \
            valid_passwd(self, entries[3]) and valid_email(self, entries[2]):
            input_email = self.entry_email.get().encode("utf-8")

            if email_taken(input_email):
                messagebox.showwarning(title="Invalid Credentials", message="Email already in use.")
                return False
            else:
                input_email = hash_str(input_email)
                if entries[3] == entries[4]:
                    add_new_account(input_email, entries[0], entries[1], entries[3])
                    for e in self.entry_boxes:
                        e.delete(0, tk.END)
                    return True
                else:
                    messagebox.showwarning(title="Invalid Input", message="Password do not match.")
            return False


class SignInPage(tk.Frame):
    """
    The class that displays the sign in page of the App.

    Args:
        parent (tkinter.Frame): the root interface that will control this frame class
        controller (tkinter.Tk): the App class
    
    Attributes:
        entry_email (tkinter.Entry): entry widget that receives the email of the user.
        entry_passwd (tkinter.Entry): entry widget that receives the password created by the user.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=170, pady=100, bg=BG_1)

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
                self.entry_passwd.delete(0, tk.END)
                return True
            else:
                messagebox.showwarning(title="Invalid Credentials", message="Invalid password.")
                return False
        else:
            messagebox.showwarning(title="Invalid Credentials", message="Email is not yet registered. Try signing up first.")
            return False


class MainPage(tk.Frame):
    """
    The main page/frame where the main program interface is shown. It contains
    the turtle race game, betting section, and deposit/withdraw sections.

    Args:
        parent (tkinter.Frame): the root interface that will controll this frame class
        controller (tkinter.Tk): the App class
        email (str): the email used in signing in

    Attributes:
        balance (int): the account balanced register in email, which is stored in user_data
        email (str): the email matched with the argument email
        canvas (tkinter.Canvas): canvas where the turtle interface puts in
        turtle_section (turtle.TurtleScreen): the turtle interface
        *turtle (turtle.RawTurtle): instance of a turtle class; creates the turtles for the race
        turtles (list): list of all turtle instances with color string according to their name
        turtle_ypos (list): list of y-coordinates (int) for setting turtles in starting line
        total_bet (int): stores the total bet inputted by the user
        total_bet_str (tkinter.StringVar): where label widget text for total bets is stored
        balance_str (tkinter.StringVar): where label widget text for account balance is stored
        input_bet_* (tkinter.StringVar): where entry widget value for bets are stored
        entry_bet_* (tkinter.Entry): entry boxes for bets
        bet_entries (list): list of input_bet_* and combinations (str) connected to them
        bet_entry_boxes (list): list of all entry_bet_* widgets
        bets_tally (dict): stores all the bet (values) for each combinations (keys)
        btn_start (tkinter.Button): button to start turtle race along with tallying all the input bets
        btn_reset_bet (tkinter.Button): button to set all the entry_bet_* to 0
        btn_deposit (tkinter.Button): button to open deposit page/window
        btn_withdraw (tkinter.Button): button to open withdraw page/window
        btn_logout (tkinter.Button): button to exit MainPage and go to StartPage
        buttons (tuple): list of all buttons
    """
    def __init__(self, parent, controller, email):
        tk.Frame.__init__(self, parent, padx=20, pady=20, bg=BG_1)

        # Get info from email that has been logged in
        for e in EXISTING_ACCOUNTS:
            if bcrypt.checkpw(email.encode("utf-8"), e.encode("utf-8")):
                f_name = EXISTING_ACCOUNTS[e]["first_name"]
                l_name = EXISTING_ACCOUNTS[e]["last_name"]
                self.balance = EXISTING_ACCOUNTS[e]["balance"]
                self.email = e
        
        valid_entry = (self.register(self.check_if_digits), "%d", "%P")

        # Set canvas for turtle section
        self.canvas = tk.Canvas(self, width=850, height=400, bg="black")
        self.canvas.grid(column=0, row=0, columnspan=13, pady=(0, 20))

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
        self.set_title()

        #----- Labels - Account info -----#
        self.total_bet = 0
        self.total_bet_str = tk.StringVar()
        self.total_bet_str.set(f"Bet: Php {self.total_bet}")

        lb_total_bet = tk.Label(self, textvariable=self.total_bet_str, height=1, font=NORMAL_FONT, anchor="w", relief=tk.SUNKEN, fg=TITLE_FG, bg=BUTTON_BG)
        lb_total_bet.grid(column=10, row=2, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW")

        lb_user_name = tk.Label(self, text=f"Name: {f_name[:30]}. {l_name[:1]}.", height=1, font=NORMAL_FONT, anchor="w", relief=tk.SUNKEN, fg=TITLE_FG, bg=BUTTON_BG)
        lb_user_name.grid(column=10, row=3, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW")

        self.balance_str = tk.StringVar()
        self.balance_str.set(f"BAL: Php {self.balance}")

        lb_user_balance = tk.Label(self, textvariable=self.balance_str, height=1, font=NORMAL_FONT, anchor="w", relief=tk.SUNKEN, fg=TITLE_FG, bg=BUTTON_BG)
        lb_user_balance.grid(column=10, row=4, columnspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW")

        #----- 1st Column -----#
        lb_RG = tk.Label(self, text=" R-G ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_RG.grid(column=0, row=1, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_RB = tk.Label(self, text=" R-B ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_RB.grid(column=0, row=2, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_RY = tk.Label(self, text=" R-Y ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_RY.grid(column=0, row=3, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_RO = tk.Label(self, text=" R-O ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_RO.grid(column=0, row=4, padx=(0, 5), sticky="NESW")
        #----------------------#

        #----- 2nd column -----#
        self.input_bet_RG = tk.StringVar()
        self.input_bet_RB = tk.StringVar()
        self.input_bet_RY = tk.StringVar()
        self.input_bet_RO = tk.StringVar()

        self.entry_bet_RG = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RG, validate="key", validatecommand=valid_entry)
        self.entry_bet_RG.grid(column=1, row=1, pady=(0, 5), sticky="NESW")

        self.entry_bet_RB = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RB,)
        self.entry_bet_RB.grid(column=1, row=2, pady=(0, 5), sticky="NESW")

        self.entry_bet_RY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RY,)
        self.entry_bet_RY.grid(column=1, row=3, pady=(0, 5), sticky="NESW")

        self.entry_bet_RO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_RO,)
        self.entry_bet_RO.grid(column=1, row=4, sticky="NESW")
        #----------------------#

        #----- 3rd Column -----#
        lb_GR = tk.Label(self, text=" G-R ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_GR.grid(column=2, row=1, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_GB = tk.Label(self, text=" G-B ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_GB.grid(column=2, row=2, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_GY = tk.Label(self, text=" G-Y ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_GY.grid(column=2, row=3, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_GO = tk.Label(self, text=" G-O ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_GO.grid(column=2, row=4, padx=(0, 5), sticky="NESW")
        #----------------------#

        #----- 4th column -----#
        self.input_bet_GR = tk.StringVar()
        self.input_bet_GB = tk.StringVar()
        self.input_bet_GY = tk.StringVar()
        self.input_bet_GO = tk.StringVar()

        self.entry_bet_GR = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GR,)
        self.entry_bet_GR.grid(column=3, row=1, pady=(0, 5), sticky="NESW")

        self.entry_bet_GB = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GB,)
        self.entry_bet_GB.grid(column=3, row=2, pady=(0, 5), sticky="NESW")

        self.entry_bet_GY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GY,)
        self.entry_bet_GY.grid(column=3, row=3, pady=(0, 5), sticky="NESW")

        self.entry_bet_GO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_GO,)
        self.entry_bet_GO.grid(column=3, row=4, sticky="NESW")
        #----------------------#

        #----- 5th Column -----#
        lb_BR = tk.Label(self, text=" B-R ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_BR.grid(column=4, row=1, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_BG = tk.Label(self, text=" B-G ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_BG.grid(column=4, row=2, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_BY = tk.Label(self, text=" B-Y ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_BY.grid(column=4, row=3, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_BO = tk.Label(self, text=" B-O ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_BO.grid(column=4, row=4, padx=(0, 5), sticky="NESW")
        #----------------------#

        #----- 6th column -----#
        self.input_bet_BR = tk.StringVar()
        self.input_bet_BG = tk.StringVar()
        self.input_bet_BY = tk.StringVar()
        self.input_bet_BO = tk.StringVar()

        self.entry_bet_BR = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_BR,)
        self.entry_bet_BR.grid(column=5, row=1, pady=(0, 5), sticky="NESW")

        self.entry_bet_BG = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_BG,)
        self.entry_bet_BG.grid(column=5, row=2, pady=(0, 5), sticky="NESW")

        self.entry_bet_BY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_BY,)
        self.entry_bet_BY.grid(column=5, row=3, pady=(0, 5), sticky="NESW")

        self.entry_bet_BO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_BO,)
        self.entry_bet_BO.grid(column=5, row=4, sticky="NESW")
        #----------------------#

        #----- 7th Column -----#
        lb_YR = tk.Label(self, text=" Y-R ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_YR.grid(column=6, row=1, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_YG = tk.Label(self, text=" Y-G ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_YG.grid(column=6, row=2, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_YB = tk.Label(self, text=" Y-B ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_YB.grid(column=6, row=3, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_YO = tk.Label(self, text=" Y-O ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_YO.grid(column=6, row=4, padx=(0, 5), sticky="NESW")
        #----------------------#

        #----- 8th column -----#
        self.input_bet_YR = tk.StringVar()
        self.input_bet_YG = tk.StringVar()
        self.input_bet_YB = tk.StringVar()
        self.input_bet_YO = tk.StringVar()

        self.entry_bet_YR = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_YR,)
        self.entry_bet_YR.grid(column=7, row=1, pady=(0, 5), sticky="NESW")

        self.entry_bet_YG = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_YG,)
        self.entry_bet_YG.grid(column=7, row=2, pady=(0, 5), sticky="NESW")

        self.entry_bet_YB = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_YB,)
        self.entry_bet_YB.grid(column=7, row=3, pady=(0, 5), sticky="NESW")

        self.entry_bet_YO = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_YO,)
        self.entry_bet_YO.grid(column=7, row=4, sticky="NESW")
        #----------------------#

        #----- 9th Column -----#
        lb_OR = tk.Label(self, text=" O-R ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_OR.grid(column=8, row=1, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_OG = tk.Label(self, text=" O-G ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_OG.grid(column=8, row=2, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_OB = tk.Label(self, text=" O-B ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_OB.grid(column=8, row=3, padx=(0, 5), pady=(0, 5), sticky="NESW")

        lb_OY = tk.Label(self, text=" O-Y ", height=1, font=NORMAL_FONT, relief=tk.SUNKEN, fg=BUTTON_BG, bg=TITLE_FG, width=3)
        lb_OY.grid(column=8, row=4, padx=(0, 5), sticky="NESW")
        #----------------------#

        #----- 10th column -----#
        self.input_bet_OR = tk.StringVar()
        self.input_bet_OG = tk.StringVar()
        self.input_bet_OB = tk.StringVar()
        self.input_bet_OY = tk.StringVar()

        self.entry_bet_OR = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_OR,)
        self.entry_bet_OR.grid(column=9, row=1, pady=(0, 5), sticky="NESW")

        self.entry_bet_OG = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_OG,)
        self.entry_bet_OG.grid(column=9, row=2, pady=(0, 5), sticky="NESW")

        self.entry_bet_OB = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_OB,)
        self.entry_bet_OB.grid(column=9, row=3, pady=(0, 5), sticky="NESW")

        self.entry_bet_OY = tk.Entry(self, width=5, font=NORMAL_FONT, textvariable=self.input_bet_OY,)
        self.entry_bet_OY.grid(column=9, row=4, sticky="NESW")
        #----------------------#

        #----- USER INPUT LIST -----#
        self.bet_entries = [
            [self.input_bet_RG, "R-G"],[self.input_bet_RB, "R-B"],[self.input_bet_RY, "R-Y"],
            [self.input_bet_RO, "R-O"],[self.input_bet_GR, "G-R"],[self.input_bet_GB, "G-B"],
            [self.input_bet_GY, "G-Y"],[self.input_bet_GO, "G-O"],[self.input_bet_BR, "B-R"],
            [self.input_bet_BG, "B-G"],[self.input_bet_BY, "B-Y"],[self.input_bet_BO, "B-O"],
            [self.input_bet_YR, "Y-R"],[self.input_bet_YG, "Y-G"],[self.input_bet_YB, "Y-B"],
            [self.input_bet_YO, "Y-O"],[self.input_bet_OR, "O-R"],[self.input_bet_OG, "O-G"],
            [self.input_bet_OB, "O-B"],[self.input_bet_OY, "OY"]
        ]

        self.bet_entry_boxes = (
            self.entry_bet_RG, self.entry_bet_RB, self.entry_bet_RY, self.entry_bet_RO,
            self.entry_bet_GR, self.entry_bet_GB, self.entry_bet_GY, self.entry_bet_GO,
            self.entry_bet_BR, self.entry_bet_BG, self.entry_bet_BY, self.entry_bet_BO,
            self.entry_bet_YR, self.entry_bet_YG, self.entry_bet_YB, self.entry_bet_YO,
            self.entry_bet_OR, self.entry_bet_OG, self.entry_bet_OB, self.entry_bet_OY,
        )

        self.bets_tally = {
            "R-G": 0, "G-R": 0, "B-R": 0, "Y-R": 0, "O-R": 0,
            "R-B": 0, "G-B": 0, "B-G": 0, "Y-G": 0, "O-G": 0,
            "R-Y": 0, "G-Y": 0, "B-Y": 0, "Y-B": 0, "O-B": 0,
            "R-O": 0, "G-O": 0, "B-O": 0, "Y-O": 0, "O-Y": 0
        }

        #----- Buttons -----#

        # Game start button
        self.btn_start = tk.Button(self, text="Start Game", font=NORMAL_FONT, command=self.start_race, height=1, fg=TITLE_FG, bg="white")
        self.btn_start.grid(column=10, row=1, padx=(5, 0), pady=(0, 5), sticky="NESW",)
        # Reset bet button
        self.btn_reset_bet = tk.Button(self, text="Reset Bet", font=NORMAL_FONT, command=self.reset_bet, height=1, fg=TITLE_FG, bg="white")
        self.btn_reset_bet.grid(column=11, row=1, padx=(5, 0), pady=(0, 5), sticky="NESW")
        # Deposite Button
        self.btn_deposit = tk.Button(self, text="Deposit", font=NORMAL_FONT, command=self.show_DepositPage, height=1, fg=TITLE_FG, bg="white")
        self.btn_deposit.grid(column=12, row=1, rowspan=2, padx=(5, 0), pady=(0, 5), sticky="NESW",)
        # Withdraw Button
        self.btn_withdraw = tk.Button(self, text="Withdraw", font=NORMAL_FONT, command=self.show_WithdrawPage, height=1, fg=TITLE_FG, bg="white")
        self.btn_withdraw.grid(column=12, row=3, padx=(5, 0), pady=(0, 5), sticky="NESW")
        # Log out Button
        self.btn_logout = tk.Button(self, text="Log out", font=NORMAL_FONT, command=lambda: controller.show_frame(StartPage), height=1, fg="red", bg="white")
        self.btn_logout.grid(column=12, row=4, padx=(5, 0), sticky="NESW")

        self.buttons = (self.btn_start, self.btn_reset_bet, self.btn_deposit,
                        self.btn_withdraw, self.btn_logout)

    def set_turtles(self) -> None:
        """Positions turtles in starting line"""
        for t in self.turtles:
            t[0].speed(0)
            t[0].clear()
            self.turtle_section.addshape(f"assets/t_{t[1]}.gif")
            t[0].shape(f"assets/t_{t[1]}.gif")
            t[0].shapesize(2)
            t[0].pencolor(t[1])
            t[0].penup()
            t[0].goto(x=-380, y=self.turtle_ypos[self.turtles.index(t)])
            t[0].pendown()

    def set_title(self) -> None:
        """Writes the title at top of the turtle interface"""
        title = "TURTLE RACE"
        t = turtle.RawTurtle(self.turtle_section)
        t.pencolor("white")
        t.speed(0)
        t.penup()
        t.goto(x=0, y=140)
        t.pendown()
        t.write(title, align="center", font=SUBTITLE_FONT)
        t.penup()
        t.hideturtle()

    def start_race(self) -> None:
        """Move the turtles forward until finish line"""
        if self.compute_bets():
            winners = []

            self.disable_enable_entries()
            self.disable_enable_buttons()
            while len(winners) < 2:
                for t in self.turtles:
                    if t[2] in winners:
                        continue
                    if t[0].xcor() >= 380:
                        winners.append(t[2])
                    else:
                        d = random.randint(3, 20)
                        t[0].forward(random.randint(1, d))
            
            winners = "-".join(winners)

            if len(winners) > 2:
                winners = winners[:3]

            win_amount = self.bets_tally[winners]
            
            messagebox.showinfo(title="Game Result", message=display_result(winners, win_amount))
            
            self.compute_wins(winners)

            self.total_bet = 0
            self.total_bet_str.set("Bet: Php 0")

            self.set_turtles()
            self.disable_enable_buttons()
            self.disable_enable_entries()

    def compute_bets(self) -> int:
        """Adds all the input bets and store in bets_tally"""
        for b in self.bet_entries:
            try:
                bet = b[0].get()
                if bet == "":
                    bet = 0
                else:
                    bet = int(bet.lstrip("0"))
            except:
                bet = 0
            self.bets_tally[b[1]] = bet
            self.total_bet += bet
        
        self.balance = curr_balance(self.email)
        if self.total_bet == 0:
            messagebox.showwarning(title="Invalid Input", message="Hey, bet something!")
            self.total_bet = 0
            return False
        elif self.total_bet == self.balance or self.total_bet < self.balance:
            self.total_bet_str.set(f"Bet: Php {self.total_bet}")
            return True
        else:
            messagebox.showwarning(title="Invalid Input", message="Insufficient balance.")
            self.total_bet = 0
            return False
    
    def compute_wins(self, winner) -> None:
        """Update account balance based on game result"""
        self.balance = curr_balance(self.email)

        win_amount = self.bets_tally[winner]    
        lose_amount = self.total_bet - win_amount
        new_balance = self.balance + win_amount - lose_amount

        update_balance(self.email, new_balance)

        self.balance_str.set(f"BAL: Php {curr_balance(self.email)}")
    
    def check_if_digits(self, action, value_if_allowed):
        """Check if the entry input contains only digits"""
        if action != '1':
            return True
        try:
            return value_if_allowed.isnumeric()
        except ValueError:
            return False

    def disable_enable_buttons(self) -> None:
        """Disable buttons if state is normal, enable it otherwise"""
        for b in self.buttons:
            if b["state"] == "normal":
                b["state"] = "disable"
            else:
                b["state"] = "normal"

    def disable_enable_entries(self) -> None:
        """Disable entry widget if state is normal, enable it otherwise"""
        for b in self.bet_entry_boxes:
            if b["state"] == "normal":
                b["state"] = "disable"
            else:
                b["state"] = "normal"

    def show_DepositPage(self) -> None:
        """Opens DepositPage window"""
        deposit_page = DepositPage(self.email,  self.balance_str)
        deposit_page.title("Deposit thru Paypal")
        deposit_page.resizable(width=False, height=False)
        deposit_page.mainloop()

    def show_WithdrawPage(self) -> None:
        """Opens WithdrawPage window"""
        withdraw_page = WithdrawPage(self.email, self.balance_str)
        withdraw_page.title("Withdraw")
        withdraw_page.resizable(width=False, height=False)
        withdraw_page.mainloop()

    def reset_bet(self) -> None:
        """Set all entry_bet_* to 0"""
        for bet in self.bet_entries:
            bet[0].set(0)


class DepositPage(tk.Toplevel):
    """
    The pop-up window that shows the deposit section of the App.

    Args:
        email (str): the email that is used by user to log in
        balance_str (tkinter.StringVar): holds the text for balance label in MainPage
    
    Attributes:
        email (str): the email that is used by the user to log in
        balance_str (tkinter.StringVar): holds the text for balance label in MainPage
        logo (tkinter.PhotoImage): imports the logo for payment method
        lb_logo (tkinter.Label): label widget for displaying the logo
        entry_amount (tkinter.Entry): entry widget for deposit amount
        entry_paypal_email (tkinter.Entry): entry widget for paypal email
        entry_paypal_pw (tkinter.Entry): entry widget for password associated with paypal email
    """
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
        """Confirms the deposit if inputs are valid"""
        balance = curr_balance(self.email)
        entries = [self.entry_paypal_email.get(), self.entry_paypal_pw.get()]
        entry_amount = int(self.entry_amount.get())
        if valid_amount(self, "deposit", entry_amount, balance) and \
            input_not_empty(self, entries) and valid_email(self, self.entry_paypal_email.get()) and \
                valid_passwd(self, self.entry_paypal_pw.get()):
            balance += entry_amount
            update_balance(self.email, balance)
            self.balance_str.set(f"BAL: Php {balance}")
            self.destroy()


class WithdrawPage(tk.Toplevel):
    """
    The pop-up window that shows the withdraw section of the App.

    Args:
        email (str): the email that is used by user to log in
        balance_str (tkinter.StringVar): holds the text for balance label in MainPage
    
    Attributes:
        email (str): the email that is used by the user to log in
        balance_str (tkinter.StringVar): holds the text for balance label in MainPage
        logo (tkinter.PhotoImage): imports the logo for payment method
        lb_logo (tkinter.Label): label widget for displaying the logo
        entry_amount (tkinter.Entry): entry widget for deposit amount
        entry_paypal_email (tkinter.Entry): entry widget for paypal email
        entry_paypal_pw (tkinter.Entry): entry widget for password associated with paypal email
    """
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
        """Confirms the withdrawal if inputs are valid"""
        balance = curr_balance(self.email)
        entries = [self.entry_paypal_email.get(), self.entry_paypal_pw.get()]
        entry_amount = int(self.entry_amount.get())
        if valid_amount(self, "withdraw", entry_amount, balance) and \
            input_not_empty(self, entries) and valid_email(self, self.entry_paypal_email.get()) and \
                valid_passwd(self, self.entry_paypal_pw.get()):
            balance -= entry_amount
            update_balance(self.email, balance)
            self.balance_str.set(f"BAL: Php {balance}")
            self.destroy()
