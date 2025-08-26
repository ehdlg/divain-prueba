import useGetProducts from '../hooks/useGetProducts';
import Product from '../components/Product';
import Loading from '../components/Loading';

function Home() {
  const { products, isLoading, error } = useGetProducts();

  if (isLoading) return <Loading />;

  if (error) return <h1>Error: {error}</h1>;
  return (
    <main className='max-w-[1000px] mx-auto p-2 mt-8'>
      <h1 className='text-3xl text-center m-4'>Inventario almacen</h1>
      <div className='grid gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-1'>
        {products.map((product) => (
          <Product key={product.id} product={product} />
        ))}
      </div>
    </main>
  );
}

export default Home;
