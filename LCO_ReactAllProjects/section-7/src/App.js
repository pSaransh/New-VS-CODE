import React, {useState, Fragment} from "react";
import './App.css'
import Provider from "./Provider";
import Context from "./Context";
//export default App;
//---------------------Drilling----------------
const Agents = () => {
  return(
    <Agent1/>
  );
}
const Agent1 = () => {
  return(
    <Agent2/>
  );
}
const Agent2 = () => {
  return(
    <AgentBond/>
  );
}
const AgentBond = () => {
  return(
    <Context.Consumer>
      {
        (context) => (
          <Fragment>
            <h3>Agent Information</h3>
            <p style={{color:'blue', textDecoration: 'underline'}}>Mission Name: {context.data.mName}</p>
            <h2>Mission Status: {context.data.accept}</h2>
            <button onClick={context.isMissionAccepted}>Flip Mission Status</button>
          </Fragment>
        )
      }
    </Context.Consumer>
  );
}
//------------Drilling Ends----------
const App = () => {
  return(
    <div>
      <h1>Context API</h1>
      <Provider>
        <Agents />
      </Provider>
    </div>
  );
}

export default App;