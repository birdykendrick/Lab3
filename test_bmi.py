import lab2.bmi as bmi

# Triple AAA pattern

# Arrange (Set up the test conditions)
# Act (Call the function)
# Assert (Verify the results)

def test_bmi_overweight_weight():
    # Arrange
    height = 1.80
    weight = 88

    # Act
    result = bmi.calculate_bmi(height, weight)

    #Assert
    assert result == 1

def test_bmi_under_weight():
    # Arrange
    height = 1.80
    weight = 50

    # Act
    result = bmi.calculate_bmi(height, weight)

    #Assert
    assert result == -1

def test_bmi_normal_weight():
    # Arrange
    height = 1.80
    weight = 70

    # Act
    result = bmi.calculate_bmi(height, weight)

    #Assert
    assert result == 0

