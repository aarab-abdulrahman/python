import json

def create_product(product_id, price, name, quantity, category):
    return {
        "ID": product_id,
        "Price": price,
        "Name": name,
        "Quantity": quantity,
        "Category": category
    }

def add_product(products, product):
    products.append(product)

def get_most_expensive_product(products):
    if not products:
        return None
    return max(products, key=lambda x: x['Price'])

def get_products_by_category(products, category):
    return [product for product in products if product['Category'] == category]

def list_low_stock_products(products, threshold=20):
    return [product for product in products if product['Quantity'] < threshold]

def get_unique_categories(products):
    return list(set(product['Category'] for product in products))

def save_to_file(products, filename):
    with open(filename, 'w') as file:
        json.dump(products, file)

def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def find_product_by_name(products, name):
    return [product for product in products if product['Name'].lower() == name.lower()]


if __name__ == "__main__":
    products = []


    add_product(products, create_product(1, 299.99, "Télévision", 15, "Électronique"))
    add_product(products, create_product(2, 49.99, "Céréales", 30, "Alimentation"))
    add_product(products, create_product(3, 19.99, "Savon", 10, "Hygiène"))
    add_product(products, create_product(4, 199.99, "Ordinateur portable", 5, "Électronique"))
    add_product(products, create_product(5, 9.99, "Biscottes", 25, "Alimentation"))


    expensive_product = get_most_expensive_product(products)
    print("Produit le plus cher:", expensive_product)


    electronics = get_products_by_category(products, "Électronique")
    print("Produits en Électronique:", electronics)


    low_stock_products = list_low_stock_products(products)
    print("Produits en stock faible:", low_stock_products)


    unique_categories = get_unique_categories(products)
    print("Catégories distinctes:", unique_categories)


    save_to_file(products, 'products.json')
    print("Produits sauvegardés dans 'products.json'.")


    loaded_products = load_from_file('products.json')
    print("Produits chargés depuis 'products.json':", loaded_products)


    product_name = input("Entrez le nom du produit que vous souhaitez rechercher: ")
    found_products = find_product_by_name(products, product_name)

    if found_products:
        for product in found_products:
            print("Informations sur le produit trouvé:", product)
    else:
        print("Aucun produit trouvé avec ce nom.")
