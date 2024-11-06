import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import FastLaneLogo from './images/FastLane Logo Transparent.png';
import SelectorForm from './components/SelectorForm';

const App = () => {
  return (
    <div>
      <img src={FastLaneLogo} alt="FastLaneLogo" />
      <SelectorForm />
    </div>
  );
}

export default App;
