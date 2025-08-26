from app.repositories.product import ProductRepository


class ProductService:
    def __init__(self, product_reposistory: ProductRepository):
        self.repository = product_reposistory

    def get_all(self):
        return self.repository.get_all()
