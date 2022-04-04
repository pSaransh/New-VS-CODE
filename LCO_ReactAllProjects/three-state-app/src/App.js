import React, {useState} from "react";
import './App.css';

const App = () => {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <header>Counter App using State</header>
      <h2>Current Value of Count is <br></br>{count}</h2>
      <button onClick={() => setCount(0)}>Reset Counter</button>
      <button onClick={() => count >= 0 && count < 20 ? setCount(count+1):setCount(0)}>+</button>
      <button onClick={() => count > 0 ? setCount(count-1): setCount(0)}>-</button>
    </div>
  );
}

export default App;