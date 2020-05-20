## @file MoleculeT.py
#  @author Dimitri Tsampiras
#  @brief Defines a template module for Molecules
#  @date Februrary 6, 2020

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet

## @breif Molecule Template class
#  @details Inherits ChemEntity and Equality Modules


class MoleculeT(ChemEntity, Equality):

  ## @brief Constructor for set class
  #  @param n number of type Natural
  #  @param e ElementT element
  def __init__(self, n, e):
    self.num = n
    self.elm = e

  ## @brief Getter that returns the number of elements
  #  @return Returns num field of reference object
  def get_num(self):
    return self.num

  ## @brief Getter that returns the element
  #  @return Returns elm field of reference object
  def get_elm(self):
    return self.elm

  ## @brief Determines the number of elements
  #  @param e element
  #  @return Returns the number of elements if the element matches the reference type
  def num_atoms(self, e):
    return (0, self.get_num())[e == self.get_elm()]

  ## @brief Creates a set of type ElmSet of the refernece element(s)
  #  @return Returns ElmSet of the refernece element(s)
  def constit_elems(self):
    return ElmSet([self.get_elm()])

  ## @brief Compares molecule with reference fields
  #  @param m MoleculeT object
  #  @return Returns true if molecules are equal, false otherwise
  def equals(self, m):
    return self.get_num() == m.get_num() and self.get_elm() == m.get_elm()
