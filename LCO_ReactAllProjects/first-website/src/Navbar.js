import React from "react";

const NavBar = () => {
    return(
    <div className="justify-content-end">
      <nav className="navbar navbar-expand-lg text-white bg-dark">
      <a className="navbar-brand text-success" href="http://localhost:3000">Navbar</a>

      
      <div className="collapse navbar-collapse ">
        <ul className="navbar-nav mr-auto ">
          <li className="nav-item active">
            <a className="nav-link text-white" href="http://localhost:3000">Home </a>
          </li>
          <li className="nav-item">
            <a className="nav-link text-white" href="http://localhost:3000">About Us</a>
          </li>
          <li className="nav-item dropdown">
            <a href="http://localhost:3000" className="nav-link text-white">
              Products
            </a>
          </li>
          <li className="nav-item ">
            <a className="nav-link disabled" href="http://localhost:3000">Meeting</a>
          </li>
        </ul>
      </div>
    </nav>
    </div>
    );
}

export default NavBar;