#!/usr/bin/env python

import register_supermarket
import json
import os

def print_menu():
    print('1) List products')
    print('2) Add a product')
    print('3) Remove a product')
    print('4) Calculate total cost of products')
    print('5) Save and exit')

if __name__ == '__main__':
    # Read config and create Supermarket Register
    product_file = open('product.json', 'r').read()
    product_data = json.loads(product_file)
    register = register_supermarket.SupermarketRegister(product_data)

    while True:
        print_menu()
        print('Select option:')
        option = int(raw_input())

        try:
            if(option == 1):
                register.list_products()
            elif(option == 2):
                print('Enter product code:')
                code = str(raw_input())
                print('Enter product name:')
                name = str(raw_input())
                print('Enter product price:')
                price = str(raw_input())
                product = { code: { 'product': name, 'price': price } }
                register.add_product(product)
            elif(option == 3):
                print('Enter product code:')
                code = str(raw_input())
                register.remove_product(code)
            elif(option == 4):
                print('Enter product codes separated by semicolons:')
                os.environ['SKUS'] = str(raw_input())
                print('$', register.total_cost(os.environ['SKUS']))
            elif(option == 5):
                with open('product.json', 'w') as config:
                    json.dump(register.p_codes, config)
                break
            else:
                print('Invalid option')
        except KeyError:
            print('Invalid input')
        except ValueError:
            print('Invalid input')
        print()
