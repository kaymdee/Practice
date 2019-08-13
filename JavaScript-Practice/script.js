console.log('Hello');


const likeBtn =
  document.querySelector("#like");

const likeAction = () => {
  //likeBtn.style.backgroundColor = "Magenta";
//  likeBtn.style.width = "300px";
//  likeBtn.style.height = "300px";
//  likeBtn.style.borderRadius = "50%";

//};
likeBtn.classList.add("magenta-cir");
};


likeBtn.addEventListener("mouseover", likeAction);

const likeAction2 = () => {
  likeBtn.classList.remove("magenta-cir");
}4
  likeBtn.addEventListener("mouseout", likeAction2);


//re-comment out ------------------------
//experime
console.log(likeBtn);
likeBtn.style.color = "blue";
likeBtn.style.backgroundColor = "gold";


const sayHello = () => {
  likeBtn.style.color = "gold";
  likeBtn.style.backgroundColor = "blue";
  likeBtn.innerHTML = "Liked!";
  console.log("Hello!");
}
likeBtn.addEventListener("click", sayHello);

const subBtn =
  document.querySelector("#sub");
  //declare/initalize final constant to equal btn object from html

console.log(subBtn);
subBtn.style.color = "white"
subBtn.style.backgroundColor = "red";
//subBtn.style.fontSize = 20px;

const confirmSub = () => {
  subBtn.style.color = "white";
  subBtn.style.backgroundColor = "grey";
  subBtn.innerHTML = "Subscribed!";
  console.log("User Subscribed");


  //if (confirmSub)
}
subBtn.addEventListener("click", confirmSub);

/*
likeBtn{
  transition: 400ms all;
}
button {
  transition: 1000ms all;
}*/

//mdn
/*
---ccs--- (this is a .js file)
#Like {
color: blue;
}
-----------
console.log('Hello');
console.log('Hello again');
console.log('Wassup?');
let name = "Linda";
name = "Karen"
console.log(name);

if (name === "Linda"){
  console.log("Such a meme");
  console.log("hahaha lol never gets old");
}

if (name === "Karen"){
  console.log("yet another meme");
  console.log("lol let him see the kids Karen");
}
else {
  console.log("You're not Linda..");
  console.log("Idk you go away Karen nobody cares");
}


let name = "Karen";
console.log(name);

let age = 18;

let meme_names =
            name === "Karen" || "Linda";

if (!(meme_names)){
  console.log("Who are you?");
  console.log("lol idc");
}


/*
if (user === "Beyonce"){
  console.log("Greetings, Queen Bee");
} else if(user === "Tyler"){
  console.log("Greetigs Tyler, how was it on Dema?");
}else if (user === "Josh Dun"){
  console.log("You aren't real");
}else{
  console.log("Who are you?");
}
//////
if (name === "Karen" || age === 18){
  console.log("Nobody cares Karen");
  console.log("such a meme lol");
}*/
