
class ProductService:

    def __init__(self):

        self.products = [
            {
                "id": 1,
                "sku": "PROD-1001",
                "name": "Laptop",
                "category": "electronics",
                "price": 1200000,
                "stock": 10
            },
            {
                "id": 2,
                "sku": "PROD-1002",
                "name": "Phone",
                "category": "electronics",
                "price": 750000,
                "stock": 15
            },
            {
                "id": 3,
                "sku": "PROD-1003",
                "name": "Chair",
                "category": "furniture",
                "price": 150000,
                "stock": 20
            }
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id: int):

        for product in self.products:

            if product["id"] == product_id:
                return product

        return None

    def create_product(self, product_data):

        # Prevent duplicate SKUs
        for product in self.products:

            if product["sku"] == product_data.sku:
                raise ValueError("Product SKU already exists")

        new_product = {
            "id": max(
                product["id"] for product in self.products
            ) + 1,
            "sku": product_data.sku,
            "name": product_data.name,
            "category": product_data.category,
            "price": product_data.price,
            "stock": product_data.stock
        }

        self.products.append(new_product)

        return new_product
