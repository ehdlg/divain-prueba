import useGetStockMovements from '../hooks/useGetStockMovements';
import Loading from '../components/Loading';
import StockMovementList from '../components/StockMovementList';

export default function Stock() {
  const { stockMovements, error, isLoading } = useGetStockMovements();

  if (isLoading) return <Loading />;
  if (error) return <div className='text-red-400 text-center mt-4'>{error}</div>;

  return (
    <div className='bg-slate-800 min-h-screen p-6'>
      <h1 className='text-3xl font-semibold text-white mb-6'>Registro de Movimientos</h1>
      <StockMovementList stockMovements={stockMovements} />
    </div>
  );
}
