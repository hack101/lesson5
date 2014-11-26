A fantastic review of JavaScript's syntax can be found here: https://gist.github.com/wetmore/7610160. http://learn.jquery.com/javascript-101/ is also a very good resource. If you want to learn even more, I recommend the book "JavaScript: The Good Parts".

I won't go into as much depth, but I'll take 15 minutes to briefly describe the few concepts of JavaScript that are used most often.

If the first language you have learned is Java, JavaScript may look strange because it has no such thing called a class. In practice it means this: In Java, if you're (say) working on a game with lots of cars in it, you might want to make a `Car` object. But to make any object, in Java you have to first write a class called `Car` in a file named `Car.java`:

```java
// Java code
public class Car {
    String make;
    int topSpeed;
    String color;

    public Car(String make, int topSpeed, String color) {
        this.make = make;
        this.topSpeed = topSpeed;
        this.color = color;
    }

    public void drive(int duration) {
        System.out.println("Driving for " + duration + " minutes!");
    }

    public static void main(String[] args) {
        Car myCar = new Car("Tesla", 240, "steelblue");
        myCar.drive(45);
    }
}
```

In contrast, in JavaScript we'll do something like this:
```javascript
// JavaScript code
var myCar = {
    make: "Tesla",
    topSpeed: 240, 
    color: "steelblue",
    drive: function(duration) {
        console.log("Driving for " + duration + " minutes!");
    }
}

myCar.drive(45);
```

(There is in fact a way to use the `new` keyword in JavaScript and make things look a lot like Java using function prototypes, but I won't go into that today.)

Let me point out some key features of JavaScript:
- There is no such thing called a "class" is javascript. You can make objects on the fly, and objects have a lot more in common with Python dictionaries than Java objects: They're just a map from a set of keys to a set of values.
- Javascript is an interpreted language like Python, so you can type code in line by line and see them execute! This allows you to enjoy a very nice interactive programming experience. You can access the console in Chrome from that_strange_button_with_three_lines > More tools > JavaScript Console. I'll be using the console to type in most of the examples I present here in the console so that you can see the realtime effects.
- You can dynamically add variables and methods/functions (I'll be using the term method and function interchangeably) to objects. For example, if half way through your program you feel that your car should have a variable called `moving`, and a function called `brake`, you simply add it like this:
```javascript
myCar.moving = true;
myCar.brake = function() {
    console.log("Halting in 2 seconds!");
    this.moving = false;
}
```
- Instead of `System.out.println` for printing to console, you have `console.log`, but it behaves essentially the same way.
- In Java, type is a big thing: there are a slew of primitive types, and every class you declare make a new type. In contrast, there are only six types of entitities in JavaScript: `number`, `boolean`, `string`, `object`, `function`, and `undefined`. There is no inheritence, no polymorphism. All numbers are floating point numbers - there is no such thing called integers. You can print out the type of an expression using the `typeof` function.
```javascript
// Try these out in a console!
typeof(1)
// "number"
typeof(myCar)  // Make sure you have defined myCar first. See code above
// "object"
typeof(myCar.drive)
// "function"
```
- In Java, every variable has a type.
```java
// Java code
int topSpeed = 45;
topSpeed = "forty-five";  // ERROR: can't assign string to integer
```
In Javascript, variables don't have types - only values or expressions have types. Variables are happy to hold values of any type.
```javascript
// Javascript code
var topSpeed = 45;
console.log(typeof(topSpeed));
// "number"
topSpeed = "forty-five";  // No error.
console.log(typeof(topSpeed));
// "string"
```

- You do have `array`, but sometimes the behavior might not be what you expect:
```javascript
var myarray = [1,2,3]  // Use "[" brackets instead of "{" braces to initialize
console.log(myarray[0])
// 1  <-- Arrays are zero indexed and have familiar syntax for accessing items
console.log(myarray[4])
// undefined  <-- No bounds checking: Just returns undefined when out-of-bound

myarray[2] = "three" // One array can hold objects of different types
console.log(myarray);
// [1, 2, "three"]
```

- lengths of arrays and strings are easily accessible:
```javascript
console.log(myarray.length)
// 3

var str = "This is a string";
console.log(str.length)
// 16
```

- `for`, `while`, and `if` work exactly as you would expect: 
```javascript
var myarray = [1,2,3];

// This prints:
// 1
// 2
// 3
for (var i=0; i < myarray.length; i++) {
    console.log(myarray[i]);
}

// This does the same thing:
var k =0;
while(k < myarray.length) {
    console.log(myarray[i]);
    k = k + 1;
}

// This will print "Javascript looks cool"
var youUnderstand = true;
if (youUnderstand) {
    console.log("Javascript looks cool ^_^");
}
else {
    console.log("Javascript is just weird :S")
}
```

##### Callback functions
The most critical thing that you will have to wrap your head around is that variables can hold functions, and functions behave just like regular objects except for the fact that they can be "called"/"executed".

Look at this code:
```javascript
// Example 1
function sayHello(name) {
    console.log("Hello" + name + "!");
}

sayHello("Turing");
// Hello Turing!

// Example 2
var sayHello = function(name) {
    console.log("Hello" + name + "!");
};

sayHello("Turing");
// Hello Turing!
```

In the second example, the function was first defined as an anonymous function (i.e. function that doesn't have a name.) We then assigned it to the variable `sayHello`, just like we could assign the number `42` to the variable `sayHello`. In Java/C/C++ there is no analogue of anonymous functions, so this might be an entirely new concept for many. Let's look at some of the things anonymous functions allow us to do:
- You can reassign the function to some other variable:
```javascript
var greet = sayHello;  // greet now has whatever sayHello had
greet("Turing");  // This is executing the same function.
// Hello Turing!
```
- You can take in a function as an argument of another function: 
```javascript
var sayHello = function(name) {
    console.log("Hello " + name + "!");
};

var sayHey = function(name) {
    console.log("Hey " + name + "!");
};

var beNice = function (greetCallback, name) {
    // We take in a function as an argument and execute it
    greetCallback(name);  
};

beNice(sayHello, "Turing");
// Hello Turing!
beNice(sayHey, "Turing");
// Hey Turing!
```
The functions that are taken in as arguments of other functions are sometimes called *callback functions*. We will casually say things like _"The $.get function takes a callback function that processes the result of the request."_
- But suppose, as a one-off case, you want to greet someone with "Yo". You don't want to declare a `sayYo` variable because you know you'll only use it once.You can define the callback as an anonymous function, and you can define in-place as you pass it in the arguments of beNice:
```javascript
beNice(function(name) {console.log("Yo " + name + "!");}, "Turing");
// Yo Turing!

// Let's just write that again but with better readability:
beNice( function(name) {
            console.log("Yo " + name + "!");
        }, 
        "Turing");
// Yo Turing!
```

