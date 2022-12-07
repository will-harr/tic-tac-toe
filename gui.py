from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window

        self.p1_turn = True
        self.tl_status = None  # top left
        self.ml_status = None  # middle left
        self.bl_status = None  # bottom left
        self.tc_status = None  # top center
        self.mc_status = None  # middle center
        self.bc_status = None  # bottom center
        self.tr_status = None  # top right
        self.mr_status = None  # middle right
        self.br_status = None  # bottom right

        self.statuslabel = Label(window, text='Player 1\'s turn')
        self.statuslabel.pack(side='top', pady=20)

        self.boardFrame = Frame(window)
        self.boardFrame.place(x=37, y=45)

        self.frameleft = Frame(self.boardFrame)
        self.frameleft.pack(side='left', padx=10)
        self.topleft = Button(self.frameleft, command=self.tl_clicked, height=2, width=2)
        self.topleft.pack(pady=10)
        self.middleleft = Button(self.frameleft, command=self.ml_clicked, height=2, width=2)
        self.middleleft.pack(pady=10)
        self.bottomleft = Button(self.frameleft, command=self.bl_clicked, height=2, width=2)
        self.bottomleft.pack(pady=10)

        self.framecenter = Frame(self.boardFrame)
        self.framecenter.pack(side='left', padx=10)
        self.topcenter = Button(self.framecenter, command=self.tc_clicked, height=2, width=2)
        self.topcenter.pack(pady=10)
        self.middlecenter = Button(self.framecenter, command=self.mc_clicked, height=2, width=2)
        self.middlecenter.pack(pady=10)
        self.bottomcenter = Button(self.framecenter, command=self.bc_clicked, height=2, width=2)
        self.bottomcenter.pack(pady=10)

        self.frameright = Frame(self.boardFrame)
        self.frameright.pack(side='left', padx=10)
        self.topright = Button(self.frameright, command=self.tr_clicked, height=2, width=2)
        self.topright.pack(pady=10)
        self.middleright = Button(self.frameright, command=self.mr_clicked, height=2, width=2)
        self.middleright.pack(pady=10)
        self.bottomright = Button(self.frameright, command=self.br_clicked, height=2, width=2)
        self.bottomright.pack(pady=10)

        self.ResetButton = Button(window, text='new game', command =self.reset)
        self.ResetButton.place(x=98, y=245)


    def tl_clicked(self):  # top left
        # check if the button is free to click
        if self.tl_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.tl_status = True   # player 1 claimed an x, cant be clicked again
                self.topleft.config(text='X')
                self.p1_turn = False # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.tl_status = False  # player 2 claimed an o, cant be clicked again
                self.topleft.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons

            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw

    def ml_clicked(self):  # middle left
        # check if the button is free to click
        if self.ml_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.ml_status = True  # player 1 claimed an x, cant be clicked again
                self.middleleft.config(text='X')
                self.p1_turn = False  # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.ml_status = False  # player 2 claimed an o, cant be clicked again
                self.middleleft.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons

            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw

    def bl_clicked(self):  # bottomleft
        # check if the button is free to click
        if self.bl_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.bl_status = True  # player 1 claimed an x, cant be clicked again
                self.bottomleft.config(text='X')
                self.p1_turn = False  # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.bl_status = False  # player 2 claimed an o, cant be clicked again
                self.bottomleft.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons

            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw

    def tc_clicked(self):  # top center
        # check if the button is free to click
        if self.tc_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.tc_status = True  # player 1 claimed an x, cant be clicked again
                self.topcenter.config(text='X')
                self.p1_turn = False  # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.tc_status = False  # player 2 claimed an o, cant be clicked again
                self.topcenter.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons

            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw


    def mc_clicked(self):  # middle center
        # check if the button is free to click
        if self.mc_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.mc_status = True  # player 1 claimed an x, cant be clicked again
                self.middlecenter.config(text='X')
                self.p1_turn = False  # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.mc_status = False  # player 2 claimed an o, cant be clicked again
                self.middlecenter.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons

            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw


    def bc_clicked(self):  # bottom center
        # check if the button is free to click
        if self.bc_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.bc_status = True  # player 1 claimed an x, cant be clicked again
                self.bottomcenter.config(text='X')
                self.p1_turn = False  # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.bc_status = False  # player 2 claimed an o, cant be clicked again
                self.bottomcenter.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons

            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw

    def tr_clicked(self):  # top right
        # check if the button is free to click
        if self.tr_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.tr_status = True  # player 1 claimed an x, cant be clicked again
                self.topright.config(text='X')
                self.p1_turn = False  # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.tr_status = False  # player 2 claimed an o, cant be clicked again
                self.topright.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons

            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw


    def mr_clicked(self):  # middle right
        # check if the button is free to click
        if self.mr_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.mr_status = True  # player 1 claimed an x, cant be clicked again
                self.middleright.config(text='X')
                self.p1_turn = False  # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.mr_status = False  # player 2 claimed an o, cant be clicked again
                self.middleright.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons


            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw


    def br_clicked(self):  # bottom right
        # check if the button is free to click
        if self.br_status == None:
            # now check who clicked it and respond accordingly
            if self.p1_turn:
                self.br_status = True  # player 1 claimed an x, cant be clicked again
                self.bottomright.config(text='X')
                self.p1_turn = False  # change player turn
                self.statuslabel.config(text='Player 2\'s turn') # update the status label

            elif self.p1_turn == False:
                self.br_status = False  # player 2 claimed an o, cant be clicked again
                self.bottomright.config(text='O')
                self.p1_turn = True  # change player turn
                self.statuslabel.config(text='Player 1\'s turn') # update the status label

            # check for a winner
            ending_status = self.check_winner()
            if ending_status == True:
                self.statuslabel.config(text='Game Over, Player 1 wins')
                self.end_game() # effectively disable all buttons
            elif ending_status == False:
                self.statuslabel.config(text='Game Over, Player 2 wins')
                self.end_game() # effectively disable all buttons

            # check if all squares used
            elif self.check_full():
                self.statuslabel.config(text='Game Over: Draw') # announce that the game has ended in a draw




    def check_winner(self):
        # check the status of the 8 winning combinations
        winner1 = False
        winner2 = False

        # left vertical
        if (self.tl_status == True) and (self.ml_status == True) and (self.bl_status == True):
            winner1 = True
        elif (self.tl_status == False) and (self.ml_status == False) and (self.bl_status == False):
            winner2 = True

        # middle vertical
        elif (self.tc_status == True) and (self.mc_status == True) and (self.bc_status == True):
            winner1 = True
        elif (self.tc_status == False) and (self.mc_status == False) and (self.bc_status == False):
            winner2 = True

        # right vertical
        elif (self.tr_status == True) and (self.mr_status == True) and (self.br_status == True):
            winner1 = True
        elif (self.tr_status == False) and (self.mr_status == False) and (self.br_status == False):
            winner2 = True

        # top horizontal
        elif (self.tl_status == True) and (self.tc_status == True) and (self.tr_status == True):
            winner1 = True
        elif (self.tl_status == False) and (self.tc_status == False) and (self.tr_status == False):
            winner2 = True

        # middle horizontal
        elif (self.ml_status == True) and (self.mc_status == True) and (self.mr_status == True):
            winner1 = True
        elif (self.ml_status == False) and (self.mc_status == False) and (self.mr_status == False):
            winner2 = True

        # bottom horizontal
        elif (self.bl_status == True) and (self.bc_status == True) and (self.br_status == True):
            winner1 = True
        elif (self.bl_status == False) and (self.bc_status == False) and (self.br_status == False):
            winner2 = True

        # top left to bottom right diagonal
        elif (self.tl_status == True) and (self.mc_status == True) and (self.br_status == True):
            winner1 = True
        elif (self.tl_status == False) and (self.mc_status == False) and (self.br_status == False):
            winner2 = True

        # bottom left to top right diagonal
        elif (self.bl_status == True) and (self.mc_status == True) and (self.tr_status == True):
            winner1 = True
        elif (self.bl_status == False) and (self.mc_status == False) and (self.tr_status == False):
            winner2 = True

        if winner1 == True:
            return True
        elif winner2 == True:
            return False
        else:
            return None

    def check_full(self):
        # check if all 9 squares are full
        if (self.tl_status != None) and (self.ml_status != None) and (self.bl_status != None) and (self.tc_status != None) and (self.mc_status != None) and (self.bc_status != None) and (self.tr_status != None) and (self.mr_status != None) and (self.br_status != None):
            return True
        else:
            return False

    def end_game(self):
        self.tl_status = False  # top left
        self.ml_status = False  # middle left
        self.bl_status = False  # bottom left
        self.tc_status = False  # top center
        self.mc_status = False  # middle center
        self.bc_status = False  # bottom center
        self.tr_status = False  # top right
        self.mr_status = False  # middle right
        self.br_status = False  # bottom right

    def reset(self):
        self.p1_turn = True
        self.statuslabel.config(text='Player 1\'s turn')

        self.tl_status = None  # top left
        self.ml_status = None  # middle left
        self.bl_status = None  # bottom left
        self.tc_status = None  # top center
        self.mc_status = None  # middle center
        self.bc_status = None  # bottom center
        self.tr_status = None  # top right
        self.mr_status = None  # middle right
        self.br_status = None  # bottom right

        self.topleft.config(text='')
        self.middleleft.config(text='')
        self.bottomleft.config(text='')
        self.topcenter.config(text='')
        self.middlecenter.config(text='')
        self.bottomcenter.config(text='')
        self.topright.config(text='')
        self.middleright.config(text='')
        self.bottomright.config(text='')



