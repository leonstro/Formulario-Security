document.getElementById("loginForm").addEventListener("submit", async function(e) {
    e.preventDefault();
  
    const tokenSalvo = localStorage.getItem("token");
  
    if (!tokenSalvo) {
      document.getElementById("mensagemLogin").innerText = "Token não encontrado. Cadastre-se primeiro.";
      return;
    }
  
    const response = await fetch("http://localhost:5050/acesso-restrito", {
      method: "GET",
      headers: {
        "Authorization": "Bearer " + tokenSalvo
      }
    });
  
    const data = await response.json();
    document.getElementById("mensagemLogin").innerText = data.message;
  
    if (response.ok) {
      document.getElementById("mensagemLogin").style.color = "green";
    } else {
      document.getElementById("mensagemLogin").style.color = "red";
    }
  });
  