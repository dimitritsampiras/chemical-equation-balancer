## @file Equality.py
#  @author Dimitri Tsampiras
#  @brief Defines an abstract base class for Equality
#  @date Februrary 6, 2020

from abc import ABC, abstractmethod

## @breif Equality abstract class
#  @details Inherits Python's abstract base class


class Equality(ABC):

  ## @brief Abstract method for equality
  #  @param t generic type
  @abstractmethod
  def equals(self, t):
    pass
