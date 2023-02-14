public class Day04score {

  public static void main(String[] args) {
    int[][] last =
  {
    {12, 3, 31, 93, 8},
    {20, 27, 51, 78, 9},
    {29, 46, 82, 85, 75},
    {15, 76, 91, 70, 63},
    {59, 39, 13, 43, 79}
  };
    boolean[][] colored = new boolean[5][5];
    int [] numbers = {
      85, 84, 30, 15, 46, 71, 64, 45, 13, 90, 63, 89, 62, 25, 87, 68, 73, 47, 65, 78, 2, 27, 67, 95, 88, 99, 96, 17, 42, 31, 91, 98, 57, 28, 38, 93, 43, 0, 55, 49, 22, 24, 82, 54, 59, 52, 3, 26, 9, 32, 4, 48, 39, 50, 80, 21, 5, 1, 23, 10, 58, 34, 12, 35, 74, 8, 6, 79, 40, 76, 86, 69, 81, 61, 14, 92, 97, 19, 7, 51, 33, 11, 77
    };
    for (int i = 0; i < numbers.length; i++) {
      for(int x = 0; x < 5; x++){
        for (int y = 0; y < 5; y++) {
          if(last[x][y] == numbers[i]){
            colored[x][y] = true;
          }
        }
      }
    }
    int score = 0;
    for (int x = 0; x < 5; x++) {
      for (int y = 0; y < 5; y++) {
        if(colored[x][y] == false){
          score = score + last[x][y];
        }
      }
    }
    score = score * 77;
    System.out.println(score);
  }
}
