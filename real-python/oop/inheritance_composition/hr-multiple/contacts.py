class Address:
    def __init__(self, street, city, state, zip_code, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        """used to obtain a string represetation of the current object"""
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zip_code}')
        return '\n'.join(lines)


if __name__ == '__main__':
    address = Address("123 Rabbit Street", "Chicago", "IL", 60610)
    print(address)
