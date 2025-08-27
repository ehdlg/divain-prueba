import { useState, useEffect, useCallback } from 'react';
import type { StockMovement } from '@/types';
import { apiUrl as API_URL } from '../constants';

export default function useGetStockMovements() {
  const [stockMovements, setStockMovements] = useState<StockMovement[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const getStockMovements = useCallback(async () => {
    try {
      const response = await fetch(`${API_URL}/stock`);

      if (response.status !== 200) {
        throw new Error(response.statusText);
      }

      const data = (await response.json()) as StockMovement[];

      data.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());

      setStockMovements(data);
    } catch (error) {
      if (error instanceof Error) {
        setError(error.message);

        return;
      }

      setError('Could not get the stock movements.');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    getStockMovements();
  }, [getStockMovements]);

  return {
    stockMovements,
    error,
    isLoading,
  };
}
