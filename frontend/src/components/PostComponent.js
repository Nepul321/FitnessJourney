import React from "react";

function Post(props) {
   const {post} = props;

   console.log(post)

   return (
    <div className="post mb-4">
        <p>Day : {post.day}</p>
        <p>Description : {post.description}</p>
        <p>Date : {post.date}</p>
    </div>
   )
}

export default Post;