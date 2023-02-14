
public class Day10 {
  public static void main(String[] args) {
    int[][] data {};
    int flashes = 0;
    for (int R = 0; R < 10; R++) {
      for (int i = 0; i < data.length; i++) {
        for (int j = 0; j < data[i].length; i++){
          data[i][j] ++;
        }
      }
      while(nohigherthen9(data)){
        for (int i = 0; i < data.length; i++) {
          for (int j = 0; j < data[i].length; j++) {
            if(data[i][j] >= 9){
              flashes ++;
              data[i][j] = 0;
              addneibourgs(data, i, j)
            }
          }
        }
      }
    }
  }
  public static int[][] (int[][] data, int x, int y){

    return int[][];
  }
  public static boolean (int [][] data){
    for (int i = 0; i < data.length; i++) {
      for (int j = 0; j< data[i].length; j++) {
        if(data[i][j] > 8){
          return false;
        }
      }
    }
    return true;
  }
}
