public class Day04P2Git {
  public static void main(String[] args) {
    File day3File = new File("Day04-imput-complete.txt");

    Day4 day4 = new Day4();

    try (Scanner myReader = new Scanner(day3File)) {
      int line = 0;

      int boardId = 0;
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        if (line == 0) {
          day4.addBingoData(Arrays.stream(data.split(",")).map(Integer::parseInt).collect(Collectors.toList()));
        } else if (data.isEmpty()) {
          // then we know the board is coming up
          // take the next 5 lines and build a board
          Board board = new Board(5, 5, boardId);

          for (int i = 0; i < 5; i++) {
            String boardLine = myReader.nextLine();
            // borrowed from:
            // https://stackoverflow.com/questions/12571338/java-regex-to-split-numbers-with-unknown-number-of-spaces
            List<Integer> splitNums = Arrays.stream(boardLine.split("\\s+")).filter(num -> !num.isEmpty())
                .map(Integer::parseInt).collect(Collectors.toList());
            board.addLine(splitNums);
          }
          day4.addBoard(board);
          boardId++;
          line += 5;
        }

        line++;
      }
    } catch (Exception e) {
      e.fillInStackTrace();
      System.err.println(e);
    }
    System.out.println(day4.playBingo());
  }

  private final List<Integer> bingoData;
  private final List<Board> boards;

  public Day4() {
    bingoData = new ArrayList<>();
    boards = new ArrayList<>();
  }

  public void addBingoData(List<Integer> bingoData) {
    this.bingoData.addAll(bingoData);
    System.out.printf("bingo data of size: %d set", this.bingoData.size());
  }

  private void addBoard(Board board) {
    this.boards.add(board);
  }

  public int playBingo() {
    // go through each bingo data entry
    // play the entry on each of the boards in order
    // check if there is a bingo, on the 4th entry onwards
    System.out.println("We are now playing bingo");
    int finishedBoardCount = 0;
    for (int i = 0; i < bingoData.size(); i++) {
      for (Board board : boards) {
        if (board.isDone()) {
          continue;
        }
        board.placeCounter(bingoData.get(i));

        if (i > 3 && board.hasBingo()) {
          System.out.println("This board has bingo!");
          System.out.println("sum: " + board.getUnmarkedSum() + " bingoed on: " + bingoData.get(i));
          // we then start checking for bingos - for part 1
          // return board.getUnmarkedSum() * bingoData.get(i);
          board.markBingod();
          finishedBoardCount++;
        }
        // for part 2
        if (finishedBoardCount == boards.size()) {
          System.out.println("This is the last board to have finished: " + board.getId());
          return board.getUnmarkedSum() * bingoData.get(i);
        }
      }
    }
    // no winners
    return -1;

    // if there is a winner, then sum the unmarked entries on the board
    // multiplied by the number that was just called
  }

  private static class Board {
    private final int height;
    private final int width;
    /**
     * I opted to denormalise the look ups, where the sum is calculated per counter
     * placed and the row and column look ups are semi-O(n).
     */
    private int overallSum;
    private final int[] markedRows;
    private final int[] markedColumns;
    /**
     * A hashmap is chosen to speed up the counter placements to prevent a full
     * board scan
     */
    private final Map<Integer, Cell> board;
    private int fillCount = 0;
    // this is just for part 2
    private boolean isFinished;
    // for debugging purposes
    private final int boardId;
    private final int[][] reference;

    public Board(int width, int height, int count) {
      this.width = width;
      this.height = height;
      this.boardId = count;
      this.reference = new int[height][width];
      this.markedColumns = new int[width];
      this.markedRows = new int[height];
      board = new HashMap<>(height * width);
    }

    public void addLine(List<Integer> line) {
      for (int i = 0; i < line.size(); i++) {
        reference[fillCount][i] = line.get(i);
        // assuming no duplicates
        board.put(line.get(i), new Cell(i, fillCount));
      }
      overallSum += line.stream().reduce(0, Integer::sum);

      fillCount++;
    }

    public void placeCounter(int counter) {
      // locate the counter and mark it
      // assume no duplicate numbers
      if (board.containsKey(counter) && !board.get(counter).isMarked()) {
        board.get(counter).mark();
        markedColumns[board.get(counter).getY()]++;
        markedRows[board.get(counter).getX()]++;
        overallSum -= counter;
      }
    }

    public boolean hasBingo() {
      // vertical or horizontal
      for (int row : markedRows) {
        if (row == height) {
          return true;
        }
      }
      for (int column : markedColumns) {
        if (column == width) {
          return true;
        }
      }
      return false;
    }

    public int getUnmarkedSum() {
      // ideally the sum is already made, and we subtract it as we
      // move through the game
      return overallSum;
    }

    public void markBingod() {
      isFinished = true;
    }

    public boolean isDone() {
      return isFinished;
    }

    public int getId() {
      return boardId;
    }
  }

  private static class Cell {
    private final int x;
    private final int y;
    private boolean isMarked = false;

    public Cell(int x, int y) {
      this.x = x;
      this.y = y;
    }

    public void mark() {
      isMarked = true;
    }

    public boolean isMarked() {
      return isMarked;
    }

    public int getX() {
      return x;
    }

    public int getY() {
      return y;
    }
  }
}
