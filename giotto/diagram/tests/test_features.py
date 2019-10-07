"""Testing for PersistentEntropy"""

import numpy as np
import pytest
from numpy.testing import assert_almost_equal
from sklearn.exceptions import NotFittedError

from giotto.diagram import PersistentEntropy

X_pe = np.array([[[0, 1, 0], [2, 3, 0],[4, 6, 1], [2, 6,1]]])


def test_pe_not_fitted():
    pe = PersistentEntropy()

    with pytest.raises(NotFittedError):
        pe.transform(X_pe)


def test_pe_transform():
    pe = PersistentEntropy()
    X_pe_res = np.array([[0.69314718, 0.63651417]])

    assert_almost_equal(pe.fit_transform(X_pe), X_pe_res)