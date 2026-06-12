export default function LogsPanel({ logs = [] }) {
  return (
    <div className="bg-gray-900 rounded-xl p-4">
      <h2 className="text-white font-bold text-lg mb-3">📋 Execution Logs</h2>
      <div className="h-64 overflow-y-auto space-y-1 font-mono text-xs">
        {logs.length === 0
          ? <p className="text-gray-500">No logs yet. Request a ride to see agent activity.</p>
          : logs.map((log, i) => {
            const color =
              log.includes('SearchAgent') ? 'text-blue-400' :
              log.includes('ComparisonAgent') ? 'text-purple-400' :
              log.includes('BookingAgent') ? 'text-green-400' :
              log.includes('MonitoringAgent') ? 'text-yellow-400' :
              log.includes('RecoveryAgent') ? 'text-red-400' :
              log.includes('AnalyticsAgent') ? 'text-cyan-400' :
              log.includes('MemoryAgent') ? 'text-pink-400' :
              'text-gray-300'
            return <p key={i} className={color}>{log}</p>
          })
        }
      </div>
    </div>
  )
}
