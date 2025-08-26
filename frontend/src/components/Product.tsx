import { type Product } from '../types';
import { useState } from 'react';

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

  const increaseStock = () => setStock((prev) => prev + 1);
  const decreaseStock = () => setStock((prev) => (prev > 0 ? prev - 1 : 0));

  return (
    <div className='bg-slate-700 rounded-xl shadow-md hover:shadow-sm transition-shadow p-6 w-full max-w-3xl mx-auto'>
      <div className='space-y-2'>
        <div className='text-3xl font-semibold text-white'>{product.sku}</div>

        <div className='text-sm text-slate-400'>EAN13</div>
        <div className='text-lg font-semibold text-white'>{product.ean13}</div>

        <div className='text-sm text-slate-400'>Stock</div>
        <div className='flex items-center justify-center gap-3'>
          <StockButton onClick={decreaseStock} ariaLabel='Decrease stock'>
            −
          </StockButton>
          <input
            type='number'
            value={stock}
            readOnly
            className='w-16 text-center bg-transparent border-none text-lg font-medium text-white outline-none appearance-none [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none'
          />
          <StockButton onClick={increaseStock} ariaLabel='Increase stock'>
            +
          </StockButton>
        </div>
      </div>
    </div>
  );
}
