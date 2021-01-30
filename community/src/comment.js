import React from "react";
import moment from "moment";
import { Button, Input, Icon, Label, Grid } from "semantic-ui-react";

class Comments extends React.Component {
  constructor() {
    super();
    this.state = { message: "", user: "unknown", messagelist: [] };
  }
  render() {
    console.log(this.state.message);
    console.log(this.state.messagelist);
    return (
      <div>
        <Grid>
          <Grid.Row columns={3}>
            <Grid.Column width={5}></Grid.Column>
            <Grid.Column width={9}>
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
            </Grid.Column>
            <Grid.Column width={1}></Grid.Column>
          </Grid.Row>
        </Grid>
      </div>
    );
  }
}
export default Comments;
