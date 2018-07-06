// use this to try to communicate https://stackoverflow.com/questions/48542644/python-and-windows-named-pipes
// use this to make a .exe file https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263 
// use this to return pointer to an array https://www.tutorialspoint.com/cplusplus/cpp_return_arrays_from_functions.htm 
#include <cstdlib>

// 
int * minmax(int depth, bool isPlayer1, int *player1Pieces, int *player2Pieces, int *player1Moves, int *player2Moves):

// return a random value for each configuration 
int EasyHeuristic():
    return rand()

// return a value based on how many more checker pieces you have compared to your opponent
int MidyHeuristic():

// reutnr a value based o nhow many more checker pieces you have, and how advantageously they are positioned
int HardHeuristic():
    