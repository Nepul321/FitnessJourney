import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { backend } from "../lookups";

function Post(props) {
    const {post} = props;
    return (
        <div className="post">
             <img src={post.image} style={{ height: "auto", width: "100%" }} alt="" />
             <br /> <br />
             <p>By Nepul Kahandawa (@{post.user.username})</p>
             <p>On {post.date}</p>
             <p>Views : {post.view_count}</p>
             <p style={{fontSize : '20px'}}>{post.description}</p>
        </div>
    )
}

function PostDetail(props) {
    const {id} = useParams();
    const [post, setPost] = useState(null);

    useEffect(() => {
        fetch(`${backend}/posts/${id}/`)
        .then((res) => {
          if (res.status === 200) {
            return res.json();
          } else if (res.status === 403) {
            alert("You don't have access to view this post");
            window.location.href = "/";
          } else if (res.status === 404) {
            window.location.href = "/";
          } else if (res.status === 500) {
            alert("An error occurred. Please try again.");
          }
  
          return {};
        })
  
        .then((data) => {
          setPost(data);
        });
    })
    return (
        <div className="PostDetail container my-5">
            <h1>Day {id}</h1>
            <hr />
            {post === null ? null : <Post post={post}/>}
            <a href="/" className="my-3 btn btn-primary">Back to home</a>
        </div>
    )
}

export default PostDetail;