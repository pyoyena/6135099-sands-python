import numpy as np
import matplotlib.pyplot as plt

def test_generate_sine():
    t, y = generate_sine(f=1, A=2)
    assert len(t) == 1000
    assert len(y) == 1000
    assert np.isclose(y[0], 0, atol=1e-6)

    t, y = generate_sine(f=1, A=3)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = generate_sine(f=1, A=0)
    assert np.allclose(y, 0)

    t, y = generate_sine(f=10, A=1)
    assert len(y) == 1000