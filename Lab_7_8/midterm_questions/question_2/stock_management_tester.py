import unittest
from stock_management import Stock

class TestStockManagementSystem(unittest.TestCase):
    total_score = 0

    @classmethod
    def tearDownClass(cls):
        print(f"\nTotal Score: {cls.total_score:.2f}/35.00")

    def test_initialization_full(self):
        # print('\nstock = Stock("Apple", 3)')
        stock = Stock("Apple", 3)
        self.assertEqual(stock.type, "Apple")
        self.assertEqual(stock.amount, 3)
        TestStockManagementSystem.total_score += 2

    def test_initialization_no_amount(self):
        # print('\nstock = Stock("Apple")')
        stock = Stock("Apple")
        self.assertEqual(stock.type, "Apple")
        self.assertEqual(stock.amount, 0)
        TestStockManagementSystem.total_score += 2

    def test_initialization_non_string_type(self):
        # print('\nStock(1.5)')
        with self.assertRaises(Exception) as context:
            Stock(1.5)
        self.assertEqual(str(context.exception), "Stock type must be a string and cannot be empty.")
        TestStockManagementSystem.total_score += 0.5

    def test_initialization_empty_type(self):
        # print('\nStock("")')
        with self.assertRaises(Exception) as context:
            Stock("")
        self.assertEqual(str(context.exception), "Stock type must be a string and cannot be empty.")
        TestStockManagementSystem.total_score += 0.5

    def test_initialization_non_int_or_float_amount(self):
        # print('\nStock("Apple", "1.5")')
        with self.assertRaises(Exception) as context:
            Stock("Apple", "1.5")
        self.assertEqual(str(context.exception), "Stock amount must be an integer or a float and it should not be negative.")
        TestStockManagementSystem.total_score += 0.5

    def test_initialization_negative_amount(self):
        # print('\nStock("Apple", -5)')
        with self.assertRaises(Exception) as context:
            Stock("Apple", -5)
        self.assertEqual(str(context.exception), "Stock amount must be an integer or a float and it should not be negative.")
        TestStockManagementSystem.total_score += 0.5

    def test_addition_with_stock(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = Stock("Apple", 4)\ns3 = s1 + s2')
        s1 = Stock("Apple", 1)
        s2 = Stock("Apple", 4)
        s3 = s1 + s2
        self.assertEqual(s3.type, "Apple")
        self.assertEqual(s3.amount, 5)
        TestStockManagementSystem.total_score += 1

    def test_addition_with_int(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 + 4')
        s1 = Stock("Apple", 1)
        s2 = s1 + 4
        self.assertEqual(s2.type, "Apple")
        self.assertEqual(s2.amount, 5)
        TestStockManagementSystem.total_score += 0.5

    def test_addition_with_float(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 + 4.5')
        s1 = Stock("Apple", 1)
        s2 = s1 + 4.5
        self.assertEqual(s2.type, "Apple")
        self.assertEqual(s2.amount, 5.5)
        TestStockManagementSystem.total_score += 0.5

    def test_addition_with_stock_no_update_check(self):
        # print('\nstock = Stock("Apple", 1) + Stock("Apple", 4)')
        s1 = Stock("Apple", 1)
        s2 = Stock("Apple", 4)
        s3 = s1 + s2
        self.assertEqual(s1.type, "Apple")
        self.assertNotEqual(s1.amount, 5)
        TestStockManagementSystem.total_score += 1

    def test_addition_with_int_no_update_check(self):
        # print('\nstock = Stock("Apple", 1) + 4')
        s1 = Stock("Apple", 1)
        s2 = s1 + 4
        self.assertEqual(s1.type, "Apple")
        self.assertNotEqual(s1.amount, 5)
        TestStockManagementSystem.total_score += 0.5

    def test_addition_with_float_no_update_check(self):
        # print('\nstock = Stock("Apple", 1) + 4.5')
        s1 = Stock("Apple", 1)
        s2 = s1 + 4.5
        self.assertEqual(s1.type, "Apple")
        self.assertNotEqual(s1.amount, 5.5)
        TestStockManagementSystem.total_score += 0.5

    def test_addition_with_stock_with_different_type(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = Stock("Orange", 4)\ns3 = s1 + s2')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = Stock("Orange", 4)
            s3 = s1 + s2
        self.assertEqual(str(context.exception), f"Stock types cannot be different during the addition of two {s1.__class__} objects.")
        TestStockManagementSystem.total_score += 1

    def test_addition_with_stock_with_negative_value(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 + -3')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = s1 + -3
        self.assertEqual(str(context.exception), f"Addition operator for {s1.__class__} cannot accept negative values.")
        TestStockManagementSystem.total_score += 1

    def test_addition_with_not_excepted_type(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 + "3"')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = s1 + "3"
        self.assertEqual(str(context.exception), f"Addition operator for {s1.__class__} can only support {s1.__class__}, integer, or float.")
        TestStockManagementSystem.total_score += 1

    def test_subtraction_with_stock(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = Stock("Apple", 1)\ns3 = s1 - s2')
        s1 = Stock("Apple", 4)
        s2 = Stock("Apple", 1)
        s3 = s1 - s2
        self.assertEqual(s3.type, "Apple")
        self.assertEqual(s3.amount, 3)
        TestStockManagementSystem.total_score += 1

    def test_subtraction_with_int(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = s1 - 1')
        s1 = Stock("Apple", 4)
        s2 = s1 - 1
        self.assertEqual(s2.type, "Apple")
        self.assertEqual(s2.amount, 3)
        TestStockManagementSystem.total_score += 0.5

    def test_subtraction_with_float(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = s1 - 1.5')
        s1 = Stock("Apple", 4)
        s2 = s1 - 1.5
        self.assertEqual(s2.type, "Apple")
        self.assertEqual(s2.amount, 2.5)
        TestStockManagementSystem.total_score += 0.5

    def test_subtraction_with_stock_no_update_check(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = Stock("Apple", 1)\ns3 = s1 - s2')
        s1 = Stock("Apple", 4)
        s2 = Stock("Apple", 1)
        s3 = s1 - s2
        self.assertEqual(s1.type, "Apple")
        self.assertNotEqual(s1.amount, 3)
        TestStockManagementSystem.total_score += 1

    def test_subtraction_with_int_no_update_check(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = s1 - 1')
        s1 = Stock("Apple", 4)
        s2 = s1 - 1
        self.assertEqual(s1.type, "Apple")
        self.assertNotEqual(s1.amount, 3)
        TestStockManagementSystem.total_score += 0.5

    def test_subtraction_with_float_no_update_check(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = s1 - 1.5')
        s1 = Stock("Apple", 4)
        s2 = s1 - 1.5
        self.assertEqual(s1.type, "Apple")
        self.assertNotEqual(s1.amount, 2.5)
        TestStockManagementSystem.total_score += 0.5

    def test_subtraction_with_stock_with_different_type(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = Stock("Orange", 1)\ns3 = s1 - s2')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 4)
            s2 = Stock("Orange", 1)
            s3 = s1 - s2
        self.assertEqual(str(context.exception), f"Stock types cannot be different during the subtraction of two {s1.__class__} objects.")
        TestStockManagementSystem.total_score += 1

    def test_subtraction_with_stock_with_greater_amount(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = Stock("Apple", 4)\ns3 = s1 - s2')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = Stock("Apple", 4)
            s3 = s1 - s2
        self.assertEqual(str(context.exception), f"{s1.__class__} objects cannot subtract {s1.__class__} objects with amounts greater than its amount.")
        TestStockManagementSystem.total_score += 1

    def test_subtraction_with_stock_with_negative_value(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 - -3')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = s1 - -3
        self.assertEqual(str(context.exception), f"Subtraction operator for {s1.__class__} cannot accept negative values.")
        TestStockManagementSystem.total_score += 1

    def test_subtraction_with_stock_with_greater_amount(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 - 3')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = s1 - 3
        self.assertEqual(str(context.exception), f"{s1.__class__} objects cannot subtract values greater than its amount.")
        TestStockManagementSystem.total_score += 1


    def test_subtraction_with_not_excepted_type(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 - "3"')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = s1 - "3"
        self.assertEqual(str(context.exception), f"Subtraction operator for {s1.__class__} can only support {s1.__class__}, integer, or float.")
        TestStockManagementSystem.total_score += 1

    def test_multiplication_with_int(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = s1 * 2')
        s1 = Stock("Apple", 4)
        s2 = s1 * 2
        self.assertEqual(s2.type, "Apple")
        self.assertEqual(s2.amount, 8)
        TestStockManagementSystem.total_score += 0.5

    def test_multiplication_with_float(self):
        # print('\ns1 = Stock("Apple", 3)\ns2 = s1 * 1.5')
        s1 = Stock("Apple", 3)
        s2 = s1 * 1.5
        self.assertEqual(s2.type, "Apple")
        self.assertEqual(s2.amount, 4.5)
        TestStockManagementSystem.total_score += 0.5

    def test_multiplication_with_int_no_update_check(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = s1 * 2')
        s1 = Stock("Apple", 4)
        s2 = s1 * 2
        self.assertEqual(s1.type, "Apple")
        self.assertNotEqual(s1.amount, 8)
        TestStockManagementSystem.total_score += 0.5

    def test_multiplication_with_float_no_update_check(self):
        # print('\ns1 = Stock("Apple", 3)\ns2 = s1 * 1.5')
        s1 = Stock("Apple", 3)
        s2 = s1 * 1.5
        self.assertEqual(s1.type, "Apple")
        self.assertNotEqual(s1.amount, 4.5)
        TestStockManagementSystem.total_score += 0.5

    def test_multiplication_with_stock_with_negative_value(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 * -3')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = s1 * -3
        self.assertEqual(str(context.exception), f"Multiplication operator for {s1.__class__} cannot accept negative values.")
        TestStockManagementSystem.total_score += 1


    def test_multiplication_with_not_excepted_type(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = Stock("Apple", 1)\ns3 = s1 * s2')
        with self.assertRaises(Exception) as context:
           s1 = Stock("Apple", 4)
           s2 = Stock("Apple", 1)
           s3 = s1 * s2
        self.assertEqual(str(context.exception), f"Multiplication operator for {s1.__class__} can only support integer or float.")
        TestStockManagementSystem.total_score += 1

    def test_less_than_with_stock_less(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = Stock("Apple", 4)\ncondition = s1 < s2')
        s1 = Stock("Apple", 1)
        s2 = Stock("Apple", 4)
        condition = s1 < s2
        self.assertEqual(condition, True)
        TestStockManagementSystem.total_score += 1

    def test_less_than_with_int_less(self):
        # print('\ns1 = Stock("Apple", 1)\ncondition = s1 < 4')
        s1 = Stock("Apple", 1)
        condition = s1 < 4
        self.assertEqual(condition, True)
        TestStockManagementSystem.total_score += 0.5

    def test_less_than_with_float_less(self):
        # print('\ns1 = Stock("Apple", 1)\ncondition = s1 < 4.5')
        s1 = Stock("Apple", 1)
        condition = s1 < 4.5
        self.assertEqual(condition, True)
        TestStockManagementSystem.total_score += 0.5

    def test_less_than_with_stock_equal(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = Stock("Apple", 1)\ncondition = s1 < s2')
        s1 = Stock("Apple", 1)
        s2 = Stock("Apple", 1)
        condition = s1 < s2
        self.assertEqual(condition, False)
        TestStockManagementSystem.total_score += 0.5

    def test_less_than_with_int_equal(self):
        # print('\ns1 = Stock("Apple", 1)\ncondition = s1 < 1')
        s1 = Stock("Apple", 1)
        condition = s1 < 1
        self.assertEqual(condition, False)
        TestStockManagementSystem.total_score += 0.25

    def test_less_than_with_float_equal(self):
        # print('\ns1 = Stock("Apple", 1)\ncondition = s1 < 1.5')
        s1 = Stock("Apple", 1.5)
        condition = s1 < 1.5
        self.assertEqual(condition, False)
        TestStockManagementSystem.total_score += 0.25

    def test_less_than_with_stock_greater(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = Stock("Apple", 1)\ncondition = s1 < s2')
        s1 = Stock("Apple", 4)
        s2 = Stock("Apple", 1)
        condition = s1 < s2
        self.assertEqual(condition, False)
        TestStockManagementSystem.total_score += 0.5

    def test_less_than_with_int_greater(self):
        # print('\ns1 = Stock("Apple", 4)\ncondition = s1 < 1')
        s1 = Stock("Apple", 4)
        condition = s1 < 1
        self.assertEqual(condition, False)
        TestStockManagementSystem.total_score += 0.25

    def test_less_than_with_float_greater(self):
        # print('\ns1 = Stock("Apple", 4)\ncondition = s1 < 1.5')
        s1 = Stock("Apple", 4)
        condition = s1 < 1.5
        self.assertEqual(condition, False)
        TestStockManagementSystem.total_score += 0.25

    def test_less_than_with_stock_with_different_type(self):
        # print('\ns1 = Stock("Apple", 4)\ns2 = Stock("Orange", 1)\ncondition = s1 < s2')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 4)
            s2 = Stock("Orange", 1)
            s3 = s1 < s2
        self.assertEqual(str(context.exception), f"Stock types cannot be different while comparing two {s1.__class__} objects.")
        TestStockManagementSystem.total_score += 1


    def test_less_than_with_not_excepted_type(self):
        # print('\ns1 = Stock("Apple", 1)\ns2 = s1 - "3"')
        with self.assertRaises(Exception) as context:
            s1 = Stock("Apple", 1)
            s2 = s1 < "3"
        self.assertEqual(str(context.exception), f"Less than operator for {s1.__class__} can only support {s1.__class__}, integer, or float.")
        TestStockManagementSystem.total_score += 1

    def test_string_with_int_amount(self):
        # print('\ns1 = Stock("Apple", 4)\nstr_s1 = str(s1)')
        s1 = Stock("Apple", 4)
        str_s1 = str(s1)
        self.assertEqual(str_s1, "A stock of Apple with the amount of 4.00")
        TestStockManagementSystem.total_score += 1

    def test_string_with_one_digit_float_amount(self):
        # print('\ns1 = Stock("Apple", 4.5)\nstr_s1 = str(s1)')
        s1 = Stock("Apple", 4.5)
        str_s1 = str(s1)
        self.assertEqual(str_s1, "A stock of Apple with the amount of 4.50")
        TestStockManagementSystem.total_score += 1

    def test_string_with_two_digit_float_amount(self):
        # print('\ns1 = Stock("Apple", 4.55)\nstr_s1 = str(s1)')
        s1 = Stock("Apple", 4.55)
        str_s1 = str(s1)
        self.assertEqual(str_s1, "A stock of Apple with the amount of 4.55")
        TestStockManagementSystem.total_score += 1

    def test_string_with_more_digit_float_amount(self):
        # print('\ns1 = Stock("Apple", 4.55555555)\nstr_s1 = str(s1)')
        s1 = Stock("Apple", 4.55555555)
        str_s1 = str(s1)
        self.assertEqual(str_s1, "A stock of Apple with the amount of 4.56")
        TestStockManagementSystem.total_score += 1

if __name__ == "__main__":
    unittest.main()
