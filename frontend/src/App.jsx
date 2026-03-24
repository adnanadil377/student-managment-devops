import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [student, setStudent] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const fetchStudent = async () => {
      try {
        const response = await fetch('/api/student')

        if (!response.ok) {
          throw new Error('Failed to load student details from backend.')
        }

        const data = await response.json()
        setStudent(data)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Something went wrong.')
      } finally {
        setLoading(false)
      }
    }

    fetchStudent()
  }, [])

  return (
    <main className="landing">
      <section className="card" aria-live="polite">
        <p className="label">Student Management</p>
        <h1>Student Profile</h1>

        {loading && <p className="status">Loading student details...</p>}

        {!loading && error && <p className="status error">{error}</p>}

        {!loading && !error && student && (
          <dl className="details">
            <div>
              <dt>Student Name</dt>
              <dd>{student.student_name}</dd>
            </div>
            <div>
              <dt>Roll Number</dt>
              <dd>{student.roll_number}</dd>
            </div>
          </dl>
        )}
      </section>
    </main>
  )
}

export default App
