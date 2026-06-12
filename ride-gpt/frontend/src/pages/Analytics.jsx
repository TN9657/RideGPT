import { useQuery } from '@tanstack/react-query'
import { getAnalytics } from '../api/client'
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer,
  PieChart, Pie, Cell, Legend,
} from 'recharts'

const USER_ID = 'user-demo-001'
const COLORS = ['#6366f1', '#22d3ee', '#f59e0b', '#10b981', '#f43f5e']

export default function AnalyticsPage() {
  const { data, isLoading } = useQuery({ queryKey: ['analytics'], queryFn: () => getAnalytics(USER_ID) })

  if (isLoading) return <div className="text-white p-8">Loading analytics...</div>
  if (!data || data.total_trips === 0) return <div className="text-white p-8">No analytics data yet. Book a ride to get started!</div>

  const pieData = data.providers_breakdown
    ? Object.entries(data.providers_breakdown).map(([name, value]) => ({ name, value }))
    : []

  const barData = pieData.map(p => ({ ...p }))

  const statsCards = [
    { label: 'Total Trips', value: data.total_trips },
    { label: 'Cancellations', value: data.total_cancellations },
    { label: 'Avg Fare', value: data.avg_fare ? `₹${data.avg_fare}` : 'N/A' },
    { label: 'Avg ETA', value: data.avg_eta ? `${data.avg_eta} min` : 'N/A' },
    { label: 'Most Used', value: data.most_used_provider || 'N/A' },
    { label: 'Completion Rate', value: data.trip_completion_rate ? `${data.trip_completion_rate}%` : 'N/A' },
  ]

  return (
    <div className="min-h-screen bg-gray-950 text-white p-6">
      <h1 className="text-3xl font-bold mb-6 text-indigo-400">📊 Analytics</h1>

      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 mb-8">
        {statsCards.map(s => (
          <div key={s.label} className="bg-gray-900 rounded-xl p-4 text-center">
            <p className="text-gray-400 text-xs">{s.label}</p>
            <p className="text-2xl font-bold text-indigo-400 mt-1">{s.value}</p>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {pieData.length > 0 && (
          <div className="bg-gray-900 rounded-xl p-6">
            <h2 className="text-white font-bold mb-4">Provider Usage Share</h2>
            <ResponsiveContainer width="100%" height={260}>
              <PieChart>
                <Pie data={pieData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={90} label>
                  {pieData.map((_, i) => <Cell key={i} fill={COLORS[i % COLORS.length]} />)}
                </Pie>
                <Legend />
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        )}

        {barData.length > 0 && (
          <div className="bg-gray-900 rounded-xl p-6">
            <h2 className="text-white font-bold mb-4">Trips per Provider</h2>
            <ResponsiveContainer width="100%" height={260}>
              <BarChart data={barData} margin={{ top: 5, right: 20, left: 0, bottom: 5 }}>
                <XAxis dataKey="name" tick={{ fill: '#9ca3af' }} />
                <YAxis tick={{ fill: '#9ca3af' }} allowDecimals={false} />
                <Tooltip contentStyle={{ backgroundColor: '#1f2937', border: 'none' }} />
                <Bar dataKey="value" radius={[4, 4, 0, 0]}>
                  {barData.map((_, i) => <Cell key={i} fill={COLORS[i % COLORS.length]} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>
    </div>
  )
}
