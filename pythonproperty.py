# decorator used to define a method as a property (it can be accessed like an attribute)
#           benefits: add additional logic when read, write or delete attributes
#           Gives you getter, setter, and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"



    @property
    def heigh(self):
        return f"{self._height:.1f}cm"
    



    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than 0")


    @heigh.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than 0")

    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")


    @height.deleter
    def height(self):
        del self.height
        print("Height has been deleted")



rectangle = Rectangle(3,4)




del Rectangle.width
del Rectangle.height

print(Rectangle.width)
print(Rectangle.height)