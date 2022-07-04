#include <Python.h>
#include <stdio.h>
/**
 * void print_python_list_info - prints some basic info about
 * Python lists
 * @PyObject: a pointer to python list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyVarObject *list;
	Py_ssize_t list_size;
	Py_ssize_t allocated;
	Py_ssize_t index;
	PyObject *curr;
	PyTypeObject *curr_type;

	if (!PyList_Check(p))
		return;
	list_size = PyList_Size(p);

	/** 
	 * print size
	 */
	printf("[*] Size of the Python List = %ld\n", list_size);
	
	/**
	 * Print allocated
	 */
	list = (PyVarObject *) p;
	allocated = list->ob_size;
	printf("[*] Allocated = %ld\n", allocated);

	for (index = 0; index < list_size; index++)
	{
		curr = PyList_GetItem(p, index);
		curr_type = Py_TYPE(curr);
		
		/**
		 * print item 
		 */
		printf("Element %ld: %s\n", index, curr_type->tp_name);
	}
}
