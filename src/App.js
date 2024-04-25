// src/App.js

import React from 'react';

import Services from './comps/Services';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="text-3xl font-bold text-center mb-8">Service Booking App</h1>
      </header>
      <Services />
    </div>
  );
}

export default App;
