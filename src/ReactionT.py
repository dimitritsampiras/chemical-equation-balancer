## @file ReactionT.py
#  @author Dimitri Tsampiras
#  @brief Defines a template module for Chemical Reactions
#  @date Februrary 6, 2020

import numpy as np
import sympy as sp


## @breif Reaction Template class
class ReactionT:

  ## @brief Constructor for reaction class
  #  @param L left side of reaction
  #  @param R right side of reaction
  def __init__(self, L, R):
    self.lhs = L
    self.rhs = R
    lhs_set = set([])
    rhs_set = set([])

    for cmp in self.lhs:
      lhs_set = lhs_set.union(set(cmp.constit_elems().to_seq()))

    for cmp in self.rhs:
      rhs_set = rhs_set.union(set(cmp.constit_elems().to_seq()))

    num_cmps = len(self.lhs) + len(self.rhs)
    num_elems = len(lhs_set)

    clm_len = num_cmps + 1
    row_len = num_elems + max((num_cmps - num_elems), 0)

    matrix = np.zeros([row_len, clm_len])

    equation = self.lhs + self.rhs

    row = 0
    clmn = 0
    counter = 0
    for elem in list(lhs_set):
      for cmp in equation:
        matrix[row][clmn] = cmp.num_atoms(elem)
        if counter >= len(self.lhs):
          matrix[row][clmn] *= -1
        clmn += 1
        counter += 1
      row += 1
      clmn = 0
      counter = 0

    for i in range(max((num_cmps - num_elems), 0)):
      for j in range(clm_len):
        if (clmn == i):
          matrix[row][clmn] = 1
        if (j == clm_len - 1):
          matrix[row][j] = 1

    reduced_matrix = sp.Matrix(matrix).rref()[0]

    coeffs = reduced_matrix.col(-1)

    lhs_coeff = []
    rhs_coeff = []
    for i in range(len(self.lhs)):
      lhs_coeff.append(coeffs[i])
    for i in range(len(self.rhs)):
      rhs_coeff.append(coeffs[i + len(self.lhs)])

    self.coeffL = lhs_coeff
    self.coeffR = rhs_coeff

  ## @brief Getter that returns the left hand side of the reaction instance
  #  @return Returns the lhs field
  def get_lhs(self):
    return self.lhs

  ## @brief Getter that returns the right hand side of the reaction instance
  #  @return Returns the rhs field
  def get_rhs(self):
    return self.rhs

  ## @brief Getter that returns the coefficients of the left hand side of the equation
  #  @return Returns the coeffL field
  def get_lhs_coeff(self):
    return self.coeffL

  ## @brief Getter that returns the coefficients of the right hand side of the equation
  #  @return Returns the coeffR field
  def get_rhs_coeff(self):
    return self.coeffR
