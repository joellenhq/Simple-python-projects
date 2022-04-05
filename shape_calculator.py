class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.height>50 or self.width>50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        if i == 0 or i == self.height - 1:
          picture = picture + "".ljust(self.width,"*") + "\n"
        else:
          picture = picture + "".ljust(self.width,"*") + "\n"
      print(picture)
    return picture

  def get_amount_inside(self, shape):
    w = self.width//shape.width
    h = self.height//shape.height
    return w*h


class Square(Rectangle):
  def __init__(self, lenght):
    self.width = lenght
    self.height = lenght
    Rectangle.__init__(self, self.width, self.height)

  def set_side(self, lenght):
    self.width = lenght
    self.height = lenght
  
  def __repr__(self):
    return f"Square(side={self.width})"
  
  def set_width(self,width):
    self.width = width
    self.height = width

  def set_height(self,height):
    self.height = height
    self.width = height
