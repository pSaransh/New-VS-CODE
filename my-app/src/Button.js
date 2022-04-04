import React from "react";

const Button = ({title=undefined}) => (
    <div>
        <button className="button">{title}</button>
    </div>
);

export default Button;