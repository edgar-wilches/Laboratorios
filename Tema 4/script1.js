// Bucle para realizar múltiples operaciones
while (true) {
  let a = parseFloat(prompt("Ingrese el primer número"));
  let b = parseFloat(prompt("Ingrese el segundo número"));
  let operacion = prompt(
    "Ingrese la operación (+ , - , * , / ) o 'salir' para terminar:"
  );

  // Salir del bucle si el usuario escribe 'salir'
  if (operacion.toLocaleLowerCase() === "salir") {
    console.log("Has salido de la calculadora.");
    document.write("\nHas salido de la calculadora.");
    break;
  }

  // Función calculadora
  function realizarOperacion(num1, num2, operacion) {
    if (isNaN(num1) || isNaN(num2)) {
      console.log("Error: Uno de los valores ingresados no es válido");
      return "Entrada no válida"; // Verifica si las entradas están vacías
    }
    // Operaciones
    if (operacion == "+") {
      return num1 + num2;
    } else if (operacion == "-") {
      return num1 - num2;
    } else if (operacion == "*") {
      return num1 * num2;
    } else if (operacion == "/") {
      if (num2 == 0) {
        console.log("Error: División por 0.");
        return "Error: División por cero";
      } else {
        return num1 / num2;
      }
    } else {
      console.log("Error: Operación no válida");
      return "Operación no válida";
    }
  }

  let resultado = realizarOperacion(a, b, operacion);

  console.log("El resultado es: " + resultado);
  document.write("El resultado es: " + resultado + "<br>");
}
