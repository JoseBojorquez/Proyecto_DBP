let hr = min = sec = ms = "0" + 0, startTimer, timeStartSubmit, timeEndSubmit, dateSubmit, newRecord = true;

const startBtn = document.querySelector(".start"),
    stopBtn = document.querySelector(".stop"),
    resetBtn = document.querySelector(".reset"),
    submitBtn = document.querySelector(".submit");

startBtn.addEventListener("click",start);
stopBtn.addEventListener("click",stop);
resetBtn.addEventListener("click",reset);
submitBtn.addEventListener("click",submit);

function start() {
    startBtn.classList.add("active");
    stopBtn.classList.remove("stopActive");
    resetBtn.classList.remove("resetActive");
    submitBtn.classList.add("submitActive");

    if(newRecord) {
        timeStartSubmit = getTime();
        dateSubmit = getDate();
        newRecord = false;
    }

    startTimer = setInterval(() => {
        ms++;
        ms = ms < 10 ? "0" + ms : ms;

        if(ms == 100) {
            sec++;
            sec = sec < 10 ? "0" + sec : sec;
            ms = "0" + 0;
        }
        if(sec == 60) {
            min++;
            min = min < 10 ? "0" + min : min;
            sec = "0" + 0;
        }
        if(min == 60) {
            hr++;
            hr = hr < 10 ? "0" + hr : hr;
            min = "0" + 0;
        }

        putValue();

    }, 10)
}

function stop() {
    startBtn.classList.remove("active");
    stopBtn.classList.add("stopActive");
    submitBtn.classList.remove("submitActive");
    timeEndSubmit = getTime();
    clearInterval(startTimer);
}

function reset() {
    startBtn.classList.remove("active");
    stopBtn.classList.add("stopActive");
    resetBtn.classList.add("resetActive");
    submitBtn.classList.add("submitActive");
    newRecord = true;
    clearInterval(startTimer);
    hr = min = sec = ms = "0" + 0;
    putValue();
}

function submit() {
    const description = document.getElementById("desInput");
    if(description.value != null) {
        if(isEmpty(description.value) == 0) {
            postRecord(description.value)
            description.value = "";
            reset();
        }
    }
}

function putValue() {
    document.querySelector('.millisecond').innerHTML = ms;
    document.querySelector('.second').innerHTML = sec;
    document.querySelector('.minute').innerHTML = min;
    document.querySelector('.hour').innerHTML = hr;
}

function getDate() {
    var now     = new Date(); 
    var year    = now.getFullYear();
    var month   = now.getMonth()+1; 
    var day     = now.getDate();
    if(month.toString().length == 1) {
        month = '0'+month;
    }
    if(day.toString().length == 1) {
        day = '0'+day;
    }     
    var date = year+'-'+month+'-'+day;   
    return date;
}

function getTime() {
    var now     = new Date();
    var hour    = now.getHours();
    var minute  = now.getMinutes();
    var second  = now.getSeconds();  
    if(hour.toString().length == 1) {
        hour = '0'+hour;
    }
    if(minute.toString().length == 1) {
        minute = '0'+minute;
    }
    if(second.toString().length == 1) {
        second = '0'+second;
    }   
    var time = hour+':'+minute+':'+second;   
    return time;
}

function isEmpty(str) {
    return !str.trim().length;
}

async function postRecord(description) {
    var duration = hr+':'+min+':'+sec;  
    const response = await fetch("http://localhost:8000/time_records/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: `{
            "user_uuid": "6c7f1194-a612-41f2-bce4-cf82537469c6",
            "description": "${description}",
            "duration": "${duration}",
            "start": "${timeStartSubmit}",
            "end": "${timeEndSubmit}",
            "date": "${dateSubmit}"
        }`,
    });

    response.json().then(data => {
        console.log(JSON.stringify(data));
    });
}