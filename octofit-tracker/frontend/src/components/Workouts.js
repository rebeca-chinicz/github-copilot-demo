import React, { useEffect, useState } from 'react';
import API_BASE_URL from '../config';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/api/workouts/`);
        if (!response.ok) throw new Error('Failed to fetch workouts');
        const data = await response.json();
        setWorkouts(data);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading workouts...</p></div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h1>Workouts</h1>
      <div className="row">
        {workouts.map(workout => (
          <div key={workout._id} className="col-md-4 mb-4">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{workout.name}</h5>
                <p className="card-text">
                  <strong>Difficulty:</strong> <span className="badge bg-info">{workout.difficulty_level}</span>
                </p>
                <p className="card-text">
                  <strong>Duration:</strong> {workout.duration} minutes
                </p>
                <p className="card-text">
                  <strong>Target:</strong> {workout.target_audience}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;
