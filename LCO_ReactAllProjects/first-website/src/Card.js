import React from "react";
const Card = ({cardTitle,imageSource,buttonName}) => {
    return(
        <div className="card" style={{width: "18rem"}}>
              <img
                src={imageSource}
                className="card-img-top"
                alt="..."
              />
              <div className="card-body">
                <h5 className="card-title">{cardTitle}</h5>
                <p className="card-text">
                  Some quick example text to build on the card title and make up
                  the bulk of the card's content.
                </p>
                <a href="http://localhost:3000" className="btn btn-success">{buttonName}</a>
              </div>
        </div>
    );
}
export default Card;