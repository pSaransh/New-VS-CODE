import React, {useState} from "react";
import PackageContext from "./Context";
var flipFlag = true;
const Provider = props => {
    const [mission, setMission] = useState({
        mName: 'Go to Russia',
        agent: '007',
        accept: 'Not Accepted' 
    })
    return(
        <PackageContext.Provider
        value={{
            data: mission,
            isMissionAccepted: () => {
                if(flipFlag){
                setMission({...mission, accept:'ACCEPTED'})
                flipFlag = false;
                }
                else{
                    setMission({...mission, accept:'NOT ACCEPTED'})
                flipFlag = true;
                }
            }
        }}
        >
            {props.children }
        </PackageContext.Provider>
    );
}
export default Provider;