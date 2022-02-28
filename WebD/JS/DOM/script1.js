//video number 37

// const red = document.querySelector(".red"); 
// const cyan = document.querySelector(".cyan");
// const violet = document.querySelector(".violet")
// const orange = document.querySelector(".orange");
// const pink = document.querySelector(".pink");
// const colorArray = [red,cyan,violet,orange,pink];
// const center = document.querySelector(".center");
// const getBGColor = (selectedElement) => {
//     return window.getComputedStyle(selectedElement).backgroundColor;
// };

// const colorChanger = (element,color) => {
//     return element.addEventListener("mouseenter",()=>{
//         center.style.background = color;
//         center.innerHTML = getBGColor(element);
//     });
// };

// colorChanger(red,getBGColor(red));
// colorChanger(cyan,getBGColor(cyan));
// colorChanger(violet,getBGColor(violet));
// colorChanger(orange,getBGColor(orange));
// colorChanger(pink,getBGColor(pink));

//video number 47

/**                                                  👇Child Text Node
 * <li class = "float-end"> JavaScript Course <span>Price</span></li>
 * Element☝️                  Text Node☝️      ☝️Child Element
 */

const courses = [
    {
        name: "JavaScript Course",
        price: "2.1",
    },
    {
        name: "React Course",
        price: "2.7",
    },
    {
        name: "C++ Bootcamp",
        price: "2.3",
    },
    {
        name: "MERN Course",
        price: "2.4",
    },
    {
        name: "Web Developement Course",
        price: "2.0",
    }
]

function generateList(){
    const ul = document.querySelector('.list-group');
    ul.innerHTML = "";
    courses.forEach(course => {
        const li = document.createElement('li');
        li.classList.add("list-group-item");
        const name = document.createTextNode(course.name);
        li.appendChild(name);

        const span = document.createElement('span');
        span.classList.add("float-end");
        const price = document.createTextNode("$"+course.price);
        span.appendChild(price);

        li.appendChild(span);
        ul.appendChild(li);
    });
}


window.addEventListener("load",generateList);
const button = document.querySelector(".sort-btn")
button.addEventListener("click",() => {
    courses.sort((a,b)=>parseFloat(a.price) - parseFloat(b.price))  ;
    generateList();
});
