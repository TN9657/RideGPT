import { NavLink } from 'react-router-dom'

const links = [
  { to: '/', label: 'Dashboard' },
  { to: '/book', label: 'Book Ride' },
  { to: '/history', label: 'History' },
  { to: '/analytics', label: 'Analytics' },
]

export default function Navbar() {
  return (
    <nav className="bg-gray-900 border-b border-gray-800 px-6 py-3 flex items-center justify-between">
      <span className="text-indigo-400 font-bold text-xl">🚕 RideGPT</span>
      <div className="flex gap-1">
        {links.map(l => (
          <NavLink
            key={l.to}
            to={l.to}
            end={l.to === '/'}
            className={({ isActive }) =>
              `px-4 py-2 rounded-lg text-sm font-medium transition ${isActive ? 'bg-indigo-700 text-white' : 'text-gray-400 hover:text-white hover:bg-gray-800'}`
            }
          >
            {l.label}
          </NavLink>
        ))}
      </div>
    </nav>
  )
}
