from src.monte_carlo import simulate_system


def test_simulate_system():
    N = 100
    t = 5

    reliability, success, failure = simulate_system(N, t)

    assert success + failure == N
    assert reliability == success / N
    assert 0 <= reliability <= 1