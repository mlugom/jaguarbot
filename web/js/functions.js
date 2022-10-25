function publishCmdVel(message){

}

function moveForward(){
    var twist = new ROSLIB.message({
        linear: {
            x: 5,
            y: 0,
            z: 0
        },
        angular: {
            x: 0,
            y: 0,
            z: 0
        }
    });
    publishCmdVel(twist);
}

function moveBackward(){
    var twist = new ROSLIB.message({
        linear: {
            x: -5,
            y: 0,
            z: 0
        },
        angular: {
            x: 0,
            y: 0,
            z: 0
        }
    });
    publishCmdVel(twist);
}

function turnLeft(){

}

function turnRight(){

}

var ros = new ROSLIB.Ros({
    // Edit this URL according to the machine which runs ROS
    url: 'ws://localhost:9090'
});

ros.on('connection',function(){
    console.log('Connected to Websocket server.');
});

ros.on('error',function(error){
    console.log(`Error: ${error}`);
});

ros.on('close',function(){
    console.log('Connection terminated.');
});