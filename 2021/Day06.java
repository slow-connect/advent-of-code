public class Day06 {
  public static void main(String[] args) {
    int[] fish = { 3, 5, 1, 5, 3, 2, 1, 3, 4, 2, 5, 1, 3, 3, 2, 5, 1, 3, 1, 5, 5, 1, 1, 1, 2, 4, 1, 4, 5, 2, 1, 2, 4, 3,
        1, 2, 3, 4, 3, 4, 4, 5, 1, 1, 1, 1, 5, 5, 3, 4, 4, 4, 5, 3, 4, 1, 4, 3, 3, 2, 1, 1, 3, 3, 3, 2, 1, 3, 5, 2, 3,
        4, 2, 5, 4, 5, 4, 4, 2, 2, 3, 3, 3, 3, 5, 4, 2, 3, 1, 2, 1, 1, 2, 2, 5, 1, 1, 4, 1, 5, 3, 2, 1, 4, 1, 5, 1, 4,
        5, 2, 1, 1, 1, 4, 5, 4, 2, 4, 5, 4, 2, 4, 4, 1, 1, 2, 2, 1, 1, 2, 3, 3, 2, 5, 2, 1, 1, 2, 1, 1, 1, 3, 2, 3, 1,
        5, 4, 5, 3, 3, 2, 1, 1, 1, 3, 5, 1, 1, 4, 4, 5, 4, 3, 3, 3, 3, 2, 4, 5, 2, 1, 1, 1, 4, 2, 4, 2, 2, 5, 5, 5, 4,
        1, 1, 5, 1, 5, 2, 1, 3, 3, 2, 5, 2, 1, 2, 4, 3, 3, 1, 5, 4, 1, 1, 1, 4, 2, 5, 5, 4, 4, 3, 4, 3, 1, 5, 5, 2, 5,
        4, 2, 3, 4, 1, 1, 4, 4, 3, 4, 1, 3, 4, 1, 1, 4, 3, 2, 2, 5, 3, 1, 4, 4, 4, 1, 3, 4, 3, 1, 5, 3, 3, 5, 5, 4, 4,
        1, 2, 4, 2, 2, 3, 1, 1, 4, 5, 3, 1, 1, 1, 1, 3, 5, 4, 1, 1, 2, 1, 1, 2, 1, 2, 3, 1, 1, 3, 2, 2, 5, 5, 1, 5, 5,
        1, 4, 4, 3, 5, 4, 4};
    long[] fishes = new long[9];
    for (int i = 0; i < fish.length; i++) {
      fishes[fish[i]] = fishes[fish[i]] + 1;
    }
    for (int i = 0; i < fishes.length; i++) {
      System.out.println(fishes[i]);
    }
    for (int i = 0; i < 256; i++) {
      long zeros = fishes[0];
      long ones = fishes[1];
      long two = fishes[2];
      long tree = fishes[3];
      long four = fishes[4];
      long five = fishes[5];
      long six = fishes[6];
      long seven = fishes[7];
      long eight = fishes[8];

      fishes[8] = zeros;
      fishes[7] = eight;
      fishes[6] = seven + zeros;
      fishes[5] = six;
      fishes[4] = five;
      fishes[3] = four;
      fishes[2] = tree;
      fishes[1] = two;
      fishes[0] = ones;
      // if (i % 5 == 0) {
      // for (int k = 0; k < 6; k++) {
      // System.out.println(fishes[k]);
      // }
      // System.out.println();
      // System.out.println();
      // }
      long total = 0;
      for (int k = 0; k < fishes.length; k++) {
        total = total + fishes[k];
      }
      System.out.println(i + ": " + total);
    }
  }

  public static int[] add(int[] fish) {
    int[] tmp = new int[fish.length + 1];
    for (int i = 0; i < fish.length; i++) {
      tmp[i] = fish[i];
    }
    tmp[fish.length] = 8;
    return tmp;
  }
}
