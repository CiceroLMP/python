(function () {
    const body = document.body;
    const botao = document.getElementById("btn-modo-escuro");
    const icone = botao ? botao.querySelector("i") : null;

    function aplicarModo(escuro) {
        body.classList.toggle("modo-escuro", escuro);
        if (icone) {
            icone.classList.toggle("bi-moon-stars", !escuro);
            icone.classList.toggle("bi-sun-fill", escuro);
        }
    }

    // Restaura a preferência salva ao carregar a página
    const preferenciaSalva = localStorage.getItem("modoEscuro") === "true";
    aplicarModo(preferenciaSalva);

    if (botao) {
        botao.addEventListener("click", function () {
            const novoEstado = !body.classList.contains("modo-escuro");
            aplicarModo(novoEstado);
            localStorage.setItem("modoEscuro", novoEstado);
        });
    }
})();
