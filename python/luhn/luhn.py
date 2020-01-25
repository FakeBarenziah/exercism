import re

class Luhn:
    def __init__(self, card_num):
        # Remove spaces from input
        regex = re.compile(r'\s')
        self.card_num = "".join(regex.split(card_num))
        
        # Check if non-digit chars are left and set a property with the result
        nondigit_search = re.compile(r'[^0-9]')
        self.invalid_input = nondigit_search.search(self.card_num)

    def valid(self):

        # Auto-fails for short strings and non-number, non-space chars
        if len(self.card_num) < 2:
            return False

        if not self.invalid_input == None:
            return False

        # Traverse string starting at the end and mutate values as necessary
        digits = []
        i = len(self.card_num) - 1
        swap = False

        while i >= 0:
            this_digit = int(self.card_num[i])
            if swap == True:
                this_digit = (this_digit * 2)
                if this_digit > 9:
                    this_digit -= 9
                swap = False
            else:
                swap = True
            digits.append(this_digit)
            i -= 1

        return sum(digits) % 10 == 0