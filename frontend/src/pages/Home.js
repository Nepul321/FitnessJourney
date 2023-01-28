import React from "react";
import Navbar from "../components/Navbar";

function Home() {
    return (
        <div className="home">
        <Navbar />
        <div class="container my-5">
         <h1>FitnessJourney</h1>
         <hr />
         <p style={{fontSize : "25px"}}>Newest Posts...</p>
       </div>
        </div>
    )
}

export default Home;