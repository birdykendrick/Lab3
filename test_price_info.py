import price_info

print("Testing of price info")

def test_total_shopping_cost():
    expeceted_result = 46.75

    #Act
    result = price_info.total_cost_shopping()

    #assert
    assert result == expeceted_result

def test_cost_of_fruits():
    # Arrange
    fruit_name = 'apple'
    quantity = 10
    expected_result = 12.0

    #act``
    result = price_info.cost_of_fruits(fruit_name, quantity)

    #assert
    assert result == expected_result

def test_average():
    result = []