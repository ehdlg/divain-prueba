import type { StockMovement } from '../types';

export default function StockMovementItem({ move }: { move: StockMovement }) {
  return (
    <li className='bg-slate-700 border border-slate-600 rounded-lg p-4 shadow hover:shadow-md transition-shadow flex flex-col gap-2'>
      <div className='flex justify-between items-center text-white text-lg font-medium'>
        <div className='flex flex-col gap-2'>
          <span>{move.sku}</span>
          <span className='text-slate-400 text-sm'>EAN13: {move.ean13}</span>
        </div>

        <div
          className={`text-xl font-bold ${move.quantity > 0 ? 'text-green-400' : 'text-red-400'}`}
        >
          {move.quantity > 0 ? `+${move.quantity}` : move.quantity}
        </div>
      </div>

      <div className='text-slate-400  text-sm'>
        Stock después del movimiento: <span className='text-white font-medium'>{move.stock}</span>
      </div>

      <div className='text-slate-200 text-xs mt-1'>
        {new Date(move.timestamp).toLocaleString('es-ES', {
          dateStyle: 'short',
          timeStyle: 'short',
        })}
      </div>
    </li>
  );
}
