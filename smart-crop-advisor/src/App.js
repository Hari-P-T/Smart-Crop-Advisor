import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [image, setImage] = useState('');

  const runScript = async () => {
    try {
      const response = await axios.post('http://localhost:3001/run-script');
      if (response.status === 200) {
        setImage('http://localhost:3001/images/bar_graph.png');
      }
    } catch (error) {
      console.error('Error running script:', error);
    }
  };

  return (
    <div className="App">
      <h1>CodeVerse Crop Prediction</h1>
      <button onClick={runScript}>Run Script</button>
      {image && <img src={image} alt="Bar Graph" />}
    </div>
  );
}

export default App;
