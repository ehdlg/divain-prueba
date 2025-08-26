export type Product = {
  id: string;
  sku: string;
  ean13: string;
  stock: number;
  name: string;
};

export type StockMovement = Omit<Product, 'name'> & {
  product_id: string;
  user_id: string | null;
  quantity: number;
  timestamp: string;
};
