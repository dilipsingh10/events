import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

type Event = {
  id: number
  title: string
  description?: string
  start_datetime?: string
  end_datetime?: string
}

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export default function EventDetailPage() {
  const { id } = useParams()
  const [event, setEvent] = useState<Event | null>(null)

  useEffect(() => {
    if (!id) return
    axios.get(`${API_BASE}/api/events/${id}`).then(res => setEvent(res.data))
  }, [id])

  if (!event) return <p>Loading...</p>

  return (
    <div className="space-y-2">
      <h1 className="text-2xl font-bold">{event.title}</h1>
      {event.description && <p>{event.description}</p>}
      <div className="text-sm text-gray-600">Event ID: {event.id}</div>
    </div>
  )
}

