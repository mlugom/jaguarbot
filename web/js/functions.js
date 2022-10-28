function publishCmdVel(twist){
    cmdVel.publish(twist);
    //console.log(twist);
}

function moveForward(){
    var twist = new ROSLIB.Message({
        linear: {
            x: 0.5,
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
    var twist = new ROSLIB.Message({
        linear: {
            x: -0.5,
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
    var twist = new ROSLIB.Message({
        linear: {
            x: 0,
            y: 0,
            z: 0
        },
        angular: {
            x: 0,
            y: 0,
            z: 2
        }
    });
    publishCmdVel(twist);
}

function turnRight(){
    var twist = new ROSLIB.Message({
        linear: {
            x: 0,
            y: 0,
            z: 2
        },
        angular: {
            x: 0,
            y: 0,
            z: -0.8
        }
    });
    publishCmdVel(twist);
}

function stop(){
    var twist = new ROSLIB.Message({
        linear: {
            x: 0,
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

function sleep(ms){
    return new Promise(resolve => setTimeout(resolve,ms));
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


var cmdVel = new ROSLIB.Topic({
    ros: ros,
    name: '/cmd_vel',
    messageType: 'geometry_msgs/Twist'
});

// Buttons
var forwardButton = document.getElementById('forward');
var backwardButton = document.getElementById('backward');
var leftButton = document.getElementById('left');
var rightButton = document.getElementById('right');
/*
while(true){
    console.log('Hola');
    sleep(1000);
}*/

