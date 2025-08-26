import type { StockMovement } from '../types';
import StockMovementItem from './StockMovementItem';

export default function StockMovementList({ stockMovements }: { stockMovements: StockMovement[] }) {
  if (stockMovements.length === 0) {
    return <div className='text-slate-400 text-center'>No hay movimientos registrados.</div>;
  }

  return (
    <ul className='space-y-4'>
      {stockMovements.map((move) => (
        <StockMovementItem key={move.id} move={move} />
      ))}
    </ul>
  );
}
