import Home from "./pages/Home";
import { Route, Routes } from "react-router-dom";
import About from "./pages/About";
import PostDetail from "./pages/PostDetail";

function App() {
  return (
    <div className="App">
        <Routes>
        <Route path="/" exact element={<Home />}></Route>
        <Route path="/about" exact element={<About />}></Route>
        <Route path="/posts/:id" exact element={<PostDetail />}></Route>
      </Routes>
    </div>
  );
}

export default App;
