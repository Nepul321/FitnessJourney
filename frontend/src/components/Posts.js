import React from "react";
import Post from "./PostComponent";

function Posts(props) {
 const {posts} = props;
 return (
    <div className="posts">
    {posts.map((item, key) => {
        return <Post post={item} key={key}/>
    })}
    </div>
 )
}

export default Posts;