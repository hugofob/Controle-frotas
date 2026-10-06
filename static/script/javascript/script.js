/*const botao = document.getElementById('botao-tema');
const body = document.body;

// Persistência do tema
const temasalvo = localStorage.getItem('tema');
temaEscuro(temasalvo === 'escuro');

// Função para alternar entre tema claro e escuro
function temaEscuro(escuro) {
  if (escuro) {
    body.classList.add('escuro');
    botao.innerHTML = '<i class="fa-solid fa-sun"></i>';
  } else {
    body.classList.remove('escuro');
    botao.innerHTML = '<i class="fa-solid fa-moon"></i>';
  }
}

botao.addEventListener('click', function(event) {
  const isescuro = body.classList.toggle('escuro');
  // Impede o link "#" de mudar de página
  event.preventDefault();
  //Alterna entre claro escuro
  const escuro = body.classList.toggle('escuro');
  //Atualiza o ícone
  temaEscuro(escuro);
  //Salva a preferência
  localStorage.setItem('tema',escuro?'escuro','claro';)
};
*/
document.addEventListener('DOMContentLoaded', () => {
  const botao = document.getElementById('botao-tema');
  const body = document.body;

  // Se o botão não for encontrado, avisa no console do navegador para ajudar a diagnosticar
  if (!botao) {
    console.error("Erro: O botão com o ID 'botao-tema' não foi encontrado no HTML.");
    return;
  }

  // Persistência do tema
  const temasalvo = localStorage.getItem('tema');
  temaEscuro(temasalvo === 'escuro');

  // Função para alternar entre tema claro e escuro
  function temaEscuro(escuro) {
    if (escuro) {
      body.classList.add('escuro');
      botao.innerHTML = '<i class="fa-solid fa-sun"></i>';
    } else {
      body.classList.remove('escuro');
      botao.innerHTML = '<i class="fa-solid fa-moon"></i>';
    }
  }

  botao.addEventListener('click', function(event) {
    // Impede o link "#" de mudar de página
    event.preventDefault();
    
    // Alterna a classe e descobre se o corpo ficou escuro
    const escuro = body.classList.toggle('escuro');
    
    // Atualiza o ícone
    temaEscuro(escuro);
    
    // Salva a preferência
    localStorage.setItem('tema', escuro ? 'escuro' : 'claro');
  });
});
