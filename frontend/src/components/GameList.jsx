import { useState, useEffect } from 'react';
import './GameList.css';

function GameList() {
  const [games, setGames] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/games/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`Error HTTP: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Datos recibidos:', data);
        setGames(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="loading">Cargando juegos...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="game-list">
      <h1>🎲 Juegos de Mesa</h1>
      {games.length === 0 ? (
        <p className="no-games">No hay juegos disponibles.</p>
      ) : (
        games.map(game => (
          <div key={game.id} className="game-card">
            <h2>{game.title}</h2>
            <p className="description">{game.description || 'Sin descripción'}</p>
            <p className="date"><small>Creado: {new Date(game.created).toLocaleDateString()}</small></p>
            
            <h4>Reseñas ({game.reviews?.length || 0})</h4>
            {game.reviews && game.reviews.length > 0 ? (
              <ul className="reviews-list">
                {game.reviews.map(review => (
                  <li key={review.id} className="review-item">
                    <strong>{review.user_name}</strong>
                    <span className="rating">
                      {'★'.repeat(review.rating)}{'☆'.repeat(5 - review.rating)}
                    </span>
                    <span className="comment">: {review.comment}</span>
                    <br />
                    <span className="date">{new Date(review.created).toLocaleDateString()}</span>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="no-reviews">No hay reseñas para este juego. ¡Sé el primero en comentar!</p>
            )}
          </div>
        ))
      )}
    </div>
  );
}

export default GameList;