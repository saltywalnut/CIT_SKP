import { Button, Input, Rating, Dropdown, Icon, Label} from "semantic-ui-react";
import React from "react";
import moment from "moment"

var x = "test";
x = "test 2";
let y = "not test";
y = "maybe test";
const z = "test2";
// z = "test3"

function App() {
  return (
    <div>
      <Name />
      <p>a</p>
      <Good />
      <TestInput />
    </div>
  );
}

class TestInput extends React.Component {
  constructor() {
    super();
    this.state = { message: "",user: "", messagelist: [] };
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
            alert(this.state.message+this.state.user);
            this.setState({
              messagelist: [...this.state.messagelist, {msg:this.state.message,u:this.state.user,likes:3}],
              message: "",
              user: ""
            });
          }}
        >
          {" "}
          Button{" "}
        </Button>{" "}
        {this.state.messagelist.map((m, idx) => (
          <p> {m.u} : {m.msg} {moment().format("AHm")}
          <div>
            <Button as='div' labelPosition='right'>
              <Button icon onClick = {()=> {
                let s = this.state.messagelist
                s[idx].likes +=1
                this.setState({messagelist:s})
              }} >
                <Icon name='heart' />
                Like
              </Button>
              <Label as='a' basic pointing='left'>
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

// function alert() {
//   alert (TestInput);
// }

const languageOptions = [
  { key: "Arabic", text: "Arabic", value: "Arabic" },
  { key: "Chinese", text: "Chinese", value: "Chinese" },
  { key: "Danish", text: "Danish", value: "Danish" },
  { key: "Dutch", text: "Dutch", value: "Dutch" },
  { key: "English", text: "English", value: "English" },
  { key: "French", text: "French", value: "French" },
  { key: "German", text: "German", value: "German" },
  { key: "Greek", text: "Greek", value: "Greek" },
  { key: "Hungarian", text: "Hungarian", value: "Hungarian" },
  { key: "Italian", text: "Italian", value: "Italian" },
  { key: "Japanese", text: "Japanese", value: "Japanese" },
  { key: "Korean", text: "Korean", value: "Korean" },
  { key: "Lithuanian", text: "Lithuanian", value: "Lithuanian" },
  { key: "Persian", text: "Persian", value: "Persian" },
  { key: "Polish", text: "Polish", value: "Polish" },
  { key: "Portuguese", text: "Portuguese", value: "Portuguese" },
  { key: "Russian", text: "Russian", value: "Russian" },
  { key: "Spanish", text: "Spanish", value: "Spanish" },
  { key: "Swedish", text: "Swedish", value: "Swedish" },
  { key: "Turkish", text: "Turkish", value: "Turkish" },
  { key: "Vietnamese", text: "Vietnamese", value: "Vietnamese" },
];

function popup() {
  alert(z);
}

const Good = () => (
  <div>
    <h1> not hello</h1>{" "}
    <Dropdown
      button
      className="icon"
      floating
      labeled
      icon="world"
      options={languageOptions}
      search
      text="Select Language"
    />
  </div>
);

function Name() {
  return (
    <div>
      <h1> hello </h1>
      <button onClick={popup}>a</button>
      <Button primary onClick={popup}>
        {y}
      </Button>
      <Input focus placeholder={x} />
      <Rating icon="star" defaultRating={3} maxRating={4} />
    </div>
  );
}

export default App;
