import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaders(results);
        console.log('Fetched leaderboard:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div>
      <h1 className="mb-4 display-6 text-primary">Leaderboard</h1>
      <div className="table-responsive">
        <table className="table table-striped table-bordered align-middle">
          <thead className="table-primary">
            <tr>
              {leaders.length > 0 && Object.keys(leaders[0]).map((key) => (
                <th key={key}>{key.charAt(0).toUpperCase() + key.slice(1)}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {leaders.map((leader, idx) => (
              <tr key={leader.id || idx}>
                {leaders.length > 0 && Object.keys(leaders[0]).map((key) => (
                  <td key={key}>{String(leader[key])}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
        {leaders.length === 0 && <div className="alert alert-info">No leaderboard data found.</div>}
      </div>
    </div>
  );
};

export default Leaderboard;
