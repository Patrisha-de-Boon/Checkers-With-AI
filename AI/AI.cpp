// use this to try to communicate https://stackoverflow.com/questions/48542644/python-and-windows-named-pipes
// use this to make a .exe file https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263 
// use this to return pointer to an array https://www.tutorialspoint.com/cplusplus/cpp_return_arrays_from_functions.htm 
// used this for algorithm pseudocode https://gamedev.stackexchange.com/questions/31166/how-to-utilize-minimax-algorithm-in-checkers-game 
#include <cstdlib>

#define MAX_DEPTH 2
#define FLT_MAX std::numeric_limits<float>::max()
// 
// int * minmax(int depth, bool isPlayer1, int *player1Pieces, int *player2Pieces, int *player1Moves, int *player2Moves):

float EvaluatePositionRecursive(int depth, Board curBoard, int signFactor, int difficulty)
{
  if ( depth >= MAX_DEPTH )
    return EvaluateBoard(curBoard);
  MoveList moves = GenerateMoveList(curBoard);
  float positionValue = -FLT_MAX;
  for (int i = 0; i<
      move in moves) {
    Board newBoard = MakeMove(curBoard, move);
    float newValue = signFactor*EvaluatePositionRecursive(depth+1, newBoard, -signFactor);
    if ( newValue > posValue ) posValue = newValue;
  }
  return signFactor*posValue;
}

Move MinMax(int depth, Board curBoard, int signFactor, int difficulty) {
    
}

Move MinMaxRecursion(int depth, Board curBoard, Moves moves, int movesIndex, int posValue, int signFactor, int difficulty) {
    if (depth >= MAX_DEPTH) {
        return EvaluateBoard(curBoard);
    }
    if (movesIndex>sizeof(moves)) {
         
    }

}

float EvaluateBoard(Board curBoard, int difficulty) {
    if (difficulty == 1){
        return EasyHeuristic();
    }
    if (difficulty == 1){
        return MidHeuristic(curBoard);
    }
    if (difficulty == 1){
        return HardHeuristic(curBoard);
    }
}

// return a random value for each configuration 
float EasyHeuristic(): {
    return rand();
}

// return a value based on how many more checker pieces you have compared to your opponent
float MidHeuristic() {
    return rand();
}
    
// reutnr a value based o nhow many more checker pieces you have, and how advantageously they are positioned
float HardHeuristic():{
    return rand();
}