public class Day03 {

  public static void main(String[] args) {
String[] binary = {
};
boolean[][] valueBase2 = new boolean[binary.length][binary[1].length()];
    for (int i = 0; i < binary.length; i++) {
      for(int j = 0; j <binary[i].length(); j++){
        if (binary[i].charAt(j) == '1'){
          valueBase2[i][j] = true;
        }
      }
    }
    // for (int i = 0; i < valueBase2.length; i++) {
    //   for (int j = 0; j < valueBase2[i].length; j++ ) {
    //     if (valueBase2[i][j] == true) {
    //       System.out.print(1);
    //     }
    //     else{
    //       System.out.print(0);
    //     }
    //   }
    //   System.out.println();
    // }



    boolean[] gamma = new boolean[binary[1].length()];
    boolean[] epsilon = new boolean[gamma.length];
    for (int j = 0; j < gamma.length ; j++) {
      int counttrue = 0;
      int countfalse = 0;
      for(int i = 0; i < valueBase2.length; i++){
        if(valueBase2[i][j] == true){
          counttrue = counttrue + 1;
        }
        else{
          countfalse = countfalse + 1;
        }
      }
      if(counttrue >= countfalse){
          gamma[j] = true;

      }
      if(countfalse >= counttrue){
        epsilon[j] = true;

      }

    }

    for (int i = 0; i < gamma.length; i++ ) {
      if (gamma[i] == true) {
        System.out.print(1);
      }
      else{
        System.out.print(0);
      }
    }
    System.out.println();
    for (int i = 0; i < epsilon.length; i++ ) {
      if (epsilon[i] == true) {
        System.out.print(1);
      }
      else{
        System.out.print(0);
      }
    }
    System.out.println();
    int gammadez = 0;
    for(int i = 0; i< gamma.length; i++){
      gammadez = 2 * gammadez;
      if(gamma[i] == true){
        gammadez = gammadez + 1;
      }
    }
    System.out.println(gammadez);
    int epsilondez = 0;
    for(int i = 0; i< epsilon.length; i++){
      epsilondez = 2 * epsilondez;
      if(epsilon[i] == true){
        epsilondez = epsilondez + 1;
      }
    }
    System.out.println(epsilondez);
    System.out.println(epsilondez * gammadez);
  }
}
