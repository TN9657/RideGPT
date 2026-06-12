const AGENTS = ['SearchAgent', 'ComparisonAgent', 'BookingAgent', 'MonitoringAgent', 'RecoveryAgent', 'MemoryAgent', 'NotificationAgent', 'AnalyticsAgent']

function getAgentStatus(logs, agent) {
  const key = agent.toLowerCase().replace('agent', '')
  const running = logs.some(l => l.toLowerCase().includes(key))
  const done = logs.some(l => l.toLowerCase().includes(key) && (l.includes('completed') || l.includes('confirmed') || l.includes('recorded') || l.includes('Updated') || l.includes('Sent') || l.includes('Selected') || l.includes('Found') || l.includes('Monitoring') || l.includes('Recovery')))
  if (done) return 'done'
  if (running) return 'running'
  return 'idle'
}

export default function AgentStatusPanel({ logs = [], timestamps = {} }) {
  return (
    <div className="bg-gray-900 rounded-xl p-4 space-y-2">
      <h2 className="text-white font-bold text-lg mb-3">⚡ Agent Execution</h2>
      {AGENTS.map(agent => {
        const status = getAgentStatus(logs, agent)
        return (
          <div key={agent} className="flex items-center justify-between bg-gray-800 rounded-lg px-4 py-2">
            <span className="text-gray-300 text-sm font-medium">{agent}</span>
            <span className={`text-xs font-semibold px-2 py-1 rounded-full ${
              status === 'done' ? 'bg-green-600 text-white' :
              status === 'running' ? 'bg-yellow-500 text-black animate-pulse' :
              'bg-gray-600 text-gray-400'
            }`}>
              {status === 'done' ? '✓ Done' : status === 'running' ? '⟳ Running' : '○ Idle'}
            </span>
          </div>
        )
      })}
    </div>
  )
}
