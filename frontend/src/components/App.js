import React, {Component} from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert';
import {render} from "react-dom";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        const data = new FormData(event.target);

        const urlPromise = fetch('/generate', {
            method: 'POST',
            body: data,
        });
        urlPromise.then(data => data.json())
            .then(data => {
                this.setState({data: data.data});
                this.setState({status: data.status});
                this.setState({msg: data.msg});
                console.log(this.state.data) // Show log in in success func

            });
    }

    render() {
        const hasError = this.state.msg != 'OK' && Object.keys(this.state.data).length > 0;
        let alertInfo;
        if (hasError) {
            alertInfo = <Alert variant='danger'>
                {this.state.data.original_url}
            </Alert>
        } else if (Object.keys(this.state.data).length > 0) {
            alertInfo = <Alert variant='info'>
                {this.state.data.short_url}
            </Alert>
        }
        return (
            <div className="container register-form">
                <div className="form">
                    <div className="note">
                        <p>This is a simple short URL generator.</p>
                    </div>
                    <Form onSubmit={this.handleSubmit}>
                        <Form.Group controlId="formURLShortener">
                            <Form.Label>URL</Form.Label>
                            <Form.Control name="original_url" type="text" placeholder="Paste In your URL"/>
                            <Form.Text className="text-muted">
                            </Form.Text>
                        </Form.Group>
                        <Form.Group>
                            {alertInfo}
                        </Form.Group>
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>

                    </Form></div>
            </div>
        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App/>, container);
