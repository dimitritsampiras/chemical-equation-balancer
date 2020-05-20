## @file CompoundT.py
#  @author Dimitri Tsampiras
#  @brief Defines a template module for Compounds
#  @date Februrary 6, 2020

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet

## @breif Compound Template class
#  @details Inherits ChemEntity and Equality Modules


class CompoundT(ChemEntity, Equality):
  ## @brief Constructor for compound class
  #  @param M set of molecules
  def __init__(self, M):
    self.C = M

  ## @brief Getter that returns the set of molecules
  #  @return Returns reference molecule set
  def get_molec_set(self):
    return self.C

  ## @brief Determines the number of a given element in the compound
  #  @param e element
  #  @return Returns number of e in the compound
  def num_atoms(self, e):
    num_atoms = 0
    for m in self.C.to_seq():
      num_atoms += m.num_atoms(e)
    return num_atoms

  ## @brief Determines the elements in the compound
  #  @return Returns a set of each element in the compound
  def constit_elems(self):
    elm_set = ElmSet([])
    for m in self.C.to_seq():
      elm_set.add(m.get_elm())
    return elm_set

  ## @brief Compares a compound with reference fields
  #  @param D CompoundT object
  #  @return Returns true if the compounds are equal, false otherwise
  def equals(self, D):
    return self.C == D.get_molec_set()
