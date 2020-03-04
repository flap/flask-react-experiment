import React, { Component } from "react";
import { IconButton, TextField } from '@material-ui/core';
import SearchIcon from '@material-ui/core/SvgIcon';
import AnimatedModal from './AnimatedModal.js'

class Search extends Component {

    state = {
        searchValue: '',
        apiResult: []
    };

    handleOnChange = event => {
        this.setState({ searchValue: event.target.value });
    };

    handleSearch = () => {
        var ans = [{
            "idCardNumber": 1.0, 
            "cpfNumber": 12345, 
            "name": "Chocolate and sweets"
        }]
        this.setState({ apiResult: ans });
    }

    // componentDidMount() {
    //     var searchUrl = `http://127.0.0.1:5000/`;
    //     fetch(searchUrl)
    //     .then(response => {
    //         return response.json();
    //     })
    //     .then(jsonData => {
    //         this.setState({ apiResult: jsonData });
    //     });
    // };

    render() {
        return (
            <div>
                <TextField
                    onChange={event => this.handleOnChange(event)}
                    value={this.state.searchValue}
                />
                <IconButton onClick={this.handleSearch}>
                    <SearchIcon/>
                </IconButton>
                {this.state.apiResult.map((apiResult, index) => (
                    <div key={index}>
                        <h1 key={apiResult.idCardNumber.toString()}>{apiResult.idCardNumber}</h1>
                        <h1 key={apiResult.cpfNumber.toString()}>{apiResult.cpfNumber}</h1>
                        <h1 key={apiResult.name}>{apiResult.name}</h1>
                        <AnimatedModal/>
                    </div>
                ))}
            </div>
        )
    }
}

export default Search;