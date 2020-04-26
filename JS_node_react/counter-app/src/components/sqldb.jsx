import React, { Component } from "react";

class SQLDB extends Component {
  state = {};

  getData() {
    return "a";
  }
  render() {
    console.log("Render- SQL***");
    return <div>{this.getData}</div>;
  }
}

export default SQLDB;
