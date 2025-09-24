import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

type Event = {
  id: number
  title: string
  description?: string
  start_datetime?: string
  end_datetime?: string
}

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export default function EventsPage() {
  const [events, setEvents] = useState<Event[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    axios.get(`${API_BASE}/api/events/`).then(res => setEvents(res.data)).finally(() => setLoading(false))
  }, [])

  return (
    <div>
      <h1 className="text-2xl font-semibold mb-4">Events</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="grid md:grid-cols-2 gap-4">
          {events.map(e => (
            <Link key={e.id} to={`/events/${e.id}`} className="block border rounded-lg p-4 bg-white hover:shadow">
              <h2 className="text-lg font-semibold">{e.title}</h2>
              {e.description && <p className="text-sm text-gray-600 line-clamp-2">{e.description}</p>}
            </Link>
          ))}
        </div>
      )}
    </div>
  )
}

