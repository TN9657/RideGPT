import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import Navbar from './components/Navbar'
import Dashboard from './pages/Dashboard'
import BookRide from './pages/BookRide'
import RideHistory from './pages/RideHistory'
import Analytics from './pages/Analytics'

const queryClient = new QueryClient()

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <div className="min-h-screen bg-gray-950">
          <Navbar />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/book" element={<BookRide />} />
            <Route path="/history" element={<RideHistory />} />
            <Route path="/analytics" element={<Analytics />} />
          </Routes>
        </div>
      </BrowserRouter>
    </QueryClientProvider>
  )
}
