import React from "react";

const TextInput = () => {

    const oc = (index) =>{
        
    } 


    return(
        <div className="textfield">
            <div className="letterbox" onChange={() => oc(0)}></div>
            <div className="letterbox" onChange={() => oc(1)}></div>
            <div className="letterbox" onChange={() => oc(2)}></div>
            <div className="letterbox" onChange={() => oc(3)}></div>
            <div className="letterbox" onChange={() => oc(4)}></div>
        </div>
    )
}

export default TextInput