const inicio = new Date("2024-11-05T14:30:00");

function mostrarPresente(){
    document.getElementById("tela-inicial").style.display="none";
    document.getElementById("tela-principal").style.display="block";
    // ================
}

function atualizarTempo() {
    const agora = new Date();
    
    let anos = agora.getFullYear() - inicio.getFullYear();
    let meses = agora.getMonth() - inicio.getMonth();
    let dias = agora.getDate() - inicio.getDate();
    let horas = agora.getHours() - inicio.getHours();
    let minutos = agora.getMinutes() - inicio.getMinutes();
    let segundos = agora.getSeconds() - inicio.getSeconds();

    // Correções para valores negativos (tipo dia 5 pra dia 3 dá -2)
    if (segundos < 0) {
        segundos += 60;
        minutos--;
    }

    if (minutos < 0) {
        minutos += 60;
        horas--;
    }

    if (horas < 0) {
        horas += 24;
        dias--;
    }

    if (dias < 0) {
        const diasNoMesAnterior = new Date(agora.getFullYear(), agora.getMonth(), 0).getDate();
        dias += diasNoMesAnterior;
        meses--;
    }

    if (meses < 0) {
        meses += 12;
        anos--;
    }

    let texto = "";

    if (anos === 1) texto += `1 ano, `;
    else if (anos > 1) texto += `${anos} anos, `;

    if (meses === 1) texto += `1 mês, `;
    else if (meses > 1) texto += `${meses} meses, `;

    if (dias === 1) texto += `1 dia, `;
    else if (dias > 1 || (anos === 0 && meses === 0)) texto += `${dias} dias, `;

    if (horas === 1) texto += `1 hora, `;
    else if (horas > 1) texto += `${horas} horas, `;

    if (minutos === 1) texto += `1 minuto `;
    else if (minutos > 1) texto += `${minutos} minutos `;

    if (segundos === 1) texto += `e 1 segundo`;
    else if (segundos > 1) texto += `e ${segundos} segundos`;

    texto = texto.trim().replace(/,\s*$/, '');

    document.getElementById("contador").innerText = texto + ".";

    
}

// CONTADOR 
atualizarTempo();
setInterval(atualizarTempo,1000);

// FOTOS

let slideAtual = 0;

const slides = document.querySelectorAll(".slide");
const bolinhas = document.querySelectorAll(".bolinha");

function mudarSlide(indice){
    slides[slideAtual].classList.remove("ativo");
    bolinhas[slideAtual].classList.remove("ativo");

    slideAtual = indice;

    slides[slideAtual].classList.add("ativo");
    bolinhas[slideAtual].classList.add("ativo");
}

setInterval(() =>{
    let proximo = (slideAtual + 1) % slides.length;
    mudarSlide(proximo);
}, 3000);

window.mudarSlide = mudarSlide;
