import React, { useEffect, useState } from 'react';
import API_BASE_URL from '../config';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/api/leaderboard/`);
        if (!response.ok) throw new Error('Failed to fetch leaderboard');
        const data = await response.json();
        // Sort by rank
        const sorted = data.sort((a, b) => a.rank - b.rank);
        setLeaderboard(sorted);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading leaderboard...</p></div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h1>Leaderboard</h1>
      <table className="table table-striped table-hover">
        <thead className="table-dark">
          <tr>
            <th>Rank</th>
            <th>Username</th>
            <th>Score</th>
            <th>Total Activities</th>
            <th>Total Duration (mins)</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map(entry => (
            <tr key={entry._id}>
              <td>#{entry.rank}</td>
              <td>{entry.user_details?.username || entry.user}</td>
              <td><strong>{entry.score}</strong></td>
              <td>{entry.total_activities}</td>
              <td>{entry.total_duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;
