import React from "react";
import Navbar from "../components/Navbar";
import Posts from "../components/Posts";
import { useState, useEffect } from "react";
import {backend} from '../lookups'

function Home() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetch(`${backend}/posts/`)
        .then(res => {
            return res.json();
        })

        .then(data => {
            setPosts(data);
        })
    })

    return (
        <div className="home">
        <Navbar />
        <div className="container my-5">
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