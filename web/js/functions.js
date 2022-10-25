function publishCmdVel(){
    cmdVel.publish(twist);
}

function moveForward(){
    var x_vel = 5;
    twist.linear.x = x_vel;
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
    var twist = new ROSLIB.message({
        linear: {
            x: 0,
            y: 0,
            z: 0
        },
        angular: {
            x: 0,
            y: 0,
            z: 0.8
        }
    });
    publishCmdVel(twist);
}

function turnRight(){
    var twist = new ROSLIB.message({
        linear: {
            x: 0,
            y: 0,
            z: 0
        },
        angular: {
            x: 0,
            y: 0,
            z: 0.8
        }
    });
    publishCmdVel(twist);
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

// Cmd_vel message published
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
while(true){
    
}

