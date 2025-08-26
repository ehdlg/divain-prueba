import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Header from './components/Header';

function App() {
  return (
    <div>
      <Header />

      <Routes>
        <Route path='/' element={<Home />} />
        {/* <Route path='/stock' element={<Home />} /> */}
      </Routes>
    </div>
  );
}

export default App;
