from tkinter import *
from typing import List, Tuple
from src.GUI.AbstractScreen import AbstractScreen


class AnalysisScreen(AbstractScreen):
    """ Create a table object

    === Public Attributes ===
    entry: tkinker Entry
    """
    entry: Entry

    def __init__(self, lst: List[Tuple[str, str]]):
        """ Initializer

        Precondition: lst is a valid input where the first entry is the title
        """
        AbstractScreen.__init__(self)

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
                        Entry(self.window, width=20, fg='Black',
                              font=('Arial', 16, "bold"))
                # Entry
                else:
                    self.entry = Entry(self.window, width=20, fg='Black',
                                       font=self.font)
                # Create the table
                self.entry.grid(row=i, column=j)
                self.entry.insert(END, lst[i][j])

        button = \
            Button(self.window, text="Exit", font=self.button_font,
                   command=self.window.destroy)
        button.grid(row=total_rows, column=total_columns)
