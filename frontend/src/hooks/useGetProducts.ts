import { useState, useEffect, useCallback } from 'react';
import type { Product } from '@/types';
import { apiUrl as API_URL } from '../constants';

export default function useGetProducts() {
  const [products, setProducts] = useState<Product[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const getProducts = useCallback(async () => {
    try {
      const response = await fetch(`${API_URL}/products`);

      if (response.status !== 200) {
        throw new Error(response.statusText);
      }

      const data = (await response.json()) as Product[];

      setProducts(data);
    } catch (error) {
      if (error instanceof Error) {
        setError(error.message);

        return;
      }

      setError('Could not get the products.');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    getProducts();
  }, [getProducts]);

  return {
    products,
    error,
    isLoading,
  };
}
