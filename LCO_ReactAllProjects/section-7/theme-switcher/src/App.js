import React, {useState} from "react";
import ThemeContext from "./Context/ThemeContext";
import AppTheme from "./Colors";
import ThemeToggler from "./Components/ThemeToggler";
import logo from './logo.svg'
import './App.css'
function App() {
  const themeHook = useState('light');
  //const currentTheme = HeroSection;
  return (
    <div className="App">
      <header className="App-header"
      style={
      {
        color:`${AppTheme[themeHook[0]].textColor}`,
        background: `${AppTheme[themeHook[0]].backgroundColor}`
      }
      }>
        <img src={logo} className="App-logo" alt="logo" />
        <p>This application toggles Theme.</p>
        <ThemeContext.Provider value={themeHook}>
          <ThemeToggler></ThemeToggler>
          {console.log(AppTheme[themeHook[0]])}
        </ThemeContext.Provider>
      </header>
    </div>
  );
}

export default App;
