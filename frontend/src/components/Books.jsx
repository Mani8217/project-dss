import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Book() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    // درخواست به API Django
    axios.get('http://localhost:8000/api/books/')
      .then(response => {
        setBooks(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the books!', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Book List</h1>
      <ul>
        {books.map(book => (
         <div className='book-container'>  
            
            <li key={book.id}>
              {book.title} by {book.author}
            </li>
         </div>
        ))}
      </ul>
    </div>
  );
}

export default Book;
