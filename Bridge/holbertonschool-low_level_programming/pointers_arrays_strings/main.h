#ifndef _MAIN_H
#define _MAIN_H

/* Function to print a single character to stdout */
int _putchar(char c);

/* Resets the value of an integer variable to 98 */
void reset_to_98(int *n);

/* Swaps the values of two integers */
void swap_int(int *a, int *b);

/* Returns the length of a string */
int _strlen(char *s);

/* Prints a string to stdout */
void _puts(char *str);

/* Prints a string in reverse order */
void print_rev(char *s);

/* Reverses a given string */
void rev_string(char *s);

/* Prints every other character of a string (starting with the first) */
void puts2(char *str);

/* Prints the second half of a string */
void puts_half(char *str);

/* Prints the elements of an array of integers */
void print_array(int *a, int n);

/* Copies the content of one string to another */
char *_strcpy(char *dest, char *src);

/* Converts a string to an integer */
int _atoi(char *s);

#endif /* _MAIN_H */
