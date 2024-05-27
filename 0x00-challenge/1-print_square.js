#!/usr/bin/node
/*
    Print a square with the character #
    
    The size of the square must be the first argument 
    of the program.
*/

// Check if the size argument is provided
if (process.argv.length !== 3) {
    process.stderr.write("Error: Missing or too many arguments.\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1);
}

// Parse the size argument as an integer
const size = parseInt(process.argv[2]);

// Check if the size is a valid positive integer
if (isNaN(size) || size <= 0 || !Number.isInteger(size)) {
    process.stderr.write("Error: Invalid size.\n");
    process.stderr.write("Size must be a positive integer.\n");
    process.exit(1);
}

// Print the square
for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
        row += '#';
    }
    console.log(row);
}