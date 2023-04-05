const precoCombustivel = 5.99;
const kmPorLitros = 6;
const distanciaEmKM = 600;

const litrosConsumidos = distanciaEmKM / kmPorLitros;
const valorGasto = litrosConsumidos * precoCombustivel;
console.log(valorGasto.toFixed(2));