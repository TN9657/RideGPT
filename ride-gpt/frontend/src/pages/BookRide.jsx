import { useState } from 'react'
import { useMutation } from '@tanstack/react-query'
import { requestRide } from '../api/client'
import AgentStatusPanel from '../components/AgentStatusPanel'
import ActiveTripPanel from '../components/ActiveTripPanel'
import LogsPanel from '../components/LogsPanel'

const USER_ID = 'user-demo-001'

export default function BookRide() {
  const [form, setForm] = useState({ pickup: '', destination: '', vehicle_preference: '', budget: '', priority: 'balanced' })
  const { mutate, data, isPending, isError, error } = useMutation({ mutationFn: requestRide })

  const handleSubmit = (e) => {
    e.preventDefault()
    mutate({ ...form, user_id: USER_ID, budget: form.budget ? Number(form.budget) : null })
  }

  return (
    <div className="min-h-screen bg-gray-950 text-white p-6">
      <h1 className="text-3xl font-bold mb-6 text-indigo-400">🚕 Book a Ride</h1>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="space-y-4">
          <form onSubmit={handleSubmit} className="bg-gray-900 rounded-xl p-6 space-y-4">
            {[
              { label: 'Pickup Location', key: 'pickup', placeholder: 'e.g. Connaught Place, Delhi' },
              { label: 'Destination', key: 'destination', placeholder: 'e.g. IGI Airport' },
            ].map(f => (
              <div key={f.key}>
                <label className="text-gray-400 text-sm">{f.label}</label>
                <input
                  required
                  className="w-full mt-1 bg-gray-800 rounded-lg px-4 py-2 text-white outline-none focus:ring-2 focus:ring-indigo-500"
                  placeholder={f.placeholder}
                  value={form[f.key]}
                  onChange={e => setForm(p => ({ ...p, [f.key]: e.target.value }))}
                />
              </div>
            ))}

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="text-gray-400 text-sm">Vehicle Type</label>
                <select
                  className="w-full mt-1 bg-gray-800 rounded-lg px-3 py-2 text-white"
                  value={form.vehicle_preference}
                  onChange={e => setForm(p => ({ ...p, vehicle_preference: e.target.value }))}
                >
                  <option value="">Any</option>
                  {['Sedan', 'SUV', 'Auto', 'Bike', 'Hatchback'].map(v => <option key={v}>{v}</option>)}
                </select>
              </div>
              <div>
                <label className="text-gray-400 text-sm">Budget (₹)</label>
                <input
                  type="number"
                  className="w-full mt-1 bg-gray-800 rounded-lg px-3 py-2 text-white"
                  placeholder="Optional"
                  value={form.budget}
                  onChange={e => setForm(p => ({ ...p, budget: e.target.value }))}
                />
              </div>
            </div>

            <div>
              <label className="text-gray-400 text-sm">Priority</label>
              <select
                className="w-full mt-1 bg-gray-800 rounded-lg px-3 py-2 text-white"
                value={form.priority}
                onChange={e => setForm(p => ({ ...p, priority: e.target.value }))}
              >
                {['balanced', 'cost', 'speed', 'reliability'].map(p => (
                  <option key={p} value={p}>{p.charAt(0).toUpperCase() + p.slice(1)}</option>
                ))}
              </select>
            </div>

            <button
              type="submit"
              disabled={isPending}
              className="w-full bg-indigo-600 hover:bg-indigo-500 disabled:bg-indigo-900 text-white font-bold py-3 rounded-xl transition"
            >
              {isPending ? '🤖 Agents Working...' : '🔍 Find Ride'}
            </button>

            {isError && <p className="text-red-400 text-sm">Error: {error.message}</p>}
          </form>

          {data && <ActiveTripPanel trip={data} />}

          {data?.agent_outputs?.comparison?.reasoning && (
            <div className="bg-gray-900 rounded-xl p-4">
              <h2 className="text-white font-bold mb-2">🤖 AI Decision</h2>
              <p className="text-indigo-300 text-sm">{data.agent_outputs.comparison.reasoning}</p>
              {data.agent_outputs.comparison.alternatives?.length > 0 && (
                <div className="mt-3 space-y-1">
                  <p className="text-gray-400 text-xs font-semibold uppercase tracking-wide">Alternatives considered</p>
                  {data.agent_outputs.comparison.alternatives.map((alt, i) => (
                    <div key={i} className="flex justify-between text-xs text-gray-400 bg-gray-800 rounded px-3 py-1">
                      <span>{alt.provider}</span>
                      <span>₹{alt.price} · {alt.eta}min · ⭐{alt.rating}</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {data?.notifications?.length > 0 && (
            <div className="bg-gray-900 rounded-xl p-4 space-y-2">
              <h2 className="text-white font-bold">🔔 Notifications</h2>
              {data.notifications.map((n, i) => (
                <div key={i} className="bg-indigo-900/40 border border-indigo-700 rounded-lg px-4 py-2 text-sm text-indigo-200">
                  <span className="font-bold mr-2">[{n.type}]</span>{n.message}
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="space-y-4">
          <AgentStatusPanel logs={data?.logs || []} timestamps={data?.timestamps || {}} />
          <LogsPanel logs={data?.logs || []} />
        </div>
      </div>
    </div>
  )
}
