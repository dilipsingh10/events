import { Route, Routes, Link, Navigate } from 'react-router-dom'
import EventsPage from './pages/EventsPage'
import EventDetailPage from './pages/EventDetailPage'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <header className="border-b bg-white">
        <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
          <Link to="/" className="font-semibold text-lg">Event Manager</Link>
          <nav className="space-x-4">
            <Link to="/" className="hover:underline">Events</Link>
          </nav>
        </div>
      </header>
      <main className="max-w-6xl mx-auto px-4 py-6">
        <Routes>
          <Route path="/" element={<EventsPage />} />
          <Route path="/events/:id" element={<EventDetailPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </main>
    </div>
  )
}

