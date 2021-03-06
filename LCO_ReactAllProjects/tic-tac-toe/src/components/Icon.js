import React from "react";
import { FaTimes, FaRegCircle, FaPenAlt } from "react-icons/fa";

const Icon = ({ name }) => {
  switch (name) {
    case "circle":
      return <FaRegCircle className="icons" />;
    case "cross":
      return <FaTimes className="icons" />;
    default:
      return <FaPenAlt className="icons" />;
  }
};

export default Icon;
