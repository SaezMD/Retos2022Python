#58 ¡HOLA MUNDO!
"""
 * Escribe un !Hola Mundo! en todos los lenguajes de programación que puedas.
 * Seguro que hay algún lenguaje que te llama la atención y nunca has utilizado, o quizás quieres dar tus primeros pasos... ¡Pues este es el momento!
 *
 * A ver quién se atreve con uno de esos lenguajes que no solemos ver por ahí...
"""

#Python
print("Hello World")

#JavaScript 
console.log('Hello World');

alert("Hello, World!");

document.write('Hello, World!');

#HTML/CSS

<!DOCTYPE html>
<html>
  <head>
    <meta charset="uft-8">
    <title>Hello World in HTML</title>
  </head>
  <body>
    <h1>MY first line in HTML</h1>
  </body>
</html>

#C

#include <stdio.h>
int main() {
   // printf() displays the string inside quotation
   printf("Hello, World!");
   return 0;
}

#C#

// Hello World! program
namespace HelloWorld
{
    class Hello {         
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello World!");
        }
    }
}

#C++

#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}

#Perl

#!/usr/bin/perl 
  
use strict; 
use warnings; 
  
# Print function  
print("Hello World\n"); 


#R

print("Hello World!", quote = FALSE)

#COBOL

IDENTIFICATION DIVISION.
PROGRAM-ID. IDSAMPLE.
ENVIRONMENT DIVISION.
PROCEDURE DIVISION.
    DISPLAY 'HELLO WORLD'.
    STOP RUN.

#GO (GOlang)

package main 
import "fmt";
// Main function
func main() {
 
    fmt.Println("!... Hello World ...!")
}

#Ruby

puts "Hello World"