export default function ActiveTripPanel({ trip }) {
  if (!trip) return null
  const { selected_ride, booking_status, ride_status, trip_id, pickup, destination, recovery_attempts, cancellation_history } = trip

  const statusColor = {
    active: 'bg-green-500',
    completed: 'bg-blue-500',
    cancelled: 'bg-red-500',
    pending: 'bg-yellow-500',
  }

  return (
    <div className="bg-gray-900 rounded-xl p-4 space-y-3">
      <h2 className="text-white font-bold text-lg">🚗 Active Trip</h2>
      <div className="grid grid-cols-2 gap-2 text-sm">
        <Info label="Trip ID" value={trip_id?.slice(0, 8) + '...'} />
        <Info label="Route" value={`${pickup} → ${destination}`} />
        <Info label="Booking" value={booking_status} badge={booking_status === 'confirmed' ? 'green' : 'red'} />
        <Info label="Ride Status" value={ride_status} badge={statusColor[ride_status] || 'gray'} />
        {selected_ride && <>
          <Info label="Provider" value={selected_ride.provider} />
          <Info label="Price" value={`₹${selected_ride.price}`} />
          <Info label="ETA" value={`${selected_ride.eta} min`} />
          <Info label="Vehicle" value={selected_ride.vehicle} />
          <Info label="Driver" value={selected_ride.driver_name || 'N/A'} />
          <Info label="Rating" value={`⭐ ${selected_ride.rating}`} />
        </>}
        {recovery_attempts > 0 && <Info label="Recovery Attempts" value={recovery_attempts} />}
        {cancellation_history?.length > 0 && <Info label="Cancellations" value={cancellation_history.length} />}
      </div>
    </div>
  )
}

function Info({ label, value }) {
  return (
    <div className="bg-gray-800 rounded-lg p-2">
      <p className="text-gray-400 text-xs">{label}</p>
      <p className="text-white text-sm font-medium">{value ?? '—'}</p>
    </div>
  )
}
