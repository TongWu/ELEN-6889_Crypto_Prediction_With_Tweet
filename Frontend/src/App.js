import React from 'react';
import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {HomePage} from './Components/HomePage';
import {BitcoinPage} from './Components/Bitcoin';
import {EthereumPage} from './Components/Ethereum';
import {ComparisonPage} from './Components/Comparison';


function App() {
  return <BrowserRouter>
    <Routes>
      <Route path="/" element={<HomePage/>}/>
      <Route path="/bitcoin" element={<BitcoinPage/>}/>
      <Route path="/ethereum" element={<EthereumPage/>}/>
 
      <Route path="/comparison" element={<ComparisonPage/>}/>
    </Routes>
  </BrowserRouter>
}

export default App;
