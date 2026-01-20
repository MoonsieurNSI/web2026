let b1 = document.querySelector('.btn1');
let b2 = document.querySelector('.btn2');
let body = document.querySelector('body');
let titre = document.querySelector('.title');
let range = document.getElementById('range');
let text = document.getElementById('text');
let toggle= false;  //console.log(b1);
let newTitre = "Nouveau Titre";

console.log(range);
range.addEventListener("change", ()=>{
  console.log(range.value);
  text.innerHTML = range.value;
});

b2.addEventListener('click', () => {
console.log("hihi");

  const newDiv = document.createElement("p");

  // and give it some content
  const newContent = document.createTextNode("Hi there and greetings!");

  // add the text node to the newly created div
  newDiv.appendChild(newContent);

document.body.insertBefore(newDiv, document.body.firstChild);
});
b1.addEventListener('click', () => {
  console.log("coucou");  
  console.log(titre.innerHTML);
  if (!toggle){
    titre.innerHTML = newTitre;
    newTitre = "Ancien Titre";
    toggle= true;
    body.style.backgroundColor = "lightblue";
  }
  else{
    titre.innerHTML = newTitre;
    newTitre = "Nouveau Titre";
    toggle= false;
  }
  
});
