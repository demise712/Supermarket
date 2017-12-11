#!/usr/bin/env python

import re

class SupermarketRegister:
    def __init__(self, p_codes, local_sales_tax=0.0875):
        for code, info in p_codes.items():
            p_codes[code.upper()] = p_codes.pop(code)
            self._vproduct_code_pattern(code)
            self._vproduct_price(info['price'])
        self.p_codes = p_codes
        self.local_sales_tax = local_sales_tax

#List the products
    def list_products(self):
        if not self.p_codes:
            print('No Product Codes is listed')
        else:
            for code, info in self.p_codes.items():
                print(code, info)
#Add a product
    def add_product(self, product):
        for code, info in product.items():
            self._vproduct_code_pattern(code)
            self._vproduct_price(product[code]['price'])
            if not code in self.p_codes:
                self.p_codes[code.upper()] = info
            else:
                raise KeyError('Product already exists: {0}'.format(code))

#Remove a products
    def remove_product(self, code):
            code = code.upper()
            self._vproduct_code_pattern(code)
            if code in self.p_codes:
                self.p_codes.pop(code, None)
            else:
                raise KeyError('Product does not exists: {0}'.format(code))

#Total Cost
    def total_cost(self, products):
        codes = ''.join(products.split()).split(';')
        total_cost = 0
        for code in codes:
            code = code.upper()
            try:
                self._vproduct_code_pattern(code)
                self._vproduct_price(self.p_codes[code]['price'])
                total_cost += float(self.p_codes[code]['price'])
            except KeyError as e:
                print('Invalid product code: {0}'.format(code))
                print('Valid product codes are:')
                self.list_products()
                raise
        return round(total_cost + (total_cost * self.local_sales_tax), 2)

    def _vproduct_price(self, price):
        if float(price) <= 0:
            raise ValueError('Invalid product price: {0}'.format(price))

    def _vproduct_code_pattern(self, code):
        pattern = re.compile(
                '^[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}$'
                )
        if not pattern.match(code):
            raise ValueError('Invalid product code pattern: {0}'.format(code))
