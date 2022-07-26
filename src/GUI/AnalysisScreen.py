import tkinter as tkt
from typing import List, Tuple
from src.GUI.AbstractScreen import AbstractScreen
from src.GUI.GUIController import GUIController


class AnalysisScreen(AbstractScreen):
    """ Create a table object

    === Public Attributes ===
    :ivar entry: tkinker Entry
    """
    entry: tkt.Entry

    def __init__(self, controller: GUIController):
        """ Initializer

        Precondition: lst is a valid input where the first entry is the title
        """
        AbstractScreen.__init__(self)

        self.controller = controller

        data = self.controller.generate_analysis().split(sep='\n')
        analysis_message = data.pop(-1)
        lst = [item.split(sep=': ') for item in data if item != '']

        # Get the table size
        total_rows = len(lst)
        total_columns = len(lst[0])

        # For each row
        for i in range(total_rows):

            # For each column in each row
            for j in range(total_columns):

                # Title
                if i == 0:
                    self.entry = \
                        tkt.Entry(self.window, width=20, fg='Black',
                                  font=('Arial', 16, "bold"))
                # Entry
                else:
                    self.entry = tkt.Entry(self.window, width=20, fg='Black', font=self.font)
                # Create the table
                self.entry.grid(row=i, column=j)
                self.entry.insert(tkt.END, lst[i][j])

        self.entry = tkt.Entry(self.window, width=20, fg='Black', font=self.font)
        self.entry.insert(tkt.END, analysis_message)
        self.entry.grid(row=total_rows, column=total_columns - 2)

        button = \
            tkt.Button(self.window, text="Exit", font=self.button_font,
                       command=self.window.destroy)
        button.grid(row=total_rows, column=total_columns - 1)
