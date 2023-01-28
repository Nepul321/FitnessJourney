import React from "react";
import Navbar from "../components/Navbar";
import Posts from "../components/Posts";

function Home() {
    const posts = [
        {
            day : 1,
            description : "abc",
            date : "1-28-2023"
        },
        {
            day : 2,
            description : "def",
            date : "1-29-2023"
        }
    ]
    return (
        <div className="home">
        <Navbar />
        <div class="container my-5">
         <h1>FitnessJourney</h1>
         <hr />
         <p style={{fontSize : "25px"}}>Newest Posts...</p>
         <br />
         <Posts posts={posts}/>
       </div>
        </div>
    )
}

export default Home;