## @file test_ALl.py
#  @author Dimitri Tsampiras
#  @brief Testing file for Chemical Balancing Program
#  @date Februrary 7, 2020

from ChemTypes import ElementT
from Set import *
from ElmSet import *
from MolecSet import *
from MoleculeT import *
from CompoundT import *
from ReactionT import *


# Global varibale declarations
test_set = Set([1, 2, 3, 4, 5])

oxygen3 = MoleculeT(3, ElementT.O)
iron1 = MoleculeT(1, ElementT.Fe)
carbon1 = MoleculeT(1, ElementT.C)
iron2 = MoleculeT(2, ElementT.Fe)
oxygen2 = MoleculeT(2, ElementT.O)
oxygen1 = MoleculeT(1, ElementT.O)
hydrogen2 = MoleculeT(2, ElementT.H)

iron_oxide = CompoundT(MolecSet([iron2, oxygen3]))
carbon = CompoundT(MolecSet([carbon1]))
iron = CompoundT(MolecSet([iron1]))
carbon_oxide = CompoundT(MolecSet([carbon1, oxygen2]))
hydrogendioxide = CompoundT(MolecSet([hydrogen2, oxygen1]))

reaction1 = ReactionT([iron_oxide, carbon], [iron, carbon_oxide])
reaction2 = ReactionT([hydrogen2, oxygen2], [hydrogendioxide])


# testing Set
def test_add():
  test_set.add(6)
  assert test_set == Set([1, 2, 3, 4, 5, 6])


def test_rm():
  test_set.rm(6)
  test_set.rm(1)
  assert test_set == Set([2, 3, 4, 5])

  try:
    test_set.rm(10)
  except ValueError:
    assert True


def test_member():
  assert test_set.member(3)
  assert not test_set.member(8)


def test_size():
  assert test_set.size() == 4
  assert test_set.size() != 10


def test_equals_set():
  test_set2 = Set([2, 3, 4, 5])
  for i in test_set2.to_seq():
    assert test_set.member(i)
  for i in test_set.to_seq():
    assert test_set2.member(i)


def test_to_seq():
  assert test_set.to_seq() == [2, 3, 4, 5]
  assert test_set.to_seq() != [9, 9, 9, 9]


# testing ElementT


def create_elements():
  assert ElementT.O == ElementT.O
  assert ElementT.H != ElementT.He


# testing MoleculeT


def test_get_num():
  assert oxygen3.get_num() == 3
  assert oxygen3.get_num() != 2


def test_get_elem():
  assert oxygen3.get_elm() == ElementT.O
  assert oxygen3.get_elm() != ElementT.He


def test_num_atoms_mol():
  assert oxygen3.num_atoms(ElementT.O) == 3
  assert oxygen3.num_atoms(ElementT.H) == 0


def test_constit_elems_mol():
  assert oxygen3.constit_elems() == ElmSet([ElementT.O])
  assert oxygen3.constit_elems() != ElmSet([ElementT.H])


def test_equals_mol():
  assert oxygen3.equals(MoleculeT(3, ElementT.O))
  assert not oxygen3.equals(MoleculeT(3, ElementT.H))


# testing CompoundT


def test_get_molec_set():
  assert iron_oxide.get_molec_set() == MolecSet([iron2, oxygen3])
  assert iron_oxide.get_molec_set() != MolecSet([ElementT.H, ElementT.Tc])


def test_num_atoms_cmp():
  assert iron_oxide.num_atoms(ElementT.Fe) == 2
  assert iron_oxide.num_atoms(ElementT.O) == 3
  assert iron_oxide.num_atoms(ElementT.C) == 0


def test_constit_elems_cmp():
  assert iron_oxide.constit_elems() == ElmSet([ElementT.Fe, ElementT.O])
  assert iron_oxide.constit_elems() != ElmSet([ElementT.H, ElementT.O])


def test_equals_cmp():
  assert iron_oxide.equals(CompoundT(MolecSet([iron2, oxygen3])))
  assert not iron_oxide.equals(CompoundT(MolecSet([MoleculeT(2, ElementT.H), oxygen3])))


# testing ReactionT


def test_getters():
  assert reaction1.get_lhs() == [iron_oxide, carbon]
  assert reaction1.get_rhs() == [iron, carbon_oxide]

  assert reaction2.get_lhs() == [hydrogen2, oxygen2]
  assert reaction2.get_rhs() == [hydrogendioxide]

  assert reaction1.get_lhs_coeff() == [1.0, 1.5]
  assert reaction1.get_rhs_coeff() == [2.0, 1.5]
  assert reaction1.get_lhs_coeff() != [2.0, 3.0]
  assert reaction1.get_rhs_coeff() != [4.0, 3.0]

  assert reaction2.get_lhs_coeff() == [1.0, 0.5]
  assert reaction2.get_rhs_coeff() == [1.0]
  assert reaction2.get_lhs_coeff() != [2.0, 3.0]
  assert reaction2.get_rhs_coeff() != [4.0, 3.0]
