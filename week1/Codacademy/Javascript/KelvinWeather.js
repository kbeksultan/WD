const kelvin = 0; // constant variable
const celsius = kelvin - 273;// convert from kelvin to celsius
let fahrenheit = celsius * (9/5) + 32;// convert from cel to far
fahrenheit = Math.floor(fahrenheit);// to round
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

let newton = celsius * (33/100);//convert to newton

newton = Math.floor(newton);
console.log(`The temperature in newton ${newton}`)

