## @file ChemEntity.py
#  @author Dimitri Tsampiras
#  @brief Defines an abstract base class for a chemical entity
#  @date Februrary 6, 2020

from abc import ABC, abstractmethod

## @breif Chemical Entitiy abstract class
#  @details Inherits Python's abstract base class


class ChemEntity(ABC):
  ## @brief Abstract method for atom number
  #  @details Defines an abstract method for the amount of atoms in the chemical entity
  #  @param ElementT object
  @abstractmethod
  def num_atoms(self, e):
    pass

  ## @brief Abstract method for constituent elements
  #  @details Defines an abstract method for the chemical elements components (elements)
  @abstractmethod
  def constit_elems(self):
    pass
