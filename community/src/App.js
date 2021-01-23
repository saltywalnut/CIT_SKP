import logo from "./logo.svg";
import "./App.css";
import {
  Button,
  Input,
  Rating,
  Dropdown,
  Icon,
  Label,
} from "semantic-ui-react";
import React from "react";
import moment from "moment";

function App() {
  return (
    <div>
  <Button>Log In</Button>
      <TestInput />
    </div>
  );
}
class TestInput extends React.Component {
  constructor() {
    super();
    this.state = { message: "", user: "", messagelist: [] };
  }
  render() {
    console.log(this.state.message);
    console.log(this.state.messagelist);
    return (
      <div>
        <Input
          onChange={(e) => {
            this.setState({ user: e.target.value });
          }}
          value={this.state.user}
        />{" "}
        <Input
          onChange={(e) => {
            this.setState({ message: e.target.value });
          }}
          value={this.state.message}
        />{" "}
        <Button
          onClick={() => {
            alert(this.state.message + this.state.user);
            this.setState({
              messagelist: [
                ...this.state.messagelist,
                {
                  msg: this.state.message,
                  u: this.state.user,
                  likes: 0,
                  t: moment().format("AHm/s"),
                },
              ],
              message: "",
              user: "",
            });
          }}
        >
          {" "}
          Button{" "}
        </Button>{" "}
        {this.state.messagelist.map((m, idx) => (
          <p>
            {" "}
            {m.u} : {m.msg} {m.t}
            <div>
              <Button as="div" labelPosition="right">
                <Button
                  icon
                  onClick={() => {
                    let s = this.state.messagelist;
                    s[idx].likes += 1;
                    this.setState({ messagelist: s });
                  }}
                >
                  <Icon name="heart" />
                  Like
                </Button>
                <Label as="a" basic pointing="left">
                  {m.likes}
                </Label>
              </Button>
            </div>
          </p>
        ))}
      </div>
    );
  }
}
export default App;
