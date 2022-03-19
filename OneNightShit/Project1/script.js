const hisBirthday = '1 December 2022';
const countDown = () => {
    const birthDate = new Date(hisBirthday);
    const currentDate = new Date();
    const seconds = Math.floor((birthDate-currentDate)/1000);
    const minutes = Math.floor(seconds/60);
    const hours = Math.floor(minutes/60);
    const days = Math.floor(hours/24);
    const htmlSeconds = document.getElementById("seconds");
    const htmlMinutes = document.getElementById("mins");
    const htmlHours = document.getElementById("hours");
    const htmlDays = document.getElementById("days");
    htmlSeconds.innerHTML = seconds%60;
    htmlMinutes.innerHTML = minutes%60;
    htmlHours.innerHTML = hours%60;
    htmlDays.innerHTML = days
};
//initial call
setInterval(countDown,1000)