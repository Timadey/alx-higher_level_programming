#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - prints some basic info about
 * Python lists
 * @p: a pointer to python list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t list_size;
	Py_ssize_t allocated;
	Py_ssize_t index;
	PyObject *curr;
	PyTypeObject *curr_type;

	if (!PyList_Check(p))
		return;

	list_size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", list_size);

	list = (PyListObject *)p;
	allocated = list->allocated;
	printf("[*] Allocated = %ld\n", allocated);

	for (index = 0; index < list_size; index++)
	{
		curr = PyList_GetItem(p, index);
		curr_type = Py_TYPE(curr);
		printf("Element %ld: %s\n", index, curr_type->tp_name);
	}
}
/**
 * print_python_bytes - print info about python bytes object
 * p: the Python byte object
 * Return void
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("[ERROR] Invalid Bytes Object\n");
	else
	{
		printf("size: %ld\n", PyBytes_Size(p));

