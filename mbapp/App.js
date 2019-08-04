import React, { Component } from "react";
import {
  Platform,
  StyleSheet,
  Text,
  View,
  TextInput,
  Button
} from "react-native";

export default class App extends Component {
  state = {
    isVisible: false,
    customerID: ""
  };

  renderResults = () => {
    this.setState({
      isVisible: !this.state.isVisible, //toggles the visibilty of the text
      customerID: this.state.customerID
    });
  };

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.welcome}>Welcome to Milkbasket Assist!</Text>
        <Text style={styles.instructions}>
          To get started, enter the Customer ID
        </Text>
        <TextInput style={styles.input} placeholder="Customer ID" />
        <Button
          style={styles.inputButton}
          title="GOO"
          onPress={this.renderResults}
        />
        {this.state.isVisible
          ? fetch("http://127.0.0.1/api/mobile/bpm/1122016", {
              method: "POST",
              headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
              },
              body: JSON.stringify()
            })
          : null}
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#F5FCFF"
  },
  welcome: {
    fontSize: 20,
    textAlign: "center",
    margin: 10
  },
  instructions: {
    textAlign: "center",
    color: "#333333",
    marginBottom: 5
  },
  input: {
    textAlign: "center",
    color: "#333333",
    margin: 10
  },
  input: {
    width: 150,
    textAlign: "center",
    color: "#333333",
    margin: 10
  }
});
