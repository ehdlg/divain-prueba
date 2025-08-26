import { type Product } from '../types';
import { useCallback, useState } from 'react';
import { apiUrl as API_URL } from '../constants';

function StockButton({
  onClick,
  ariaLabel,
  children,
}: {
  onClick: () => void;
  ariaLabel: string;
  children: React.ReactNode;
}) {
  return (
    <button
      onClick={onClick}
      className='w-12 h-12 rounded-full bg-slate-600 text-3xl hover:cursor-pointer font-bold flex items-center justify-center hover:bg-slate-500 transition'
      aria-label={ariaLabel}
      type='button'
    >
      {children}
    </button>
  );
}

export default function Product({ product }: { product: Product }) {
  const [stock, setStock] = useState(product.stock);
  const [originalStock, setOriginalStock] = useState(product.stock);

  const stockChanged = stock !== originalStock;

  const updateStock = useCallback(async () => {
    const response = await fetch(`${API_URL}/products/${product.id}`, {
      method: 'PATCH',
      body: JSON.stringify({ stock }),
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (response.ok) {
      setOriginalStock(stock); // Update local "original" stock after success
    }
  }, [stock, product.id]);

  const increaseStock = () => setStock((prev) => prev + 1);
  const decreaseStock = () => setStock((prev) => (prev > 0 ? prev - 1 : 0));

  return (
    <div className='bg-slate-700 rounded-xl shadow-md hover:shadow-sm transition-shadow p-6 w-full max-w-3xl mx-auto'>
      <div className='space-y-2 flex flex-col gap-4'>
        <div className='text-3xl font-semibold text-white'>{product.sku}</div>

        <div>
          <h3 className='text-lg text-slate-400'>EAN13</h3>
          <div className='text-lg font-semibold text-white'>{product.ean13}</div>
        </div>

        <div>
          <h3 className='text-lg text-slate-400'>Stock</h3>
          <div className='flex flex-col gap-2'>
            <div className='flex items-center justify-center gap-3'>
              <StockButton onClick={decreaseStock} ariaLabel='Decrease stock'>
                −
              </StockButton>
              <input
                type='number'
                value={stock}
                onChange={(e) => {
                  const newStock = Number(e.currentTarget.value);
                  if (isNaN(newStock)) return;
                  setStock(newStock);
                }}
                className='w-16 text-center bg-transparent border-none text-lg font-medium text-white outline-none appearance-none [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none'
              />
              <StockButton onClick={increaseStock} ariaLabel='Increase stock'>
                +
              </StockButton>
            </div>
            {stockChanged && (
              <button
                onClick={updateStock}
                className='mx-auto hover:shadow-none hover:translate-y-0.5 px-4 py-2 bg-blue-500 cursor-pointer hover:bg-blue-600 transition ease-in duration-200 shadow-xl rounded mt-8'
              >
                Actualizar stock
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
