import { useQuery } from '@tanstack/react-query'
import { getUserTrips } from '../api/client'

const USER_ID = 'user-demo-001'

const STATUS_COLORS = {
  completed: 'bg-green-700 text-green-200',
  cancelled: 'bg-red-700 text-red-200',
  active: 'bg-yellow-700 text-yellow-200',
  pending: 'bg-gray-700 text-gray-300',
}

export default function RideHistory() {
  const { data: trips = [], isLoading } = useQuery({ queryKey: ['trips'], queryFn: () => getUserTrips(USER_ID) })

  return (
    <div className="min-h-screen bg-gray-950 text-white p-6">
      <h1 className="text-3xl font-bold mb-6 text-indigo-400">🕘 Ride History</h1>
      {isLoading && <p className="text-gray-400">Loading...</p>}
      {!isLoading && trips.length === 0 && <p className="text-gray-500">No rides yet. Book your first ride!</p>}
      <div className="space-y-3">
        {trips.map(trip => (
          <div key={trip.id} className="bg-gray-900 rounded-xl p-4 flex items-center justify-between">
            <div>
              <p className="font-semibold">{trip.pickup} → {trip.destination}</p>
              <p className="text-gray-400 text-sm">{new Date(trip.created_at).toLocaleString()}</p>
              <p className="text-gray-500 text-xs mt-1">Priority: {trip.priority} | Vehicle: {trip.vehicle_preference || 'Any'}</p>
            </div>
            <span className={`text-xs font-bold px-3 py-1 rounded-full ${STATUS_COLORS[trip.status] || STATUS_COLORS.pending}`}>
              {trip.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}
