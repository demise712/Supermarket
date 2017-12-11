#!/usr/bin/env python

import supermarket_register
import unittest

class TestSupermarketRegister(unittest.TestCase):

    #Test the SupermarketRegister class.
    def _mock_supermarket_instance(self):
        p_codes = {
                'XXXX-XXXX-XXXX-XXXX': {
                    'product': 'a',
                    'price': 1
                }
        }
        return supermarket_register.SupermarketRegister(p_codes)

#Test initializing an instance
    def test_init(self):

        sm = self._mock_supermarket_instance()
        self.assertIs(type(sm),supermarket_register.SupermarketRegister)

        # Test invalid product code initialization
        p_codes = {
                'XXXX-XXXX-XXXX-XXX*': {
                    'product': 'a',
                    'price': 1
                }
        }
        with self.assertRaises(ValueError):
            supermarket_register.SupermarketRegister(p_codes)

        # Test invalid price initialization
        p_codes = {
                'XXXX-XXXX-XXXX-XXXX': {
                    'product': 'a',
                    'price': -1
                }
        }
        with self.assertRaises(ValueError):
            supermarket_register.SupermarketRegister(p_codes)

#Test input of the Product
    def test_add_product(self):
        sm = self._mock_supermarket_instance()
        product = {
                'BBBB-BBBB-BBBB-BBBB': {
                    'product': 'b',
                    'price': 2
                }
        }
        sm.add_product(product)
        # Test product is added
        self.assertEqual(
                sm.p_codes['BBBB-BBBB-BBBB-BBBB'],
                    { 'product': 'b', 'price': 2 }
                )

        # Test KeyError is raised if product already exists
        with self.assertRaises(KeyError):
            sm.add_product(product)

#Test remove of the product
    def test_remove_product(self):

        sm = self._mock_supermarket_instance()
        product = {
                'XXXX-XXXX-XXXX-XXXX': {
                    'product': 'a',
                    'price': 1
                }
        }
        sm.remove_product('XXXX-XXXX-XXXX-XXXX')
        # Test product is removed
        self.assertTrue('XXXX-XXXX-XXXX-XXXX' not in sm.p_codes)

        # Test KeyError is raised if product does not exists.
        with self.assertRaises(KeyError):
            sm.remove_product('XXXX-XXXX-XXXX-XXXX')

#Test total cost of the products
    def test_total_cost(self):

        p_codes = {
                'XXXX-XXXX-XXXX-XXXX': {
                    'product': 'x',
                    'price': 1
                },
                'YYYY-YYYY-YYYY-YYYY': {
                    'product': 'y',
                    'price': 1.12
                },
                'ZZZZ-ZZZZ-ZZZZ-ZZZZ': {
                    'product': 'z',
                    'price': 2.345
                },
                'AAAA-AAAA-AAAA-AAAA': {
                    'product': 'a',
                    'price': '1'
                }
        }
        sm = supermarket_register.SupermarketRegister(p_codes)
        # Test single item
        self.assertEqual(
                sm.total_cost('xxxx-xxxx-xxxx-xxxx'),
                round(1+(1*sm.local_sales_tax),2)
                )

        # Test different spacing in input string
        self.assertEqual(
                sm.total_cost('xxxx-xxxx-xxxx-xxxx;YYYY-YYYY-YYYY-YYYY'),
                round((1+1.12)+((1+1.12)*sm.local_sales_tax),2)
                )
        self.assertEqual(
                sm.total_cost('xxxx-xxxx-xxxx-xxxx; YYYY-YYYY-YYYY-YYYY'),
                round((1+1.12)+((1+1.12)*sm.local_sales_tax),2)
                )
        self.assertEqual(
                sm.total_cost('xxxx-xxxx-xxxx-xxxx;    YYYY-YYYY-YYYY-YYYY'),
                round((1+1.12)+((1+1.12)*sm.local_sales_tax),2)
                )

        # Test price greater than two decimal places
        self.assertEqual(
                sm.total_cost('zZzZ-zZzZ-zZzZ-zZzZ'),
                round(2.345+ (2.345*sm.local_sales_tax),2)
                )

        # Test price equals string integer
        self.assertEqual(
                sm.total_cost('aaaa-aaaa-aaaa-aaaa'),
                round(int(1)+(int(1)*sm.local_sales_tax),2)
                )

#Test product price
    def test__vproduct_price(self):
    
        sm = self._mock_supermarket_instance()
        # Test vaild price int
        self.assertIsNone(sm._vproduct_price(1))

       # Test vaild price float
        self.assertIsNone(sm._vproduct_price(1.1))

        # Test invalid price 0
        with self.assertRaises(ValueError):
            sm._vproduct_price(0)

        # Test invalid price < 0
        with self.assertRaises(ValueError):
            sm._vproduct_price(-1)

#The Code Pattern
    def test__vproduct_codes_pattern(self):
        sm = self._mock_supermarket_instance()
        # Test valid product code pattern lowercase
        self.assertIsNone(
                sm._vproduct_code_pattern('abcd-1234-abcd-1234')
                )

        # Test valid product code pattern uppercase
        self.assertIsNone(
                sm._vproduct_code_pattern('ABCD-1234-ABCD-1234')
                )

        # Test valid product code pattern mixcase
        self.assertIsNone(
                sm._vproduct_code_pattern('A123-b123-C123-d123')
                )


        # Test invalid lowercase 2 character group
        with self.assertRaises(ValueError):
            sm._vproduct_code_pattern('aaaa-bbbb-cccc-12')

       # Test invalid uppercase 2 character group
       with self.assertRaises(ValueError):
           sm._vproduct_code_pattern('AAAA-BBBB-CCCC-12')

        # Test invalid lowercase 3 character group
        with self.assertRaises(ValueError):
            sm._vproduct_code_pattern('aaaa-bbbb-cccc-123')

        # Test invalid uppercase 3 character group
        with self.assertRaises(ValueError):
            sm._vproduct_code_pattern('AAAA-BBBB-CCCC-123')

        # Test invalid lowercase 5 character group
        with self.assertRaises(ValueError):
            sm._vproduct_code_pattern('aaaa-bbbb-cccc-12345')

        # Test invalid uppercase 5 character group
        with self.assertRaises(ValueError):
            sm._vproduct_code_pattern('AAAA-BBBB-CCCC-12345')

        # Test invalid character
        with self.assertRaises(ValueError):
            sm._vproduct_code_pattern('AAA*-BBBB-CCCC-1234')

if __name__ == '__main__':
    unittest.main()
