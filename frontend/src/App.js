import { Container } from "react-bootstrap";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Header from "./components/header";
import Footer from "./components/footer";
import HomeScreen from "./screens/HomeScreen";

function App() {
  return (
    <Router>
      <Header />
      <main className="py-3">
        <Container>
          <Route path="/home" component={HomeScreen} exact />
        </Container>
      </main>

      <Footer />
    </Router>
  );
}

export default App;
