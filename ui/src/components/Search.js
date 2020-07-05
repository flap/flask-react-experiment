import React, { Component } from "react";
import { IconButton, TextField } from '@material-ui/core';
import SearchIcon from '@material-ui/core/SvgIcon';
import AnimatedModal from './AnimatedModal.js'

class Search extends Component {

    state = {
        searchedValue: '',
        answer: null,
        modalShow: false
    };

    handleOnChange = event => {
        this.setState({ searchedValue: event.target.value });
    };

    fetchAnswer = () => {
        var searchUrl = `https://api.exchangeratesapi.io/2010-01-12`;
        fetch(searchUrl)
        .then(response => {
            return response.json();
        })
        .then(jsonData => {
            console.log(jsonData.rates)
            this.setState({ answer: jsonData.base})
            console.log(this.state.answer)
            this.setState({ modalShow: true })
        });
    };

    render() {
        return (
            <div>
                <TextField
                    onChange={event => this.handleOnChange(event)}
                    value={this.state.searchedValue}
                />
                <IconButton onClick={this.fetchAnswer}>
                    <SearchIcon/>
                </IconButton>
                <AnimatedModal 
                    open={this.state.modalShow}
                    onClose={() => this.setState({ modalShow: false })}
                    content={this.state.answer}
                />
            </div>
        )
    }
}

export default Search;