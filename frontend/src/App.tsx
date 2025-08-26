import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Header from './components/Header';
import Stock from './pages/Stock';

function App() {
  return (
    <>
      <Header />
      <main className='max-w-[1000px] mx-auto p-2 mt-8'>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/stock' element={<Stock />} />
        </Routes>
      </main>
    </>
  );
}

export default App;
