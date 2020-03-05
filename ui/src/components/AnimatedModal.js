import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import Backdrop from '@material-ui/core/Backdrop';
import Fade from '@material-ui/core/Fade';

const useStyles = makeStyles(theme => ({
    modal: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
    },
    paper: {
        backgroundColor: theme.palette.background.paper,
        border: '2px solid #000',
        boxShadow: theme.shadows[5],
        padding: theme.spacing(2, 4, 3),
    },
}));

export default function AnimatedModal(props) {
    const classes = useStyles();

    return (
        <div>
            <Modal
                {...props}
                aria-labelledby="transition-modal-title"
                aria-describedby="transition-modal-description"
                className={classes.modal}
                closeAfterTransition
                BackdropComponent={Backdrop}
                BackdropProps={{
                    timeout: 500,
                }}
            >
            <Fade in={props.open}>
                    <div className={classes.paper}>
                        <h1>{props.content}</h1>
                    {/* {this.state.apiResult.map((apiResult, index) => (
                        <div key={index}>
                            <h1 key={apiResult.idCardNumber.toString()}>{apiResult.idCardNumber}</h1>
                            <h1 key={apiResult.cpfNumber.toString()}>{apiResult.cpfNumber}</h1>
                            <h1 key={apiResult.name}>{apiResult.name}</h1>
                        </div>
                    ))} */}
                    </div>
                </Fade>
            </Modal>
        </div>
    );
}