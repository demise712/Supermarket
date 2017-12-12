# ​Supermarket​ ​Register​ ​-​ ​CLI​ ​Application
​The​ ​Supermaket Register CLI application features includes:

- Lists each​ ​product that are registered,
- Add/register a product
- Remove a product that is registered
- Calculate ​the​ ​total​ ​amount​ ​of​ ​sale of selected products (including local​ ​sales​ ​tax​)​ ​
- Save the changes, if new product is registered or removed

# To Tests and Build the application

# Makefile
make build

# Docker
docker build -t Supermarket .

# Running (To calculate the total products)
Set environment variable 'SKUS' to a string of products codes separated by semicolons, which will calculate total amount of sale.

For example
export SKUS="A12T-4GH7-QPL9-3N4M;E5T6-9UI3-TH15-QR88"

#To run the Application

# Makefile
make run

# Docker
docker run -e SKUS="${SKUS}" -it Supermarket
