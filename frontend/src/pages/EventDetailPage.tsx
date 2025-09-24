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
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [ticketTypeId, setTicketTypeId] = useState<number | null>(null)
  const [ticketTypes, setTicketTypes] = useState<{ id: number; name: string; price: number }[]>([])
  const [message, setMessage] = useState<string>('')

  useEffect(() => {
    if (!id) return
    axios.get(`${API_BASE}/api/events/${id}`).then(res => setEvent(res.data))
    axios.get(`${API_BASE}/api/tickets/types`, { params: { event_id: id } }).then(res => setTicketTypes(res.data))
  }, [id])

  if (!event) return <p>Loading...</p>

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">{event.title}</h1>
      {event.description && <p>{event.description}</p>}
      <div className="text-sm text-gray-600">Event ID: {event.id}</div>
      <section className="border rounded p-4 bg-white">
        <h2 className="font-semibold mb-2">Register</h2>
        <div className="grid md:grid-cols-2 gap-3">
          <input className="border rounded p-2" placeholder="Full name" value={name} onChange={e => setName(e.target.value)} />
          <input className="border rounded p-2" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
          <select className="border rounded p-2 md:col-span-2" value={ticketTypeId ?? ''} onChange={e => setTicketTypeId(Number(e.target.value))}>
            <option value="">Select ticket type</option>
            {ticketTypes.map(tt => (
              <option key={tt.id} value={tt.id}>{tt.name} — ${tt.price}</option>
            ))}
          </select>
          <button
            className="bg-blue-600 text-white rounded px-4 py-2 w-fit"
            onClick={async () => {
              try {
                if (!id || !ticketTypeId) return
                const res = await axios.post(`${API_BASE}/api/registration/simple`, null, {
                  params: { event_id: id, ticket_type_id: ticketTypeId, name, email }
                })
                setMessage(`Registered: ${res.data.name} (${res.data.email})`)
              } catch (e: any) {
                setMessage(e?.response?.data?.detail || 'Registration failed')
              }
            }}
          >
            Register
          </button>
          {message && <div className="text-sm text-green-700 md:col-span-2">{message}</div>}
        </div>
      </section>
    </div>
  )
}

