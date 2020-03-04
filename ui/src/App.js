import React, { Component } from "react";
import Search from './components/Search.js';

class App extends Component {

    render(){
        return (
            <div>
            <h1>Welcome to the meal search app</h1>
            <Search/>
            </div>
        )
    }
}

export default App;