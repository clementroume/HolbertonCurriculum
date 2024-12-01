#include <unistd.h>

/**
 * _strcpy - function that copies a string to another
 * @src: Source string
 * @dest: Destination string
 *
 * Return: Copied string
 */
char *_strcpy(char *dest, char *src)
{
	int i = -1;

	/* Copy characters from src to dest until null terminator is reached */
	while (src[++i])
		dest[i] = src[i];

	dest[i] = '\0'; /* Add null terminator to the destination string */
	return (dest);	/* Return the destination string */
}
