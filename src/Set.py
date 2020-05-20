## @file Set.py
#  @author Dimitri Tsampiras
#  @brief Defines a generic template module for sets
#  @date Februrary 6, 2020

from Equality import Equality

## @brief Set Template class
#  @details Inherits Equality


class Set(Equality):

  ## @brief Constructor for set class
  #  @param s Sequence of a generic type
  def __init__(self, s):
    self.S = set(s)

  ## @brief Adds an element to the set
  #  @param e element of the same type as set elements
  def add(self, e):
    self.S.add(e)

  ## @brief Removes an element from the set
  #  @details Will raise a value error if the element is not in the set
  #  @param e element of the same type as set elements
  def rm(self, e):
    try:
      self.S.remove(e)
    except KeyError:
      raise ValueError

  ## @brief Determines if element is in the set
  #  @param e element of the same type as set elements
  #  @return Returns true if element is in the set, false otherwise
  def member(self, e):
    return e in self.S

  ## @brief Determines the sets length
  #  @return The length of the set
  def size(self):
    return len(self.S)

  ## @brief Determines if referenced set is equal to another set
  #  @param R A set of elements
  #  @return Returns true is R is equal to the refenced set
  def equals(self, R):
    return self.S == set(R.to_seq())

  ## @brief Magic function that determines if referenced set is equal to another set
  #  @details called when equality operator is used between set
  #  @param R A set of elements
  #  @return Returns true is R is equal to the refenced set
  def __eq__(self, R):
    return self.S == set(R.to_seq())

  ## @brief Returns a sequence of all the elements in the set
  #  @return Returns a python list of set elements
  def to_seq(self):
    return list(self.S)

  ## @brief Magic function that initializes index variable for iteration
  #  @details initializes self.index field to 0
  #  @return Returns self
  def __iter__(self):
      self.index = 0
      return self

  ## @brief Magic function that makes Set obeject iterable
  #  @details called when Set object is iterated over
  #  @return Returns the element of the iteration
  def __next__(self):
      if self.index < self.size():
          element = self.to_seq()[self.index]
          self.index += 1
          return element
      else:
          raise StopIteration
