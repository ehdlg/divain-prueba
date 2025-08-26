import useGetProducts from '../hooks/useGetProducts';
import Product from '../components/Product';
import Loading from '../components/Loading';

export default function Home() {
  const { products, isLoading, error } = useGetProducts();

  if (isLoading) return <Loading />;

  if (error) return <div className='text-red-400 text-center mt-4'>{error}</div>;
  return (
    <>
      <h1 className='text-3xl font-semibold text-white mb-6'>Inventario almacen</h1>
      <div className='grid gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-1'>
        {products.map((product) => (
          <Product key={product.id} product={product} />
        ))}
      </div>
    </>
  );
}
