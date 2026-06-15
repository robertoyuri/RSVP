let nome = "João";
let idade = 2;
let v = [1,2,3]
let o = {nome:"João", idade:20}

if(idade>=18){
    console.log("Maior de idade");
} else{
    console.log("Menor");
}
for(let i=0; i <=5; i++){
    console.log(nome);
}
console.log(nome);
let a = 1;
while(a <= idade){
    console.log(a);
    a++;
}

function ola(){
    let ss = document.getElementById("mensagem");
    console.log(ss.innerText);
    if(ss.innerText == "Seja bem vindo convidado"){
        ss.innerText="Volte Sempre!";
        ss.style.background="#000000";
        ss.style.color="#FFFFFF"
    }else{
        ss.innerText="Seja bem vindo convidado";
        ss.style.background="#FFF000";
        ss.style.color="#3A23a1"

    }

}

function soma(a,b){
    let s=a+b;
    return s;
}