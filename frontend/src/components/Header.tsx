import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <nav className='p-4 bg-slate-800 flex gap-4 text-xl hover:text-white border-b border-slate-700 shadow'>
      <Link to='/'>Home</Link>
      <Link to='/stock'>Movimiento de stock</Link>
    </nav>
  );
}
