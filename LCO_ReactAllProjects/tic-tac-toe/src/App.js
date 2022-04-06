import {React,useState} from 'react';
import Icon from './components/Icon';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css'

import {Card, CardBody, Button, Container, Col, Row} from 'reactstrap'
import 'bootstrap/dist/css/bootstrap.css'
import './App.css';

const itemArray = new Array(9).fill("empty");
const App = () => {
  const [isCross,setIsCross] = useState(false);
  const [winMessage, setWinMessage] = useState("");

  const reloadGame = () => {
    setIsCross(false);
    setWinMessage("");
    itemArray.fill("empty",0,8);
  };

  const checkIsWinner = () => {

  };

  const changeItem = (itemNumber) =>{
    if(winMessage)
      return toast(winMessage, {type: "success"});
    
    if(itemArray[itemNumber] === "empty"){
      itemArray[itemNumber] = isCross?"cross":"circle";
      setIsCross(!isCross);
    }
    else
      return toast("Already filled", {type:"error"});

    checkIsWinner();
if(!itemArray.include("empty")){
reloadGame();
}
  }
  return (
    <Container className='p-5'>
      <ToastContainer position='bottom-center'/>
      <Row>
        <Col md={6} className="offset-md-3">
          {winMessage ? (
            <div className='mb-2 mt-2'>
              <h1 className='text-success text-uppercase text-center'>
                {winMessage}
              </h1>
              <Button color='success' block onClick={reloadGame}>Reload the Game</Button>

            </div>
          ) : (
            <h1 className='text-center text-warning'>
              {isCross ? "Cross": "Circle"} Turn
            </h1>
          )}
          <div className='grid'>
            {
              itemArray.map((item,index) => {return (
                <Card onClick={changeItem(index)}>
                  <CardBody className='box'>
                    <Icon name={item}/>
                  </CardBody>
                </Card>
              )})
            }
          </div>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
