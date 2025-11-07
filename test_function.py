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


def test_sine_time_shifting():
    t, y = sine_time_shifting(f=1, A=1, shift=0)
    assert np.allclose(y, np.sin(2*np.pi*t))
    
    t, y = sine_time_shifting(f=1, A=2, shift=0.25)
    expected = 2*np.sin(2*np.pi*(t-0.25))
    assert np.allclose(y, expected)
    
    t, y = sine_time_shifting(f=1, A=0, shift=1)
    assert np.allclose(y, 0)


def test_sine_time_scaling():
    t, y = sine_time_scaling(f=1, A=1, scale=1)
    assert np.allclose(y, np.sin(2*np.pi*t))
    
    t, y = sine_time_scaling(f=1, A=2, scale=2)
    expected = 2*np.sin(2*np.pi*(t*2))
    assert np.allclose(y, expected)
    
    t, y = sine_time_scaling(f=1, A=0, scale=0.5)
    assert np.allclose(y, 0)


def test_generate_unit_step():
    t, y = generate_unit_step(t0=1, A=1)
    assert len(t) == 1000
    assert len(y) == 1000
    assert np.allclose(y[t < 1], 0)
    assert np.allclose(y[t > 1], 1)
    
    t, y = generate_unit_step(t0=0, A=2)
    assert np.allclose(y[t >= 0], 2)
    
    t, y = generate_unit_step(t0=2, A=0)
    assert np.allclose(y, 0)


def test_unit_step_time_shifting():
    t, y = unit_step_time_shifting(t0=1, A=1, shift=0)
    expected_t, expected_y = generate_unit_step(t0=1, A=1)
    assert np.allclose(y, expected_y)
    
    t, y = unit_step_time_shifting(t0=1, A=2, shift=0.5)
    assert np.allclose(y[(t-0.5) < 1], 0)
    assert np.allclose(y[(t-0.5) > 1], 2)
    
    t, y = unit_step_time_shifting(t0=1, A=0, shift=1)
    assert np.allclose(y, 0)