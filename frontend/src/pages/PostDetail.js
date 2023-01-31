import React from "react";
import { useParams } from "react-router-dom";

function PostDetail(props) {
    const {id} = useParams();
    return (
        <div className="PostDetail container my-5">
            <h1>Day {id}</h1>
        </div>
    )
}

export default PostDetail;