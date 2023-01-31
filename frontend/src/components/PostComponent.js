import React from "react";

function Post(props) {
   const {post} = props;

   return (
    <div className="post mb-4">
        <div className="card mb-3">
    <div className="row g-0">
      <div className="col-md-4">
        <img src={post.image} className="img-fluid rounded-start" alt="..." />
      </div>
      <div className="col-md-8">
        <div className="card-body">
          <h5 className="card-title">Day : {post.day}</h5>
          <p className="card-text">{post.date}</p>
          <p className="card-text">@{post.user.username}</p>
          <a href="/" className="btn btn-outline-primary">View</a>
          {/* <div className="btn-group">
            <a href="" className="btn btn-outline-primary">View</a>
            <a href="" className="btn btn-outline-secondary">Edit</a>
          </div> */}
        </div>
      </div>
    </div>
  </div>
    </div>
   )
}

export default Post;