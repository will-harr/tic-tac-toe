from gui import *

def main():
    window = Tk()
    window.title('Tic Tac Toe')
    window.geometry('300x300')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()