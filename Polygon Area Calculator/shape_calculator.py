class Rectangle():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50:
            return 'Too big for picture.'
        picture = ''
        for _ in range(self.height):
            picture += (self.width * '*' + '\n')
        return picture

    def get_amount_inside(self, another_shape) -> int:
        '''
        Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations)
        '''
        return self.get_area() // another_shape.get_area()

class Square(Rectangle):
    
    def __init__(self, side) -> None:
        super().__init__(side, side)
    
    def __repr__(self) -> str:
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side
