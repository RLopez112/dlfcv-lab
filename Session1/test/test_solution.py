from Session1.solution import adding_two_numbers


def test_adding_two_numbers():
    # Test basic addition of positive numbers
    assert adding_two_numbers(2, 3) == 5

    # Test with negative numbers
    assert adding_two_numbers(-1, 1) == 0
    assert adding_two_numbers(-2, -3) == -5

    # Test with zero
    assert adding_two_numbers(0, 5) == 5
    assert adding_two_numbers(0, 0) == 0

    # Test with floating point numbers
    assert adding_two_numbers(1.5, 2.5) == 4.0
    assert abs(adding_two_numbers(0.1, 0.2) - 0.3) < 1e-10  # Handle floating point precision
