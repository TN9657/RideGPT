import { Link } from 'react-router-dom'

const cards = [
  { to: '/book', icon: '🚕', title: 'Book a Ride', desc: 'Let AI agents find and book the best ride for you' },
  { to: '/history', icon: '🕘', title: 'Ride History', desc: 'View all your past trips' },
  { to: '/analytics', icon: '📊', title: 'Analytics', desc: 'Insights on your ride patterns and spending' },
]

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-950 text-white p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-indigo-400 mb-2">RideGPT 🤖</h1>
        <p className="text-gray-400 mb-10">Autonomous AI-powered ride booking platform</p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
          {cards.map(c => (
            <Link key={c.to} to={c.to} className="bg-gray-900 hover:bg-gray-800 rounded-2xl p-6 transition group">
              <div className="text-4xl mb-3">{c.icon}</div>
              <h2 className="text-lg font-bold group-hover:text-indigo-400 transition">{c.title}</h2>
              <p className="text-gray-500 text-sm mt-1">{c.desc}</p>
            </Link>
          ))}
        </div>

        <div className="bg-gray-900 rounded-2xl p-6">
          <h2 className="text-white font-bold text-lg mb-4">🤖 Agent Architecture</h2>
          <div className="flex flex-wrap gap-2">
            {['SearchAgent', 'ComparisonAgent', 'BookingAgent', 'MonitoringAgent', 'RecoveryAgent', 'MemoryAgent', 'NotificationAgent', 'AnalyticsAgent'].map(a => (
              <span key={a} className="bg-indigo-900/50 text-indigo-300 border border-indigo-700 text-xs px-3 py-1 rounded-full">{a}</span>
            ))}
          </div>
          <div className="mt-4 text-gray-500 text-sm space-y-1">
            <p>✦ Powered by LangGraph multi-agent workflow</p>
            <p>✦ Groq (Llama 3) + Google Gemini fallback</p>
            <p>✦ Auto-recovery on cancellation</p>
            <p>✦ Uber · Ola · Rapido simulators</p>
          </div>
        </div>
      </div>
    </div>
  )
}
