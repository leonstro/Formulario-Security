document.getElementById("formulario").addEventListener("submit", async function(e) {
    e.preventDefault();
  
    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value;
  
    if (nome.length < 3) {
      alert("Nome deve ter pelo menos 3 caracteres.");
      return;
    }
  
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regexEmail.test(email)) {
      alert("E-mail inválido.");
      return;
    }
  
    const regexSenha = /^(?=.*[A-Z])(?=.*\d).{8,}$/;
    if (!regexSenha.test(senha)) {
      alert("Senha precisa ter no mínimo 8 caracteres, incluindo uma letra maiúscula e um número.");
      return;
    }
  
    const response = await fetch("http://localhost:5000/cadastrar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome, email, senha })
    });
  
    const data = await response.json();
    document.getElementById("mensagem").innerText = data.message;
  });
