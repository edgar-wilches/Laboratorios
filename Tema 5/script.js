const welcomeButton = document.getElementById("welcomeButton");
welcomeButton.addEventListener("click", () => {
  alert("¡Bienvenido a mi página!");
});

const form = document.getElementById("contactform");
form.addEventListener("submit", function (event) {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;

  if (name === "" || email === "") {
    alert("Por favor, completa todos los campos.");
    event.preventDefault();
  } else {
    alert("¡Formulario enviado correctamente!");
  }
});
