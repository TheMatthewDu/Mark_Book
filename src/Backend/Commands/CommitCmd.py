from src.Backend.Commands.AbstractClasses.NeedsData import NeedsData

import json


class CommitCmd(NeedsData):
    """ A command to commit MarkBook changes to the file """

    def run(self) -> None:
        """ Writes the data into the specified file

        :return: None
        """
        storage_file = open(f"src\\DataFiles\\Data\\{self.data.name}.json", 'w')
        weights_file = open(f"src\\DataFiles\\Weights\\{self.data.name}_weights.json", 'w')

        json.dump(self.data.get_data(), storage_file)
        json.dump(self.data.get_weights(), weights_file)

        storage_file.close()
        weights_file.close()

        self.set_overall()

    def set_overall(self):
        """ Update the Overall file """
        # Write the info to file
        data = self.get_analysis()

        output = open("src\\Backend\\Overall Averages.txt", 'w')
        output.write(data)
        output.flush()
        output.close()

    def get_analysis(self) -> str:
        """ Reads the current analysis and returns the updated information.

        :return: A string of the contents of the analysis file
        """
        input_file = open("src\\Backend\\Overall Averages.txt", 'r')

        complete_output = ""
        total_average = 0
        num_entries = 0
        has_written = False

        # For each entry line
        for line in input_file.readlines()[:-2]:
            line_elements = line.split(sep=": ")

            # If the name of the entry is the name of the MarkBook
            if line_elements[0] == self.data.name:
                complete_output += f"{self.data.name}: {round(self.data.get_current_mark(), 2)}\n"
                total_average += self.data.get_current_mark()
                has_written = True
            else:
                complete_output += line
                total_average += float(line_elements[1])
            num_entries += 1

        # If none of the names match, it is a new course. Hence, Write it
        if not has_written:
            complete_output += f"{self.data.name}: {round(self.data.get_current_mark(), 2)}\n"
            total_average += self.data.get_current_mark()
            num_entries += 1

        total_average = total_average / num_entries
        complete_output += f'OVERALL AVERAGE: {round(total_average, 2)}\n'
        if round(total_average, 2) < 85:
            complete_output += f'Danger! Below Goal by {round(85 - total_average, 2)}%\n'
        else:
            complete_output += f'Good. Above Goal by {round(total_average - 85, 2)}%\n'

        input_file.close()
        return complete_output

