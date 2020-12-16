#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to Python object
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	int size, i = -1;

	size = ((int)Py_SIZE(p));
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)list->allocated);
	while (++i < size)
		printf("Element %d: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
