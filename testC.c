#include <Python.h>
 
int main () {
    // PyObject est un wrapper Python autour des objets qu'on
    // va échanger enter le C et Python.
    PyObject *retour, *module, *fonction, *arguments;
    char *resultat;
 
    // Initialisation de l'interpréteur. A cause du GIL, on ne peut
    // avoir qu'une instance de celui-ci à la fois.
    Py_Initialize();   
 
    // Import du script. 
    PySys_SetPath("."); // Le dossier en cours n'est pas dans le PYTHON PATH
    module = PyImport_ImportModule("biblio");
 
    // Récupération de la fonction
    fonction = PyObject_GetAttrString(module, "yolo");
 
    // Création d'un PyObject de type string. Py_BuildValue peut créer
    // tous les types de base Python. Voir :
    // https://docs.python.org/2/c-api/arg.html#c.Py_BuildValue
    arguments = Py_BuildValue("(s)", "Leroy Jenkins"); 
 
    // Appel de la fonction.
    retour = PyEval_CallObject(fonction, arguments);
 
    // Conversion du PyObject obtenu en string C
    PyArg_Parse(retour, "s", &resultat);
 
    printf("Resultat: %s\n", resultat);
 
    // On ferme cet interpréteur.
    Py_Finalize(); 
    return 0;
}