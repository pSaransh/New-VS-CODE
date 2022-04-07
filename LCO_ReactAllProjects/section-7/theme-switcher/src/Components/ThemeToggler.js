import React, {useContext} from "react";
import ThemeContext from "../Context/ThemeContext";

const ThemeToggler = () => {
    const [themeMode,setThemeMode] = useContext(ThemeContext);

    return(
            <button className="App-link" onClick={()=>{
                setThemeMode(themeMode==='light'?'dark':'light');
            }}>{themeMode==='light'?'Dark Mode':'Lights On'}</button>
    );
}

export default ThemeToggler;