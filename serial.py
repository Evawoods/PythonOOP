"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """Making a new generator that starts at 0 """

        self.start = start
        self.next = start + 1
    
    def __repr__(self):
        """Show representation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        """Return next serial"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """reset number to original start"""
        self.next = self.start

