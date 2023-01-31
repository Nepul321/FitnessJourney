import Home from "./pages/Home";
import { Route, Routes } from "react-router-dom";
import About from "./pages/About";

function App() {
  return (
    <div className="App">
        <Routes>
        <Route path="/" exact element={<Home />}></Route>
        <Route path="/about" exact element={<About />}></Route>
      </Routes>
    </div>
  );
}

export default App;
